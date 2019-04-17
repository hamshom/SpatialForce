import database as db


def get_users():
    query = "SELECT * FROM spatialforce.GEO"
    return db.query_db(query)


def get_data():
    conn = db.connect()
    cursor = conn.cursor()
    sql = "SELECT * FROM spatialforce.Geo"
    cursor.execute(sql)
    result = cursor.fetchone()

    return result