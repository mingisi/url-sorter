import pytest
from .context import db_utils
from sqlite3 import Error

DB_PATH = "./tests/db/test_update.db"
TABLE_NAME = "test_update"


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


def test_update(db_connect):
    """ updating a record in db
    """

    db_utils.update_url(db_connect, ('abcd',), TABLE_NAME)
    rows = db_utils.db_select_all(db_connect, TABLE_NAME)
    db_connect.close()

    # then
    assert len(rows) == 1
    assert rows[0][0] == "abcd"
    assert rows[0][1] == 2

def test_error(db_connect):
    """ testing the error is raised when table name is incorrect
    """
    with pytest.raises(Error, match=r"no such table.*"):
        db_utils.update_url(db_connect, ('abcd',),'abcd')