from flask import Flask
from flask_cors import CORS
import connections

app = Flask(__name__)
CORS(app)
counter = connections.counter()

@app.route("/")
def hello_world():
  return "<p>Hello, world!</p>"

@app.route("/number-submissions/update")
def update():
  counter.update_count()
  return "Updated count"

@app.route("/number-submissions")
def num_submissions():
  return {
    "count": counter.count
  }



@app.route("/submissions-time")
def time_submissions():
  return {
  "datasets": [
    {
      "id": "Submissions",
      "data": [
        { "x": "12:00", "y": 82 },
        { "x": "13:00", "y": 88 },
        { "x": "14:00", "y": 101 },
        { "x": "15:00", "y": 97 },
        { "x": "16:00", "y": 121 },
        { "x": "17:00", "y": 83 },
        { "x": "18:00", "y": 59 }
      ]
    }
  ]
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