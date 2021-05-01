import sqlite3

conn = sqlite3.connect('books.db')
c_cart = sqlite3.connect('cart.db')
c_client = sqlite3.connect('client.db')
c = conn.cursor()
c_ca = c_cart.cursor()
c_cl = c_client.cursor()


def bookAvailability(ISBN):  # checks availibility of Books

    if c.execute('''SELECT * FROM BOOK as B WHERE ? = B.ISBN''', (ISBN,)).fetchone():
        return True
    else:
        print("Not found")
        return False
    conn.commit()


def addToCart(ISBN, quantity):  # have parameters isbn and cid

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


def removeFromCart(ISBN):  # parameters isbn and cID
    c_ca.execute('''DELETE FROM CART as C WHERE ? = C.ISBN ''', (ISBN,))
    c_cart.commit()

def removeCart():  # parameters isbn and cID
    c_ca.execute('''DELETE FROM CART as C ''')
    c_cart.commit()

def printCart():
    c_ca.execute("SELECT c.ISBN, c.title, c.quantity, c.price FROM CART AS c")
    pr = c_ca.fetchall()
    sum = 0
    print("---------------------------------------------------------------------------------------------")
    print('{:<25} {:<50} {:<10} {:<8}'.format('ISBN', 'Title', 'Qt', 'Price'))
    print("---------------------------------------------------------------------------------------------")
    for i in pr:
        QP = i[2] * i[3]
        print('{:<25} {:<50} {:<10} {:<8}'.format(i[0], i[1], i[2], QP))
        sum += QP
    print("---------------------------------------------------------------------------------------------")
    print("---------------------------------------------------------------------------------------------")
    print("                                                                       Total:          $", sum)
    print("---------------------------------------------------------------------------------------------")
    c_cart.commit()


def checkOut(username):
    print("Shipping Details: ")
    new_ship = input("Would you like enter new shipping address? y/n: ")

    if (new_ship == "n"):
        for r in c_cl.execute(
                '''SELECT c.cid, c.firstname, c.lastname, c.address, c.city, c.state, c.zip, c.phoneNumber, c.email FROM CLIENT AS c WHERE CID=?''',
                (username,)):
            # cl_details = c_cl.fetchall()
            cid = r[0]
            f_name = r[1]
            l_name = r[2]
            Ship_add = r[3]
            city = r[4]
            state = r[5]
            zip = r[6]
            phone = r[7]
            e_mail = r[8]
            break
    elif (new_ship == "y"):
        for r in c_cl.execute(
                '''SELECT c.cid FROM CLIENT AS c WHERE CID=?''', (username,)):
            new_cid = r[0]
            break
        new_firstname = input("Enter firstname: ")
        new_lastname = input("Enter lastname: ")
        new_add = input("Enter street: ")
        new_city = input("City: ")
        new_state = input("State: ")
        new_zip = input("zip: ")
        new_phone = input("Enter phone: ")
        new_email = input("Enter email: ")
    print()
    print("Payment Details:")
    pay_firstname = input("Enter first name on the card: ")
    pay_lastname = input("Enter last name on the card: ")
    CC_num = int(input("Enter 16 digit credit card number: "))
    exp_date = input("Enter expiration date (mm/yy): ")
    CVV_num = int(input("Enter 3 CVV number: "))
    bill_add = input("Enter billing address: ")
    bill_city = input("City: ")
    bill_state = input("State: ")
    bill_zip = input("zip: ")
    save_details = input("Would you like to save your payment information for future shopping? y/n: ")

    if (save_details == "y" and new_ship == "n"):
        c_cl.execute("INSERT INTO SHIPPING VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                     (cid, f_name, l_name, Ship_add, city, state, zip, phone, e_mail,
                      CC_num, exp_date, CVV_num, bill_add, bill_city, bill_state, bill_zip))
        print()
        print("                                     Invoice for Customer: ", cid)
        print("-------------------------------------------------------------------------------------------------------")
        print("                                         Shipping Address:")
        print("                                         Name: ", f_name, l_name)
        print("                                      Address: ", Ship_add)
        print("                                               ", city)
        print("                                               ", state, zip)
        print("-------------------------------------------------------------------------------------------------------")
        print("                                         Payment Address: ")
        print("                                         Name: ", pay_firstname, pay_lastname)
        print("                                      Address: ", bill_add)
        print("                                               ", bill_city)
        print("                                               ", bill_state, bill_zip)
        print("-------------------------------------------------------------------------------------------------------")
        printCart()

    elif (save_details == "y" and new_ship == "y"):
        c_cl.execute("INSERT INTO SHIPPING VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                     (new_cid, new_firstname, new_lastname, new_add, new_city, new_state, new_zip, new_phone, new_email,
                      CC_num, exp_date, CVV_num, bill_add, bill_city, bill_state, bill_zip))
        print()
        print("                                     Invoice for Customer: ", new_cid)
        print("-------------------------------------------------------------------------------------------------------")
        print("                                         Shipping Address:")
        print("                                         Name: ", new_firstname, new_lastname)
        print("                                      Address: ", new_add)
        print("                                               ", new_city)
        print("                                               ", new_state, new_zip)
        print("-------------------------------------------------------------------------------------------------------")
        print("                                         Payment Address: ")
        print("                                         Name: ", pay_firstname, pay_lastname)
        print("                                      Address: ", bill_add)
        print("                                               ", bill_city)
        print("                                               ", bill_state, bill_zip)
        print("-------------------------------------------------------------------------------------------------------")
        printCart()

    elif (save_details == "n" and new_ship == "n"):
        print()
        print("                                     Invoice for Customer: ", cid)
        print("-------------------------------------------------------------------------------------------------------")
        print("                                         Shipping Address:")
        print("                                         Name: ", f_name, l_name)
        print("                                      Address: ", Ship_add)
        print("                                               ", city)
        print("                                               ", state, zip)
        print("-------------------------------------------------------------------------------------------------------")
        print("                                         Payment Address: ")
        print("                                         Name: ", pay_firstname, pay_lastname)
        print("                                      Address: ", bill_add)
        print("                                               ", bill_city)
        print("                                               ", bill_state, bill_zip)
        print("-------------------------------------------------------------------------------------------------------")
        printCart()

    elif (save_details == "n" and new_ship == "y"):
        print()
        print("                                     Invoice for Customer: ", new_cid)
        print("-------------------------------------------------------------------------------------------------------")
        print("                                         Shipping Address:")
        print("                                         Name: ", new_firstname, new_lastname)
        print("                                      Address: ", new_add)
        print("                                               ", new_city)
        print("                                               ", new_state, new_zip)
        print("-------------------------------------------------------------------------------------------------------")
        print("                                         Payment Address: ")
        print("                                         Name: ", pay_firstname, pay_lastname)
        print("                                      Address: ", bill_add)
        print("                                               ", bill_city)
        print("                                               ", bill_state, bill_zip)
        print("-------------------------------------------------------------------------------------------------------")
        printCart()
    #    return 0
    c_cart.commit()
