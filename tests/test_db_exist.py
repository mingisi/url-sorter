import pytest
from .context import db_utils
from sqlite3 import Error

DB_PATH = "./test_exist.db"
TABLE_NAME = "test_exist"


@pytest.fixture
def db_connect():
    db_utils.db_terminate(DB_PATH)
    INSERT_DATA = "INSERT INTO %s (hostname, occurrence) VALUES('abcd', 1)" % (TABLE_NAME)
    connection = db_utils.db_connection(DB_PATH)
    db_utils.db_create(connection, TABLE_NAME)
    cur = connection.cursor()
    cur.execute(INSERT_DATA)
    connection.commit()

    return connection


def test_exist(db_connect):
    """ check if the record exist, if so return true else false
    """
    exist_true = db_utils.db_exist(db_connect, ('abcd',), TABLE_NAME)
    exist_false = db_utils.db_exist(db_connect, ('dfg',), TABLE_NAME)
    rows = db_utils.db_select_all(db_connect, TABLE_NAME)

    db_connect.close()
    db_utils.db_terminate(DB_PATH)

    # then
    assert exist_true == True
    assert exist_false == False

def test_exist_error(db_connect):
    """ testing the error is raised when table name is incorrect
    """
    with pytest.raises(Error, match=r"no such table.*"):
        db_utils.db_exist(db_connect, ('abcd',), 'abcd')