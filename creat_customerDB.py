import sqlite3

conn = sqlite3.connect('client.db')

c = conn.cursor()

c.execute('''CREATE  TABLE IF NOT EXISTS CLIENT ([cID] text PRIMARY KEY, [firstname] text, [lastname] text, [address] text, [city] text, [state] text, [zip] integer, [phoneNumber] integer, [email] text)''' )

c.execute('''CREATE TABLE If NOT EXISTS SHIPPING ([cID] text PRIMARY KEY, [firstname] text, [lastname] text, [address] text, [city] text, [state] text, [zip] integer, [phoneNumber] integer, [email] text, [Credit Card] integer, [exp date] text, [CVV] text, [billing address] text, [billing city] text, [billing state] text, [billing zip] text)''')
conn.commit()