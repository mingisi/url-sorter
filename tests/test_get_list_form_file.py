import pytest
from .context import url_parser


@pytest.fixture
def domain_list():
    return url_parser.get_lines("tests/files/test1.txt")


def test_domain_list_form_file(domain_list):
    """ Testing if we get list of domain names
    """
    assert domain_list == ['https://abcd.com/asdasd',
                           'http://abce.com', 'http://www.abcd.com/dsdsd']


def test_io_error():
    """ Testing if we get list of domain names
    """
    with pytest.raises(IOError, match=r"File does not exist."):
        url_parser.get_lines("files/test1.txt")
