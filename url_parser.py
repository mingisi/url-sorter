""" This script is written run via console
all the unique hostnames and the number
of occurrences of that hostname found in the file.
will be displayed in the following format:

    <num_of_occurrences> <hostname>
"""

from murl import Url
import sys
import sqlite3
import db_utils


def get_file():
    """Returns the absolute path to the file, first arg passed through the console"""

    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        raise ValueError('Please provide a input file.')


def store(conn, filename):
    """
    Return a dictionary of domain and count.
    :param conn: the Connection object
    :param filename: file path to the list of url
    :return:
    """
    try:
        with open(filename, "r") as urlfile:
            for line in urlfile:
                pline = process_line(line)
                if pline != '' and db_utils.db_exist(conn, (pline,)):
                    db_utils.update_url(conn, (pline,))
                else:
                    db_utils.db_insert(conn, (pline, 1,))
    except IOError as error:
        raise IOError('File does not exist.') from error


def process_line(line):
    """Return a list of hostnames wi th www removed

    >>> process_line('https://abcd.com/asdasd')
    'abcd.com'

    >>> process_line('http://abce.com')
    'abce.com'

    >>> process_line('http://www.abcd.com/dsdsd')
    'abcd.com'

    >>> process_line('invalid_url')
    ''
    """
    ext = Url(line.rstrip('\n').lower())
    return ext.host.replace("www.", "")

def main():
    """Prints a sorted list"""

    # get the file name from the console
    filename = get_file()

    # create db connection
    conn = db_utils.db_connection()
    with conn:
        # create a table
        db_utils.db_create(conn)

        # add the hostname and occurrence to the db
        store(conn, filename)

        # select all host name
        db_utils.db_select_all(conn)   # create a table

        # conn.commit()

    conn.close()

    db_utils.db_terminate()


if __name__ == "__main__":
    # import doctest
    # doctest.testmod()
    main()
