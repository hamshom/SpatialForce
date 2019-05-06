import database as db
from random import randint

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

def get_top_10_zip_by_mean_housing_val():
    sql = "SELECT zip_code FROM spatialforce.zipcode_to_geoid inner join spatialforce.housing_value_2017 on housing_value_2017.state_id = zipcode_to_geoid.state_id and housing_value_2017.county_id = zipcode_to_geoid.county_id and housing_value_2017.tract_id = zipcode_to_geoid.tract_id order by housing_value_2017.mean_housing_value desc limit 10"
    conn = db.connect()
    cursor = conn.cursor(buffered = True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def get_bottom_10_zip_by_mean_housing_val():
    sql = "SELECT zip_code FROM spatialforce.zipcode_to_geoid inner join spatialforce.housing_value_2017 on housing_value_2017.state_id = zipcode_to_geoid.state_id and housing_value_2017.county_id = zipcode_to_geoid.county_id and housing_value_2017.tract_id = zipcode_to_geoid.tract_id order by housing_value_2017.mean_housing_value limit 10"
    conn = db.connect()
    cursor = conn.cursor(buffered = True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def get_top_10_zip_most_expensive_house():
    sql = "SELECT zip_code FROM spatialforce.zipcode_to_geoid inner join spatialforce.housing_value_2017 on housing_value_2017.state_id = zipcode_to_geoid.state_id and housing_value_2017.county_id = zipcode_to_geoid.county_id and housing_value_2017.tract_id = zipcode_to_geoid.tract_id order by housing_value_2017.num_most_exp_house desc limit 10"
    conn = db.connect()
    cursor = conn.cursor(buffered = True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def zipcode_log():
    query = "SELECT Zipcode, COUNT(*) AS Log FROM spatialforce.zipcodeLog GROUP BY Zipcode ORDER BY Log Desc"
    conn = db.connect()
    cursor = conn.cursor(buffered=True)
    cursor.execute(query)
    results = cursor.fetchall()
    return results

# DUMMIE FUNCTION for trend querying
def trend_query():
    data = [{
        "zipcode": "94704",
        "count": 9999
      },
      {
        "zipcode": "94889",
        "count": 888
      },
      {
        "zipcode": "92979",
        "count": 777
      }]
    return data

# DUMMIE FUNCTION for trend querying
# using the TYPE for querying and returns result
def rank_query(qtype):
    if(qtype=="pop"):
        data = {
            "top": [90003, 90004, 90005, 90006, 90007],
            "bottom": [99123, 99124, 99125, 99126, 99127]
        }
    else:
        tempArr = []
        for i in range(5):
            temp = randint(10000, 99999)
            tempArr.append(temp)
        data = {}
        data['top'] = tempArr
        data['bottom'] = tempArr

    print(data)
    return data
