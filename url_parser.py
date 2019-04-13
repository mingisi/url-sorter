""" This script is written run via console
all the unique hostnames and the number
of occurrences of that hostname found in the file.
will be displayed in the following format:

    <num_of_occurrences> <hostname>
"""

from murl import Url
import sys

def get_file():
    """Returns the absolute path to the file, first arg passed through the console"""

    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        raise ValueError('Please provide a input file.')


def get_lines(filename):
    """Return a content of given file.

    >>> get_lines("./tests/files/test1.txt")
    ['https://abcd.com/asdasd', 'http://abce.com', 'http://www.abcd.com/dsdsd']
    """
    content = []
    try:
        with open(filename, "r") as f:
            content = [line.rstrip('\n') for line in f]
        return content
    except IOError as error:
        raise IOError('File does not exist.') from error


def get_full_domain(url_list):
    """Return a list of domains.

    >>> get_full_domain(['https://abcd.com/asdasd', 'http://abce.com', 'http://www.abcd.com/dsdsd'])
    ['abcd.com', 'abce.com', 'abcd.com']
    """
    domains = []
    for url in url_list:
        ext = Url(url)
        domains.append(ext.host.replace("www.", ""))

    return domains


def get_domain_dict(domains):
    """Return a dictionary of domain and count.

    >>> get_domain_dict(["abcd.com", "abce.com", "abcd.com"])
    {'abcd.com': 2, 'abce.com': 1}

    """

    domainWithCount = {}
    for domain in domains:
        if domain in domainWithCount:
            domainWithCount[domain] += 1
        else:
            domainWithCount[domain] = 1

    return domainWithCount


def get_sorted_domain_dict(domain_dict):
    """Return a sorted list. ignoring case

    >>> get_sorted_domain_dict({'a': 3, 'b': 4, 'c': 3})
    {'b': 4, 'a': 3, 'c': 3}

    >>> get_sorted_domain_dict({'a': 3, 'b': 4, 'C': 3})
    {'b': 4, 'a': 3, 'C': 3}
    """
    sortedDomainDict = {}
    for key, value in sorted(domain_dict.items(), key=lambda item: (-item[1], item[0].lower())):
        sortedDomainDict[key] = value

    return sortedDomainDict


def display(sorted_domain_dict):
    """Prints a sorted list"""
    for key, value in sorted_domain_dict.items():
        print("%s  %s" % (value, key))


def main():
    filename = get_file()
    lines = get_lines(filename)
    domains_list = get_full_domain(lines)
    domain_dict = get_domain_dict(domains_list)
    sorted_domain_dict = get_sorted_domain_dict(domain_dict)
    display(sorted_domain_dict)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
