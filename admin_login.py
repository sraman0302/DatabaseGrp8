import sqlite3


import add_remove_books

conn = sqlite3.connect('admin.db')
c_client = sqlite3.connect('client.db')
cursor = conn.cursor()
c_cl = c_client.cursor()


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


def loginAdmin(username, password):
    cursor.execute(
        """SELECT * FROM ADMIN WHERE USER_ID=? AND PASSWORD=?""", (username, password,))
    record = cursor.fetchall()

    if (record):
        print('You have successfully logged in!')
    else:
        print("print('Incorrect username / password, please try again.")
        return 0

    while (record):
        print("*****************************************************************************************************")
        print("**--------                                                                                 --------**")
        print("**---                            Welcome to Online Book-Store                                   ---**")
        print("**--------                              Admin Menu                                         --------**")
        print("*****************************************************************************************************")
        print()
        print("                                      1. Add Book                                                    ")
        print()
        print("                                      2. Remove Book                                                 ")
        print()
        print("                                      3. Logout                                                      ")
        print()

        admin_choice = int(input("Enter your choice: "))
        while (admin_choice == 1):
            add_remove_books.add_book()
            out = input("Would you like to add more Books? (y/n): ")
            if(out == "y"):
                continue
            else:
                break
        while (admin_choice == 2):
            add_remove_books.remove_book()
            out = input("Would you like to Remove more Books? (y/n): ")
            if (out == "y"):
                continue
            else:
                break
        if (admin_choice == 3):
            print("You have been successfully logged out")
            break
    #else:
     #   print('Incorrect username / password, please try again.')
      #  return 0

def insertAdmin(username, password, firstname, lastname):
    if (passwordCheck(password) and usernameCheck(username)):
        cursor.execute("INSERT INTO ADMIN VALUES (?,?,?,?)", (username, password, firstname, lastname))
        conn.commit()
        return 1

    else:
        return 0

cursor.execute("INSERT INTO ADMIN VALUES (?,?,?,?)", ("vpatel16", "Vivek@1234", "Vivek", "Patel"))