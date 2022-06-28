import psycopg2

databases = {
  "fra":"seta-fra.cvcpj1fhj3k9.us-east-2.rds.amazonaws.com",
  "gbr":"seta-gbr.cvcpj1fhj3k9.us-east-2.rds.amazonaws.com",
  "ita":"seta-ita.cvcpj1fhj3k9.us-east-2.rds.amazonaws.com"
}


count = 0

for k, v in databases.items():
  connection = psycopg2.connect(host=v, database=k, user='seta', password='defaultUnsafePassword')
  cursor = connection.cursor()
  cursor.execute("SELECT COUNT(id) FROM responses")
  count += sum(cursor.fetchone())

print(count)