import contextlib
from copy import deepcopy

import astroid

from pylint_single_element_destructuring import checker
import pylint.testutils


class TestUniqueReturnChecker(pylint.testutils.CheckerTestCase):
    CHECKER_CLASS = checker.SingleElementDestructuring

    @contextlib.contextmanager
    def _with_config(self, **kwargs):
        old_config = deepcopy(self.checker.config)
        for key, value in kwargs.items():
            setattr(self.checker.config, key, value)
        try:
            yield
        finally:
            self.checker.config = old_config

    def _assert_no_error(self, code):
        node = astroid.extract_node(code)
        with self.assertNoMessages():
            self.checker.visit_assign(node)

    def _assert_error(self, code, num_errors=1):
        node = astroid.extract_node(code)
        expected_message = pylint.testutils.Message(
            msg_id=self.CHECKER_CLASS.SINGLE_ELEMENT_DESTRUCTURING_MSG, node=node,
        )
        expected_messages = [expected_message] * num_errors
        with self.assertAddsMessages(*expected_messages):
            self.checker.visit_assign(node)

    def test_no_error(self):
        self._assert_no_error("a, b = [1, 2]")

    def test_annotation_assignment_no_error(self):
        self._assert_no_error("a: int = 1")

    def test_multiple_targets_without_destructuring(self):
        self._assert_no_error("a = b = 1")

    def test_multiple_targets_with_destructuring(self):
        self._assert_error("a, = b, = [1]", num_errors=2)
        self._assert_error("a, = b = [1]", num_errors=1)
        self._assert_error("a = b, = [1]", num_errors=1)

    def test_no_destructuring(self):
        self._assert_no_error("a = [1, 2]")

    def test_no_destructuring_class(self):
        self._assert_no_error(
            """
            class A:
                def __init__(self):
                    self._x = 1 #@
        """
        )

    def test_error_lhs_tuple_destructuring(self):
        self._assert_error("(a,) = [1]")

    def test_error_lhs_list_destructuring(self):
        self._assert_error("[a] = [1]")

    def test_ignore_lists_config(self):
        with self._with_config(ignore_single_element_list_destructuring=True):
            self._assert_no_error("[a] = [1]")
            self._assert_error("a, = [1]")
            self._assert_error("(a,) = [1]")
        self._assert_error("[a] = [1]")
        with self._with_config(ignore_single_element_list_destructuring=False):
            self._assert_error("[a] = [1]")
