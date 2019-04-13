import pytest
from .context import url_parser


@pytest.fixture
def domain_dict():
    return url_parser.get_domain_dict(["abcd.com", "abce.com", "abcd.com"])


def test_domain_dict(domain_dict):
    """ Testing if we get list of domain names
    """
    assert domain_dict['abcd.com'] == 2
    assert domain_dict['abce.com'] == 1
