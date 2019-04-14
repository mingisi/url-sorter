import pytest
from .context import db_utils
from sqlite3 import Error

DB_PATH = "./test_insert.db"
TABLE_NAME = "test_insert"


@pytest.fixture
def db_connect():
    db_utils.db_terminate(DB_PATH)
    connection = db_utils.db_connection(DB_PATH)
    db_utils.db_create(connection, TABLE_NAME)
    return connection


def test_insert(db_connect):
    """ Testing insert into db
    """
    # given
    db_utils.db_insert(db_connect, ('abcd.com', 1,), TABLE_NAME)

    # when
    cur = db_connect.cursor()
    cur.execute('SELECT * FROM %s' % (TABLE_NAME))
    rows = cur.fetchall()
    db_connect.close()
    db_utils.db_terminate(DB_PATH)

    # then
    assert len(rows) == 1
    assert rows[0][0] == "abcd.com"
    assert rows[0][1] == 1

    # print("%s  %s" % (row[1], row[0]))


def test_insert_error(db_connect):
    """ testing the error is raised when table name is incorrect
    """
    with pytest.raises(Error, match=r"no such table.*"):
        db_utils.db_insert(db_connect, ('abcd.com', 1,), 'abcd')

