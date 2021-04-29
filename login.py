import search_book
import sqlite3


conn = sqlite3.connect('users.db')
cursor = conn.cursor()

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS USERS (USERID INT, PASSWORD TEXT, FIRSTNAME TEXT, LASTNAME TEXT)''')


def usernameCheck(username):
    valid = True
    count = 0
    t = (username,)

    for i in cursor.execute('SELECT * FROM USERS WHERE USERID=?', t):
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
    if(len(password) < 8):
        overallStatus = False
        return overallStatus
    if(len(password) > 13):
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
   # record = cursor.fetchall()

    if(cursor.fetchall()):
        for r in cursor:
            print(r)
        print()  # formatting
        print('You have successfully logged in!')
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
        print("                                      3. Check out                                                   ")
        print()
        print("                                      4. Order details                                               ")
        print()
        print("                                      5. View/edit shopping cart                                     ")
        print()
        print("                                      6. Edit personal info                                          ")
        print()
        print("                                      7. Logout                                                      ")
        print()

        customer_choice = int(input("Enter your choice: "))

        if (customer_choice == 1):
            print("1. Children")
            print("2. Sports")
            print("3. Novel")
            print("4. Fiction")
            print("5. Non-Fiction")

            book_sub = int(input("Enter your choice: "))
            # search books by sub/category from database and print here
            # then ask whether they want to add to cart or not
        elif(customer_choice == 2):
            print("1. by author")
            print("2. by ISBN")
            print("3. by title")

            search_choice = int(input("Enter your choice: "))
            if(search_choice == 1):
                by_author = input("Enter author name: ")
                search_book.searchBook_Byauthor(by_author)

            elif (search_choice == 2):
                by_ISBN = int(input("Enter ISBN: "))

            elif(search_choice == 3):
                by_title = input("Enter title of the book: ")


        return username
    else:
        print('Incorrect username / password, please try again.')
        return 0  # flag


def insertUser(username, password, firstname, lastname):
    if(passwordCheck(password) and usernameCheck(username)):
        cursor.execute("INSERT INTO USERS VALUES (?,?,?,?)",
                       (username, password, firstname, lastname))
        conn.commit()
        return 1

    else:
        return 0
