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
      for country_code, url in self.database:
        result = tasks.update_count.delay(country_code, url)
        while result.status == 'PENDING':
          print("Pending")
        new_count = result.get()
        print(new_count)
        # self.redis.incrby("count", new_count)
    except Exception as e:
      print(f"EXCEPTION!!!!! {e}")

  def get_count(self):
    return int(self.redis.get("count"))