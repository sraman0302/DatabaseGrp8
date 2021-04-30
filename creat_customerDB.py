import sqlite3

conn = sqlite3.connect('client.db')

c = conn.cursor()

c.execute('''CREATE  TABLE IF NOT EXISTS CLIENT ([cID] text PRIMARY KEY, [firstname] text, [lastname] text, [address] text, [city] text, [state] text, [zip] integer, [phoneNumber] integer, [email] text)''' )

conn.commit()