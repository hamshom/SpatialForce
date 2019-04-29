import database as db


def get_users():
    query = "SELECT * FROM spatialforce.Geo"
    conn = db.connect()
    cursor = conn.cursor(buffered = True)
    cursor.execute(query)
    results = cursor.fetchall()
    return results


def get_data():
    conn = db.connect()
    cursor = conn.cursor(buffered = True)
    sql = "SELECT * FROM spatialforce.Geo"
    cursor.execute(sql)
    result = cursor.fetchmany()
    return result

def get_geo(state, county, tract):
    sql = "Select * FROM spatialforce.Geo where state = '%d' and county = '%d' and tract = '%d'" % (state, county, tract)
    conn = db.connect()
    cursor = conn.cursor(buffered = True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result
