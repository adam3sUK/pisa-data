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
      self.redis.set("count", tasks.update_count.delay(self.database))
    except Exception as e:
      print(e)

  def get_count(self):
    return int(self.redis.get("count"))