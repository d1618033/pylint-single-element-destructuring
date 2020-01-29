from pylint.interfaces import IAstroidChecker
from pylint.checkers import BaseChecker


class SingleElementDestructuring(BaseChecker):
    __implements__ = IAstroidChecker

    name = 'single-element-destructuring-checker'

    msgs = {
        'C0001': 'Single element destructuring detected',
    }
    options = ()

    priority = -1

    def visit_importfrom(self, node):
        pass  # to be implemented


def register(linter):
    linter.register_checker(SingleElementDestructuring(linter))