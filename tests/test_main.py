import pytest
import sys
from .context import url_parser


def test_display(capsys):
    """ Testing display of dictionary
    """
    sys.argv = ['programme_name', 'tests/files/test2.txt']
    url_parser.main()
    captured = capsys.readouterr()
    assert captured.out == "3  twitter.com\n2  abcnews.go.com\n1  google.co.uk\n1  newsfeed.time.com\n1  world.time.com\n"


