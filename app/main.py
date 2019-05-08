import json
from flask import Flask, render_template, json, request, Response, jsonify, flash
import queries as query
from flask_mysqldb import MySQL
import database as db
from random import randint

app = Flask(__name__)


app.config.update(dict(
    DATABASE='spatialforce',
    USERNAME='spatialforce',
    HOST='127.0.0.1',
    PASSWORD='09j5fgt'
))

mysql = MySQL(app)


@app.route("/")
def index():
    # return app.send_static_file("index.html")
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search_default():
    houseValue = ""
    incomeValue = ""
    populationValue = ""
    educationValue = ""
    return render_template('search.html', houseValue=houseValue, incomeValue=incomeValue, populationValue=populationValue, educationValue=educationValue)


def post_json_endpoint(zipcode):

    try:
        conn = db.connect()
        cursor = conn.cursor(buffered=True)
        cursor.execute('''SELECT MAX(id) FROM spatialforce.zipcode_log''')
        maxid = cursor.fetchone()
        cursor.execute('''INSERT INTO spatialforce.zipcode_log (id, Zipcode) VALUES (%s, %s)''', (maxid[0] + 1, zipcode))

        conn.commit()
        cursor.close()
        print("add zipcode to trend table successfully with code:" + zipcode)
        return 'success'

    except Exception as e:
        print(e)

    return 'fail'



@app.route('/search', methods=['POST'])
def search():

    zipCode = str(request.form['zipCode'])

    if(zipCode == ""):
        return jsonify({'error' : 'Missing data!'})

    # Updates zipcode logger
    post_json_endpoint(zipCode)

    housingpriceResult = query.get_avg_housingprice_by_zip(zipCode)
    totalPopulation    = query.get_population_byzip(zipCode)
    totalEduction      = query.get_number_college_grad_byzip(zipCode)
    AverageIncome      = query.get_avg_income_byzip(zipCode)

    variableList = [totalPopulation, housingpriceResult,totalEduction, AverageIncome ]

    if any(elem[0][0] is None for elem in variableList):
        # data = {
        #     "houseValue": "N/A",
        #     "incomeValue": "N/A",
        #     "populationValue": "N/A",
        #     "educationValue": "N/A"
        # }
        # return jsonify(data)
        return jsonify({'error' : 'Missing data!'})

    else:
        data = {
            "houseValue": int(housingpriceResult[0][0]),
            "incomeValue": int(AverageIncome[0][0]),
            "populationValue": int(totalPopulation[0][0]),
            "educationValue": int(totalEduction[0][0])
        }
        return jsonify(data)


@app.route('/rank', methods=['GET'])
def rank_default():
    data = {
        "top": [],
        "bottom": []
      }
    return render_template('rank.html', data=data)

@app.route('/rank', methods=['POST'])
def rank():
    # return render_template('rank.html')
    click_type = request.form['type']
    print(click_type)
    data = query.rank_query(click_type)

    queryValid = 1
    if queryValid:
        return jsonify(data)

    return jsonify({'error' : 'Missing data!'})

@app.route('/trend', methods=['GET'])
def trend():
    trendTableData = query.zipcode_log()
    return render_template('trend.html', data=trendTableData)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route("/users")
def users():
    return jsonify(query.get_data())


@app.route("/api/zipcode_log")
def zipcodeLog():
    return jsonify(query.zipcode_log())











if __name__ == "__main__":
    app.run()
