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

def get_race_data_byzip(zip_code):
    sql = "select * from race_2010 inner join zipcode_to_geoid on race_2010.state_id = zipcode_to_geoid.state_id and race_2010.county_id = zipcode_to_geoid.county_id and race_2010.tract_id = zipcode_to_geoid.tract_id and zipcode_to_geoid.zip_code = %s" % (zip_code)
    conn = db.connect()
    cursor = conn.cursor(buffered = True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def get_top_population():
    sql = "SELECT * FROM race_2010 order by total_pop desc limit 10"
    conn = db.connect()
    cursor = conn.cursor(buffered = True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result
