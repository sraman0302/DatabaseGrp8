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
