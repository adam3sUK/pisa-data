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

@app.route("/early-education-belonging")
def sense_belonging():
  return {
    "datasets": [
      {
        "id": "GBR",
        "data": [
          {
            "x": 6,
            "y": 1.1,
            "submissions": 412
          }
        ]
      },
      {
        "id": "FRA",
        "data": [
          {
            "x": 5,
            "y": 0.9,
            "submissions": 469
          }
        ]
      },
      {
        "id": "ESP",
        "data": [
          {
            "x": 6,
            "y": 0.4,
            "submissions": 500
          }
        ]
      }
    ]
  }

if __name__ == '__main__':
  app.run()