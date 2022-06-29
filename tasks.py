import celery
import os
app = celery.Celery('example')

@app.task
def add(redis, x, y):
  redis.set("result", int(x + y))

@app.task
def increment(redis):
  redis.set("count", int(redis.get("count")))

app.conf.update(BROKER_URL=os.environ['REDIS_URL'],
                CELERY_RESULT_BACKEND=os.environ['REDIS_URL'])