import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS USERS (USERID INT, PASSWORD TEXT, FIRSTNAME TEXT, LASTNAME TEXT)''')


def usernameCheck(username):
    valid = True
    count = 0
    t = (username,)

    for i in cursor.execute('SELECT * FROM users WHERE username=?', t):
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
        'SELECT * FROM users WHERE username=? AND password=?', (username, password,))
    if(cursor.fetchone()):
        print()  # formatting
        print('You have successfully logged in!')
        print()  # formatting
        return username  # flag
    else:
        print('Incorrect username / password, please try again.')
        return 0  # flag


def insertUser(firstName, lastName, username, password):
    if(passwordCheck(password) and usernameCheck(username)):
        cursor.execute("INSERT INTO users VALUES (?,?,?,?)",
                       (firstName, lastName, username, password,))
        conn.commit()
        return 1

    else:
        return 0


def main():

    while (True):

        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        ch = int(input("Your Choice: "))

        if(ch == 1):
            f_name = input("Enter your first name: ")
            l_name = input("Enter your last name: ")
            username = input("Enter username: ")
            print("Remember: Having a strong password should be between 8-13 characters with some Upper Case, Digits, and special characters")
            password = input("\nEnter Password: ")

            r = insertUser(f_name, l_name, username, password)
            if(r == 1):
                loginUser(username, password)
            else:
                print("Username maybe taken or password is not strong")

        elif(ch == 2):
            username = input("Enter username: ")
            password = input("Enter Password: ")

            loginUser(username, password)

        elif(ch == 3):
            break

        else:
            print("Invalid Input")


main()
