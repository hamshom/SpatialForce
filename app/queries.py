import database as db
from random import randint

# def get_avg_housingprice_by_zip(zipcode):
#     query = "select AVG(housing_value_2017.mean_housing_value) from spatialforce.housing_value_2017 inner join spatialforce.zipcode_to_geoid on housing_value_2017.state_id = zipcode_to_geoid.state_id and housing_value_2017.county_id = zipcode_to_geoid.county_id and housing_value_2017.tract_id = zipcode_to_geoid.tract_id and zipcode_to_geoid.zip_code = %s" % (zipcode)
#     conn = db.connect()
#     cursor = conn.cursor(buffered = True)
#     cursor.execute(query)
#     results = cursor.fetchall()
#     return results


def get_avg_housingprice_by_zip(zipcode):
    query = "select AVG(housing_value_2017.mean_housing_value) from spatialforce.housing_value_2017 inner join spatialforce.zipcode_to_geoid on housing_value_2017.tract_pid = zipcode_to_geoid.tract_pid and zipcode_to_geoid.zip_code = %s" % (zipcode)
    conn = db.connect()
    cursor = conn.cursor(buffered = True)
    cursor.execute(query)
    results = cursor.fetchall()
    return results




def get_users(county):
    query = "SELECT Geo.county, Geo.tract, Geo.state, Geo.ID FROM spatialforce.Geo WHERE Geo.county = %s LIMIT 2" % (county)
    conn = db.connect()
    cursor = conn.cursor(buffered = True)
    cursor.execute(query)
    results = cursor.fetchall()
    return results

'''
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
'''
############## SEARCH QUERIES ####################

def get_population_byzip(zip_code):
    sql = "Select SUM(race_2010.total_pop) from spatialforce.race_2010 inner join spatialforce.zipcode_to_geoid on race_2010.tract_pid = zipcode_to_geoid.tract_pid and zipcode_to_geoid.zip_code = %s" % (zip_code)
    conn = db.connect()
    cursor = conn.cursor(buffered = True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def get_avg_income_byzip(zip_code):
    sql = "select AVG(income) from spatialforce.income_2013_2016 inner join spatialforce.zipcode_to_geoid on income_2013_2016.tract_pid = zipcode_to_geoid.tract_pid and zipcode_to_geoid.zip_code = %s" % (zip_code)
    conn = db.connect()
    cursor = conn.cursor(buffered = True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def get_number_college_grad_byzip(zip_code):
    sql = "select sum(pop_college_grad) from spatialforce.education_2017 inner join spatialforce.zipcode_to_geoid on education_2017.tract_pid = zipcode_to_geoid.tract_pid and zipcode_to_geoid.zip_code = %s" % (zip_code)
    conn = db.connect()
    cursor = conn.cursor(buffered = True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


'''
def get_top_population():
    sql = "SELECT * FROM race_2010 order by total_pop desc limit 10"
    conn = db.connect()
    cursor = conn.cursor(buffered = True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result
'''
################## RANK QUERIES #########################

def get_top_5_zip_by_mean_housing_val():
    sql = "SELECT zipcode_to_geoid.zip_code FROM spatialforce.zipcode_to_geoid inner join spatialforce.housing_value_2017 on housing_value_2017.tract_pid = zipcode_to_geoid.tract_pid order by housing_value_2017.mean_housing_value desc limit 5"
    conn = db.connect()
    cursor = conn.cursor(buffered = True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def get_bottom_5_zip_by_mean_housing_val():
    sql = "SELECT zipcode_to_geoid.zip_code FROM spatialforce.zipcode_to_geoid inner join spatialforce.housing_value_2017 on housing_value_2017.tract_pid = zipcode_to_geoid.tract_pid order by housing_value_2017.mean_housing_value  limit 5"
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

def get_top_5_zip_by_income():
    sql = "SELECT zip_code FROM spatialforce.zipcode_to_geoid inner join spatialforce.income_2013_2016 on  income_2013_2016.tract_pid = zipcode_to_geoid.tract_pid order by income_2013_2016.income desc limit 5"
    conn = db.connect()
    cursor = conn.cursor(buffered = True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def get_bottom_5_zip_by_income():
    sql = "SELECT zip_code FROM spatialforce.zipcode_to_geoid inner join spatialforce.income_2013_2016 on  income_2013_2016.tract_pid = zipcode_to_geoid.tract_pid order by income_2013_2016.income limit 5"
    conn = db.connect()
    cursor = conn.cursor(buffered = True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def get_top_5_zip_by_education():
    sql ="SELECT zip_code FROM spatialforce.zipcode_to_geoid inner join spatialforce.education_2017 on  education_2017.tract_pid = zipcode_to_geoid.tract_pid order by education_2017.pop_college_grad desc limit 5" 
    conn = db.connect()
    cursor = conn.cursor(buffered = True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def get_bottom_5_zip_by_education():
    sql ="SELECT zip_code FROM spatialforce.zipcode_to_geoid inner join spatialforce.education_2017 on  education_2017.tract_pid = zipcode_to_geoid.tract_pid order by education_2017.pop_college_grad limit 5"
    conn = db.connect()
    cursor = conn.cursor(buffered = True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def get_top_5_zip_by_population():
    sql ="SELECT zip_code FROM spatialforce.zipcode_to_geoid inner join spatialforce.race_2010 on race_2010.tract_pid = zipcode_to_geoid.tract_pid order by race_2010.total_pop desc limit 5"
    conn = db.connect()
    cursor = conn.cursor(buffered = True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def get_bottom_5_zip_by_population():
    sql ="SELECT zip_code FROM spatialforce.zipcode_to_geoid inner join spatialforce.race_2010 on race_2010.tract_pid = zipcode_to_geoid.tract_pid order by race_2010.total_pop limit 5"
    conn = db.connect()
    cursor = conn.cursor(buffered = True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

################################################

def zipcode_log():
    query = "SELECT Zipcode, COUNT(*) AS Log FROM spatialforce.zipcode_log GROUP BY Zipcode ORDER BY Log Desc"
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
