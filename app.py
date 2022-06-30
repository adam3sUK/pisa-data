from flask import Flask
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)

connection = psycopg2.connect(host='pisa2018.cvruukypsgyb.eu-west-2.rds.amazonaws.com', database='postgres', user='postgres', password='dQ4hVXnipUJSMw8')
cursor = connection.cursor()
cursor.execute("SELECT count FROM total_submissions WHERE id = 1")
count = sum(cursor.fetchone())

@app.route("/")
def hello_world():
  return f"<p>Hello, world!</p>"

@app.route("/number-submissions")
def num_submissions():
  return {
    "count": count
  }



# @app.route("/submissions-time")
# def time_submissions():
#   return {
#   "datasets": [
#     {
#       "id": "Submissions",
#       "data": [
#         { "x": "12:00", "y": 82 },
#         { "x": "13:00", "y": 88 },
#         { "x": "14:00", "y": 101 },
#         { "x": "15:00", "y": 97 },
#         { "x": "16:00", "y": 121 },
#         { "x": "17:00", "y": 83 },
#         { "x": "18:00", "y": 59 }
#       ]
#     }
#   ]
# }

# @app.route("/early-education-belonging")
# def sense_belonging():
#   return {
#     "datasets": [
#       {
#         "id": "GBR",
#         "data": [
#           {
#             "x": 6,
#             "y": 1.1,
#             "submissions": 412
#           }
#         ]
#       },
#       {
#         "id": "FRA",
#         "data": [
#           {
#             "x": 5,
#             "y": 0.9,
#             "submissions": 469
#           }
#         ]
#       },
#       {
#         "id": "ESP",
#         "data": [
#           {
#             "x": 6,
#             "y": 0.4,
#             "submissions": 500
#           }
#         ]
#       }
#     ]
#   }

if __name__ == '__main__':
  app.run()