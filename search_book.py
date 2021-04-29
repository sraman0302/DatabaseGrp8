import sqlite3

conn = sqlite3.connect('bookstore.db')

cursor = conn.cursor()


#need function to search by subject/category also need to add column in the BOOK datase for category

def searchBook_Byauthor(author):
    cursor.execute(
        """SELECT * FROM BOOK WHERE author=?""", (author,))
    if (cursor.fetchall()):
        for r in cursor:
            print(r)