from distutils.log import debug
from flask import Flask

app = Flask(__name__) # for 2 underscores, python calls this dunderscore

@app.route("/")
def hello():
  return "hello world"

app.run(debug=True)