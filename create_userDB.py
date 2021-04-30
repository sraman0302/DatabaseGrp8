import sqlite3

conn = sqlite3.connect('user.db')

c = conn.cursor()

c.execute('''CREATE TABLE USER (USERID INT, PASSWORD TEXT, FIRSTNAME TEXT, LASTNAME TEXT)''')

conn.commit()