import pytest
from .context import url_parser


@pytest.fixture
def sorted_domain_dict():
    return url_parser.get_sorted_domain_dict({'a': 3, 'b': 4, 'c': 3})


def test_order(sorted_domain_dict):
    """ Testing if the order of the output is
        sorted in descending order based on number of occurrences,
        then alphabetical order
    """
    assert tuple(sorted_domain_dict.keys()).index('b') == 0
    assert tuple(sorted_domain_dict.keys()).index('a') == 1
    assert tuple(sorted_domain_dict.keys()).index('c') == 2
