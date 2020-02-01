import os
from collections import namedtuple

import pylint
import pytest

PylintError = namedtuple("PylintError", "file, row, col, err, message")


@pytest.fixture
def run_pylint(capsys):
    def _parse_output(output):
        start_parsing = False
        errors = []
        for line in output.splitlines():
            if "Module errors" in line:
                start_parsing = True
            if start_parsing:
                split_line = line.split(":")
                if len(split_line) != 5:
                    continue
                file, row, col, err, message = list(map(str.strip, split_line))
                row = int(row)
                col = int(col)
                errors.append(PylintError(file, row, col, err, message))
        return errors

    def _run(args):
        pylint.PylintRun(args, do_exit=False)
        output = capsys.readouterr().out
        return _parse_output(output)

    return _run


EXAMPLES_FOLDER = os.path.join(os.path.dirname(__file__), "..", "examples")


def test_examples_error(run_pylint):
    actual = run_pylint([os.path.join(EXAMPLES_FOLDER, "errors.py")])
    message = "Uses single element destructuring (single-element-destructuring)"
    file = "examples/errors.py"
    error = "W0001"
    expected = [
        PylintError(file, 12, 4, error, message),
        PylintError(file, 14, 4, error, message),
        PylintError(file, 16, 4, error, message),
        PylintError(file, 26, 8, error, message),
        PylintError(file, 27, 8, error, message),
        PylintError(file, 28, 8, error, message),
        PylintError(file, 37, 8, error, message),
        PylintError(file, 43, 8, error, message),
    ]
    assert actual == expected


def test_examples_no_error(run_pylint):
    actual = run_pylint([os.path.join(EXAMPLES_FOLDER, "no_errors.py")])
    assert len(actual) == 0
