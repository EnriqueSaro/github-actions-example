import logging
from flask import Flask, json

app = Flask(__name__)

@app.route("/")
def hello():
    app.logger.info("root endopoint was reached")
    return "Hello World! MOdifieddd"

@app.route("/status")
def getStatus():
    app.logger.info("status endopoint was reached")
    resp = app.response_class(
        response=json.dumps({"result": "OK - healthy"}),
        status=200,
        mimetype='application/json'
    )
    return resp

@app.route("/metrics")
def getMetrics():
    app.logger.info("metrics endopoint was reached")
    data = json.dumps({
        "data": {
            "UserCount": 140,
            "UserCountActive": 23
        }
    })
    resp = app.response_class(
        response=data,
        status=200,
        mimetype='application/json'
    )
    return resp

if __name__ == "__main__":

    logging.basicConfig(filename='app.log', level='DEBUG')

    app.run(host='0.0.0.0')
