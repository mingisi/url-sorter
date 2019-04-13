import pytest
import sys
from .context import url_parser


# @pytest.fixture
# def domain_list():
#     return url_parser.get_lines("tests/files/test1.txt")


def test_get_file():
    """ Testing if we get list of domain names
    """
    sys.argv = ['programme_name', 'filename']
    assert url_parser.get_file() == 'filename'


def test_get_file_value_error():
    """ Testing if we get list of domain names
    """
    with pytest.raises(ValueError, match=r"Please provide a input file."):
        sys.argv = ['programme_name']
        url_parser.get_file()
