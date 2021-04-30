import sqlite3

conn = sqlite3.connect('books.db')

c = conn.cursor()


def add_book():

    isbn = input('ISBN:')
    author = input('Author:')
    year = input('Year Published:')
    title = input('Title:')
    price = input('Price:')
    sub = input("Subject: ")
    c.execute('''INSERT INTO BOOK (ISBN, author, year, title, price, sub) VALUES(?,?,?,?,?,?)''', (isbn, author, year, title, price, sub))
    conn.commit()


def remove_book():
    ISBN = input('ISBN of book to remove: ')
    c.execute('''DELETE FROM BOOK as B WHERE ? = B.ISBN ''', (ISBN,))
    conn.commit ()