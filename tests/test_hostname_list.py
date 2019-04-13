import pytest
from .context import url_parser


@pytest.fixture
def hostname_list():
    return url_parser.get_full_domain(['https://abcd.com/asdasd', 'http://abce.com', 'http://www.abcd.com/dsdsd'])
    
def test_hostname_list(hostname_list):
    """ Testing if we get list of domain names
    """
    assert hostname_list == ['abcd.com', 'abce.com', 'abcd.com']
