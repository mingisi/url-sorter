import pytest
from .context import url_parser, db_utils

DB_PATH = "./test_file.db"
TABLE_NAME = "test_file"

@pytest.fixture
def db_update_connect():
    db_utils.db_terminate(DB_PATH)
    return db_utils.db_connection(DB_PATH)

def test_io_error(db_update_connect):
    """ Testing if we get list of domain names
    """
    with pytest.raises(IOError, match=r"File does not exist."):
        url_parser.store(db_update_connect, "files/test1.txt")
