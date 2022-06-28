from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
  return "<p>Hello, world!</p>"

@app.route("/number-submissions")
def num_submissions():
  return {
    "count": 134000
  }

if __name__ == '__main__':
  app.run()