from databases import database_objects
import tasks

class counter():
  def __init__(self, redis):
      self.database = database_objects
      self.redis = redis
      self.redis.set("count", 0)
      self.update_count()

  def update_count(self):
    try:
      tasks.update_count.delay(self.redis, self.database)
    except:
      print("An error has occured in running the Celery task")

  def get_count(self):
    return int(self.redis.get("count"))