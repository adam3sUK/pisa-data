import celery
import os
import psycopg2

app = celery.Celery('tasks')

# @app.task
# def add(x, y):
#   r.set("result", int(x + y))

# @app.task
# def increment():
#   r.set("count", int(r.get("count")) + 1)

@app.task
def update_count(db_dict):
  count = 0
  for country_code, url in db_dict.items():
    connection = psycopg2.connect(host=url, database=country_code, user='seta', password='defaultUnsafePassword')
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(id) FROM responses")
    count = sum(cursor.fetchone())
  return count

app.conf.update(BROKER_URL=os.environ['REDIS_URL'],
                CELERY_RESULT_BACKEND=os.environ['REDIS_URL'])