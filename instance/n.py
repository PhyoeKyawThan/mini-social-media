import sqlite3

con = sqlite3.connect("database.db")
cur = con.cursor()

for data in cur.execute("SELECT * FROM post"):
	print(data)
