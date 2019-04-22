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


@app.route("/users")
def users():
    return json.dumps({'success': 'success', 'results': query.get_data()})


if __name__ == "__main__":
    app.run()
