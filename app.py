from flask import Flask
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)

connection = psycopg2.connect(host='pisa2018.cvruukypsgyb.eu-west-2.rds.amazonaws.com', database='postgres', user='postgres', password='dQ4hVXnipUJSMw8')
cursor = connection.cursor()
cursor.execute("SELECT count FROM total_submissions WHERE id = 1")
count = sum(cursor.fetchone())
cursor.close()
connection.close()

@app.route("/")
def hello_world():
  return f"<p>Hello, world!</p>"

@app.route("/number-submissions")
def num_submissions():
  return {
    "count": count
  }

if __name__ == '__main__':
  app.run()