import pytest
from .context import db_utils
from sqlite3 import Error

DB_PATH = "./test_clear.db"
TABLE_NAME = "test_clear"


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


def test_clear_db(db_connect):
    """ Testing if the db is cleared
    """
    db_utils.db_clear(db_connect, TABLE_NAME)
    rows = db_utils.db_select_all(db_connect, TABLE_NAME)

    assert len(rows) == 0
