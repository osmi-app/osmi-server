from flask import Flask, render_template, request, redirect, url_for
from flask.ext.cors import CORS, cross_origin
from random import randint

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/", methods=["POST"])
@cross_origin()
def update():
    if len(request.data.split("SEP")[0].split(",")) == 6:
        return "END"
    else:
        return str(randint(1,16)) + ',' + str(len(request.data.split("[SEP]")[0].split(",")) * 20)

@app.route("/", methods=["PUT"])
def send():
    # send records for archiving
    return "FEED ME, SEYMOUR!!!"

@app.route("/", methods=["GET"])
def do():
    return "have a good day!"

@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return "Page/File not found", 404


if __name__ == '__main__':
    app.run(debug=True)
