import mysql.connector
from flask import g
from main import app
from sshtunnel import SSHTunnelForwarder


def connect():

    ssh_host = 'groups.ischool.berkeley.edu'
    ssh_user = ## ISCHOOL USERNAME
    ssh_port = 22
    ssh_p = ##ISCHOOL PASSWORD

    tunnel = SSHTunnelForwarder(
        (ssh_host, ssh_port),
        ssh_username=ssh_user,
        ssh_password=ssh_p,
        remote_bind_address=('localhost', 3306))

    tunnel.start()

    conn = mysql.connector.connect(user=app.config["USERNAME"],
                                   password=app.config["PASSWORD"],
                                   host=app.config["HOST"],
                                   database=app.config["DATABASE"] ,
                                   port = tunnel.local_bind_port)
    return conn


def disconnect_db():
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


def make_dicts(cursor, row):
    """
    Makes database results to a dictionary.
    :param cursor:
    :param row:
    :return:
    """
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))


def get_db():
    """
    :return:
    """
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = connect()
        db.row_factory = make_dicts
    return db


def fetch_all(cur):
    """
    :param cur:
    :return:
    """
    rv = []
    row = cur.fetchone()
    while row is not None:
        rv.append(make_dicts(cur,row))
        row = cur.fetchone()
    if len(rv) == 0:
        return None
    else:
        return rv


def query_db(query, args=(), one=False):
    """
    Args must be sent as a tuple, if you have one argument pass it as (value,)
    :param query:
    :param args:
    :param one:
    :return:
    """
    db = get_db()
    cur = db.cursor()
    cur.execute(query, args)
    rv = fetch_all(cur)
    cur.close()
    db.commit()
    return (rv[0] if rv else None) if one else rv
