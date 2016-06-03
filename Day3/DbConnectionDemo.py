import MySQLdb

conn = MySQLdb.connect('localhost','root','katieholmes123','python')

conn.autocommit(True)

query = "Select version()"

cur = conn.cursor()

cur.execute(query)

print cur.description[0][0]
print '-' * 22
print cur.fetchone()[0]
cur.close()