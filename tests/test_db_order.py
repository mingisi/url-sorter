import pytest
from .context import db_utils
from sqlite3 import Error

DB_PATH = "./tests/db/test_exist.db"
TABLE_NAME = "test_exist"


@pytest.fixture
def db_connect():
    db_utils.db_terminate(DB_PATH)
    INSERT_DATA = "INSERT INTO %s (hostname, occurrence) VALUES(?, ?)" % (
        TABLE_NAME)
    connection = db_utils.db_connection(DB_PATH)
    db_utils.db_create(connection, TABLE_NAME)
    cur = connection.cursor()
    cur.executemany(INSERT_DATA, [('a', 3), ('b', 4), ('c', 3)])
    connection.commit()

    return connection


def test_order(db_connect):
    """ Testing if the order of the output is
        sorted in descending order based on number of occurrences,
        then alphabetical order
    """
    rows = db_utils.db_select_all_order(db_connect, TABLE_NAME)

    assert rows[0][1] == 4
    assert rows[0][0] == 'b'

    assert rows[1][1] == 3
    assert rows[1][0] == 'a'

    assert rows[2][1] == 3
    assert rows[2][0] == 'c'
    # assert tuple(sorted_domain_dict.keys()).index('a') == 1
    # assert tuple(sorted_domain_dict.keys()).index('c') == 2


def test_db_select_all_order_error(db_connect):
    """ testing the error is raised when table name is incorrect
    """
    with pytest.raises(Error, match=r"no such table.*"):
        db_utils.db_select_all_order(db_connect, 'abcd')

def test_db_select_all_error(db_connect):
    """ testing the error is raised when table name is incorrect
    """
    with pytest.raises(Error, match=r"no such table.*"):
        db_utils.db_select_all(db_connect, 'abcd')
