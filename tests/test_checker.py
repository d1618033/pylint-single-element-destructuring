import astroid

from pylint_single_element_destructuring import checker
import pylint.testutils


class TestUniqueReturnChecker(pylint.testutils.CheckerTestCase):
    CHECKER_CLASS = checker.SingleElementDestructuring

    def _assert_no_error(self, code):
        node = astroid.extract_node(code)
        with self.assertNoMessages():
            self.checker.visit_assign(node)

    def _assert_error(self, code):
        node = astroid.extract_node(code)
        with self.assertAddsMessages(
            pylint.testutils.Message(
                msg_id=self.CHECKER_CLASS.SINGLE_ELEMENT_DESTRUCTURING_MSG,
                node=node,
            ),
        ):
            self.checker.visit_assign(node)

    def test_no_error(self):
        self._assert_no_error("a, b = [1, 2]")

    def test_error_lhs_tuple_destructuring(self):
        self._assert_error("(a,) = [1]")

    def test_error_lhs_list_destructuring(self):
        self._assert_error("[a] = [1]")
