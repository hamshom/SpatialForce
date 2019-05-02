import json
from flask import Flask, render_template
import queries as query

app = Flask(__name__)


app.config.update(dict(
    DATABASE='spatialforce',
    USERNAME='spatialforce',
    HOST='127.0.0.1',
    PASSWORD='09j5fgt'
))


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

@app.route('/trend',methods=['GET'])
def trend():
    return render_template('trend.html')

@app.route("/users")
def users():
    return json.dumps({'success': 'success', 'results': query.get_data()})


if __name__ == "__main__":
    app.run()
