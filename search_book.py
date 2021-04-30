import sqlite3

conn = sqlite3.connect('books.db')

cursor = conn.cursor()


# need function to search by subject/category also need to add column in the BOOK datase for category

def searchBook_Byauthor(author):
    cursor.execute(
        """SELECT * FROM BOOK WHERE author=?""", (author,))
    record = cursor.fetchall()
    if(record):
        for r in record:
            print(r)
    else:
        print("No matched found")


def searchBook_ByISBN(ISBN):
    cursor.execute(
        """SELECT * FROM BOOK WHERE ISBN=?""", (ISBN,))
    record = cursor.fetchall()
    if (record):
        for r in record:
            print(r)
    else:
        print("No matched found")


def searchBook_Bytitle(title):
    cursor.execute(
        """SELECT * FROM BOOK WHERE title=?""", (title,))
    record = cursor.fetchall()
    if (record):
        for r in record:
            print(r)
    else:
        print("No matched found")

def searchBook_Bysubject(sub):
    cursor.execute(
        """SELECT * FROM BOOK WHERE sub=?""", (sub,))
    record = cursor.fetchall()
    if (record):
        for r in record:
            print(r)
    else:
        print("No matched found")