import search_book
import sqlite3
import cart_insert_remove

conn = sqlite3.connect('user.db')
c_cart = sqlite3.connect('cart.db')
c_client = sqlite3.connect('client.db')
c_book = sqlite3.connect('books.db')
cursor = conn.cursor()
c_ca = c_cart.cursor()
c_cl = c_client.cursor()
book = c_book.cursor()

def usernameCheck(username):
    valid = True
    count = 0
    t = (username,)

    for i in c_cl.execute('SELECT * FROM CLIENT WHERE CID=?', t):
        count = count + 1

    if count == 0:
        valid = True
    else:
        valid = False
        print("Sorry, your username has already been taken. Please Try Again.")

    return valid


def passwordCheck(password):
    # Password Requirements
    overallStatus = False
    hasCapitalLetter = False
    hasSpecialCharacter = False
    hasOneDigit = False
    # If Password Lengths are Wrong
    if (len(password) < 8):
        overallStatus = False
        return overallStatus
    if (len(password) > 13):
        overallStatus = False
        return overallStatus
    # Loop through each character of the string to see if it passes all test cases
    for char in password:
        if char.isupper():  # Checking for Capital
            hasCapitalLetter = True
        if char.isalnum() == False:  # Checking for Special Character
            hasSpecialCharacter = True
        if char.isdigit():  # Checking for Digits
            hasOneDigit = True

    if hasCapitalLetter == True and hasSpecialCharacter == True and hasOneDigit == True:
        overallStatus = True

    return overallStatus


def loginUser(username, password):
    cursor.execute(
        """SELECT * FROM USERS WHERE USERID=? AND PASSWORD=?""", (username, password,))
    record = cursor.fetchall()

    if(record):
        print('You have successfully logged in!')
    else:
        print("print('Incorrect username / password, please try again.")
        return 0
    while (record):
        print()  # formatting

        print()  # formatting
        print("*****************************************************************************************************")
        print("**--------                                                                                 --------**")
        print("**---                            Welcome to Online Book-Store                                   ---**")
        print("**--------                              Customer Menu                                      --------**")
        print("*****************************************************************************************************")
        print()
        print("                                      1. Search Book by subject/category                             ")
        print()
        print("                                      2. Search Book by ISBN/ title/ author                          ")
        print()
        print("                                      3. View/edit shopping cart                                     ")
        print()
        print("                                      4. Edit personal info                                          ")
        print()
        print("                                      5. Logout                                                      ")
        print()

        customer_choice = int(input("Enter your choice: "))

        while (customer_choice == 1):
            print("1. Children")
            print("2. Sports")
            print("3. Novel")
            print("4. Fiction")
            print("5. Non-Fiction")
            print("6. Return to main menu")

            book_sub = int(input("Enter your choice: "))
            if(book_sub == 1):
                search_book.searchBook_Bysubject("children")
            elif(book_sub == 2):
                search_book.searchBook_Bysubject("sports")
            elif(book_sub == 3):
                search_book.searchBook_Bysubject("novel")
            elif(book_sub == 4):
                search_book.searchBook_Bysubject("fiction")
            elif(book_sub == 5):
                search_book.searchBook_Bysubject("non-fiction")
            elif(book_sub == 6):
                break
            add_cart = input("Enter ISBN to add the item into your shopping cart or "
                             "Press enter to go back to customer menu or "
                             "To brows more enter 'b' : ")
            if (add_cart.isnumeric()):
                quantity = int(input("Enter quantity: "))
                cart_insert_remove.addToCart(add_cart, quantity)
            elif (add_cart == 'b'):
                continue
            if(add_cart == ""):
                break

            # search books by sub/category from database and print here
            # then ask whether they want to add to cart or not
        while (customer_choice == 2):
            print("1. by author")
            print("2. by ISBN")
            print("3. by title")
            print("4. Return to main menu")

            search_choice = int(input("Enter your choice: "))
            while (search_choice == 1):
                by_author = input("Enter author name: ")
                search_book.searchBook_Byauthor(by_author)

                add_cart = input("Enter ISBN to add the item into your shopping cart or "
                                 "Press enter to go back to search menu or "
                                 "To brows more enter 'b' : ")
                if (add_cart.isnumeric()):
                    quantity = int(input("Enter quantity: "))
                    cart_insert_remove.addToCart(add_cart, quantity)
                elif (add_cart == 'b'):
                    continue
                if (add_cart == ""):
                    break

            while (search_choice == 2):
                by_ISBN = int(input("Enter ISBN: "))
                search_book.searchBook_ByISBN(by_ISBN)
                add_cart = input("Enter ISBN to add the item into your shopping cart or "
                                 "Press enter to go back to search menu or "
                                 "To brows more enter 'b' : ")
                if (add_cart.isnumeric()):
                    quantity = int(input("Enter quantity: "))
                    cart_insert_remove.addToCart(add_cart, quantity)
                elif (add_cart == 'b'):
                    continue
                if (add_cart == ""):
                    break
            while (search_choice == 3):
                by_title = input("Enter title of the book: ")
                search_book.searchBook_Bytitle(by_title)
                add_cart = input("Enter ISBN to add the item into your shopping cart or "
                                 "Press enter to go back to search menu or "
                                 "To brows more enter 'b' : ")
                if (add_cart.isnumeric()):
                    quantity = int(input("Enter quantity: "))
                    cart_insert_remove.addToCart(add_cart, quantity)
                elif (add_cart == 'b'):
                    continue
                if (add_cart == ""):
                    break
            if(search_choice == 4):
                break

        while (customer_choice == 3): #view/edit shopping cart
            print("Current Cart status")
            c_cart.execute(''' SELECT * FROM CART ''')
            r = c_ca.fetchall()
            if (r):
                for i in r:
                    print(i)
            else:
                break


        if (customer_choice == 5): #logout
            print("You have been successfully logged out")
            break
        #return username
    #else:
     #   print('Incorrect username / password, please try again.')
      #  return 0  # flag


def insertUser(username, password, firstname, lastname):
    if (passwordCheck(password) and usernameCheck(username)):
        cursor.execute("INSERT INTO USERS VALUES (?,?,?,?)", (username, password, firstname, lastname))
        conn.commit()
        return 1

    else:
        return 0


def insertUserDetail(cid, firstname, lastname, address, city, state, zip, phone, email):
    if (usernameCheck(cid)):
        c_cl.execute("INSERT INTO CLIENT VALUES (?,?,?,?,?,?,?,?,?)",
                       (cid, firstname, lastname, address, city, state, zip, phone, email))
        c_client.commit()
        return 1
    else:
        return 0
