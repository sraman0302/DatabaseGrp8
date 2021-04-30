import sqlite3

conn = sqlite3.connect('cart.db')

c = conn.cursor()

c.execute('''CREATE  TABLE IF NOT EXISTS CART ([ISBN] text, [title] text, [price] integer, [quantity] integer, PRIMARY KEY(ISBN))''' )

conn.commit()