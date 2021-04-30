import sqlite3

conn = sqlite3.connect('admin.db')

c = conn.cursor()

c.execute('''CREATE  TABLE IF NOT EXISTS ADMIN ([User_ID] text PRIMARY KEY, [password] text, [firstname] text, [lastname] text)''')


conn.commit()