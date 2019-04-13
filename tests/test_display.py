import pytest
from .context import url_parser


def test_display(capsys):
    """ Testing display of dictionary
    """
    url_parser.display({'abcd.com': 2, 'abce.com': 1})
    captured = capsys.readouterr()
    assert captured.out == "2  abcd.com\n1  abce.com\n"


