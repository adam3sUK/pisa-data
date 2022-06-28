import psycopg2

connection = psycopg2.connect(host='seta-gbr.cvcpj1fhj3k9.us-east-2.rds.amazonaws.com', database='gbr', user='seta', password='defaultUnsafePassword')

cursor = connection.cursor()
cursor.execute("SELECT COUNT(id) FROM public.responses")

records = cursor.fetchone()

count = records[0]