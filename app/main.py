import json
from flask import Flask, render_template, json, request, Response, jsonify, flash
import queries as query
from flask_mysqldb import MySQL
import database as db


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

@app.route('/update',methods=['GET'])
def update_form():
    return render_template('update.html')

@app.route('/search',methods=['GET'])
def search():
    return render_template('search.html')

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
