import psycopg2
import numpy as np

def column_stats(tName, attribute):
  conn = psycopg2.connect(dbname='db', user='grok')
  cursor = conn.cursor()
  cursor.execute('SELECT '+ attribute + ' FROM '+tName)
  records = cursor.fetchall()
  mean = np.mean(np.array(records))
  median = np.median(np.array(records))
  return (mean, median)

if __name__ == '__main__':
  a = column_stats('Star','t_eff')
  print (a)
