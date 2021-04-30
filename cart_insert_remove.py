import sqlite3

conn = sqlite3.connect('books.db')
c_cart = sqlite3.connect('cart.db')
c = conn.cursor()
c_ca = c_cart.cursor()


def bookAvailability(ISBN):  # checks availibility of Books
    # ISBN = input('ISBN ')
    if c.execute('''SELECT * FROM BOOK as B WHERE ? = B.ISBN''', (ISBN,)).fetchone():
        print("Found")
        return True
    else:
        print("Not found")
        return False
    conn.commit()


def addToCart(ISBN, quantity):  # have parameters isbn and cid

    # ISBN = input('ISBN ')
   # cID = input('cID ')


    availability = bookAvailability(ISBN)  # gets availability
    print(availability)

    if (availability == False):
        print("book not found.  \n")
        return

    for value in c.execute('''SELECT title FROM BOOK as B WHERE ? == B.ISBN ''', (ISBN,)):  # gets title for cart table
        title = value[0]
        break
    else:
        print("book not found")
    for row in c.execute('''SELECT price FROM BOOK as B WHERE ? == B.ISBN ''', (ISBN,)):  # gets price for cart table
        price = row[0]
        break
    else:
        print("book not found")

    c_ca.execute('''INSERT INTO CART VALUES(?,?,?,?)''', (ISBN, title, price, quantity))

    print("added to cart. ")

    c_cart.commit()


def removeFromCart():  # parameters isbn and cID

    ISBN = input('ISBN ')
    cID = input('cID ')

    c_ca.execute('''DELETE FROM CART as C WHERE ? = C.ISBN AND ? = C.cID ''', (ISBN, cID))
    c_cart.commit()


def priceInCart():  # cID parameter

    cID = input('cID ')

    for row in c_ca.execute('''SELECT C.price, C.title, C.ISBN FROM CART as C WHERE ? == C.cID ''',
                            (cID,)):  # gets price for cart table
        price = row[0]
        title = row[1]
        ISBN = row[2]
        break
    else:
        print("book not found")

    #  print(price)
    print("price is:", price, "$ for", title, "ISBN: ", ISBN)
    c_cart.commit()
