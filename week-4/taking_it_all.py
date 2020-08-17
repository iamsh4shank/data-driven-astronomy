import psycopg2

def select_all(tName):
  conn = psycopg2.connect(dbname='db', user='grok')
  cursor = conn.cursor()
  cursor.execute('SELECT * FROM '+tName)
  records = cursor.fetchall()
  return records

if __name__ == '__main__':
  a = select_all('Star')
  print (a)
  b = select_all('Planet')
  print (a)
