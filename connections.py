

from databases import database_objects
import psycopg2

class counter():
  def __init__(self, redis):
      self.database = database_objects
      self.redis = redis
      self.redis.set("count", 0)

  def update_count(self):
    count = 0
    for k, v in self.database.items():
      connection = psycopg2.connect(host=v, database=k, user='seta', password='defaultUnsafePassword')
      cursor = connection.cursor()
      cursor.execute("SELECT COUNT(id) FROM responses")
      count += sum(cursor.fetchone())
    self.redis.set("count", count)

  def get_count(self):
    return int(self.redis.get("count"))