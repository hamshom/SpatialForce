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

@app.route('/rank',methods=['GET'])
def update_form():
    return render_template('rank.html')

@app.route('/search', methods=['GET'])
def search_default():
    houseValue = ""
    incomeValue = ""
    populationValue = ""
    educationValue = ""
    return render_template('search.html', houseValue=houseValue, incomeValue=incomeValue, populationValue=populationValue, educationValue=educationValue)

@app.route('/search', methods=['POST'])
def search():
    zipCode = '33'

    queryResult = query.get_users(zipCode)

    print(queryResult)

    if(zipCode == ""):
        return jsonify({'error' : 'Missing data!'})

    if(int(zipCode) == 99999):
        data = {
            "houseValue": 1,
            "incomeValue": 2,
            "populationValue": 3,
            "educationValue":4
        }
    else:
        data = {
            "houseValue": queryResult[0][0],
            "incomeValue": queryResult[0][1],
            "populationValue": queryResult[0][2],
            "educationValue": queryResult[0][3]
        }

    if zipCode.isdigit():
        return jsonify(data)

    return jsonify({'error' : 'Missing data!'})


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact',methods=['GET'])
def contact():
    return render_template('contact.html')

@app.route("/users")
def users():
    return jsonify(query.get_data())


@app.route("/api/zipcode_log")
def zipcodeLog():
    return jsonify(query.zipcode_log())


@app.route("/api/zipcode/<string:zipcode>", methods=['POST'])
def post_json_endpoint(zipcode):

    try:
        if request.method == "POST":
            if request.headers['Content-Type'] == 'application/json':
                # arguments = request.get_json()
                # zipcode = arguments.get("zipcode")

                conn = db.connect()
                cursor = conn.cursor(buffered=True)
                cursor.execute('''SELECT MAX(id) FROM spatialforce.zipcodeLog''')
                maxid = cursor.fetchone()
                cursor.execute('''INSERT INTO spatialforce.zipcodeLog (id, Zipcode) VALUES (%s, %s)''', (maxid[0] + 1, zipcode))

                conn.commit()
                cursor.close()

                data = {
                    "result": zipcode,
                    "request-content-type": "application/json"
                }
                resp = Response(json.dumps(data), mimetype='application/json')

                return resp

    except Exception as e:
        print(e)

    return 'fail'









if __name__ == "__main__":
    app.run()
