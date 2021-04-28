import sqlite3

conn = sqlite3.connect('bookstore.db')

c = conn.cursor()


def add_book():

    isbn = input('ISBN:')
    author = input('Author:')
    year = input('Year Published:')
    title = input('Title:')
    price = input('Price:')
    c.execute(''' INSERT INTO BOOK (ISBN, author, year , title , price)
    VALUES (?,?,?,?,?) ''', (isbn, author, year, title, price))
#conn.commit ()


def remove_book():
    ISBN = input('ISBN of book to remove: ')
    c.execute('''DELETE FROM BOOK as B WHERE ? = B.ISBN ''', (ISBN,))


conn.commit()


def main():
    while(True):
        print("1. ADD BOOK")
        print("2. REMOVE BOOK")
        print("3. PRINT BOOKS")
        print("4. EXIT")

        choice = int(input("your choice: "))

        if(choice == 1):
            add_book()
        elif(choice == 2):
            remove_book()

        elif(choice == 3):
            c.execute(''' SELECT * FROM BOOK''')
            print(c.fetchall())
        elif(choice == 4):
            break

        else:
            print("invalid input")


main()
