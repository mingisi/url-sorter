import pytest
from .context import url_parser


@pytest.fixture
def domain_list():
    return url_parser.get_lines("tests/files/test1.txt")


def test_domain_dict(domain_list):
    """ Testing if we get list of domain names
    """
    assert domain_list['abcd.com'] == 2
    assert domain_list['abce.com'] == 1
 
def test_io_error():
    """ Testing if we get list of domain names
    """
    with pytest.raises(IOError, match=r"File does not exist."):
        url_parser.get_lines("files/test1.txt")
