import os
import sqlite3
from sqlite3 import Error

DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'hostnames.sqlite3')


def db_terminate(db_path=DEFAULT_PATH):
    """ removes the db file
    :param db_path: database file path
    :return:
    """
    try:
        if os.path.exists(db_path):
            os.remove(db_path)
    except:
        pass


def db_connection(db_path=DEFAULT_PATH):
    """ create a connection to db
    :param db_path: database file path
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_path)
        return conn
    except Error as e:
        print(e)
        raise

    return None


def db_clear(conn, table='urls'):
    """ create a table in the urls db
    :param conn: connection object
    :param table: table name, default is set to urls
    :return:
    """
    CLEAR_ALL = 'DELETE FROM "%s";' % table

    cur = conn.cursor()
    cur.execute(CLEAR_ALL)
    conn.commit()


def db_create(conn, table='urls'):
    """ create a table in the urls db
    :param conn: connection object
    :param table: table name, default is set to urls
    :return:
    """
    MAKE_TABLE = ''' CREATE TABLE IF NOT EXISTS %s (
                    hostname text PRIMARY KEY,
                    occurrence integer NOT NULL
                ); ''' % (table)
    try:
        cur = conn.cursor()
        cur.execute(MAKE_TABLE)
        conn.commit()
    except Error as error:
        print(error)
        raise


def db_insert(conn, urls, table='urls'):
    """
    insert hostname and occurrence to urls table
    :param conn: connection object
    :param urls: table values
    :return: hostname
    """
    INSERT_DATA = ''' INSERT INTO %s (hostname,occurrence)
              VALUES(?,?) ''' % (table)
    try:
        cur = conn.cursor()
        cur.execute(INSERT_DATA, urls)
        conn.commit()
        return cur.lastrowid
    except Error as error:
        print(error)
        raise


def update_url(conn, hostname, table='urls'):
    """
    increment the occurrence value of given hostname
    :param conn: connection object
    :param hostname:
    :return:
    """
    UPDATE_ROW = ''' UPDATE %s
              SET occurrence = occurrence + 1
              WHERE hostname = ?''' % (table)
    try:
        cur = conn.cursor()
        cur.execute(UPDATE_ROW, hostname)
        conn.commit()
    except Error as error:
        print(error)
        raise


def db_exist(conn, hostname, table='urls'):
    """
    check if a given hostname exist in the urls table
    :param conn: connection object
    :return: True | False
    """
    SELECT_ALL = '''
        SELECT 1 FROM %s WHERE hostname = ? LIMIT 1 
        ''' % (table)
    try:
        cur = conn.cursor()
        cur.execute(SELECT_ALL, hostname)
        if cur.fetchone():
            return True
    except (Error) as error:
        print(error)
        raise

    return False


def db_select_all_order(conn, table='urls'):
    """
    select all the rows in the urls table and print the result to console
    :param conn: connection object
    :return:
    """
    try:
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM %s ORDER BY occurrence DESC, hostname ASC" % (table))
        return cur.fetchall()

    except Error as error:
        print(error)
        raise


def db_select_all(conn, table='urls'):
    """
    select all the rows in the urls table and print the result to console
    :param conn: connection object
    :return:
    """
    try:
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM %s" % (table))
        rows = cur.fetchall()
        return rows
    except Error as error:
        print(error)
        raise
