import login
import admin_login
import sqlite3

from sympy import true

#conn = sqlite3.connect('mypersonal.db')

#c = conn.cursor()


def main():

    print("*****************************************************************************************************")
    print("**--------                                                                                 --------**")
    print("**---                            Welcome to Online Book-Store                                   ---**")
    print("**--------                                                                                 --------**")
    print("*****************************************************************************************************")
    print()
    print("                                      1. Customer Login                                              ")
    print()
    print("                                      2. Admin Login                                                 ")
    print()
    print("                                      3. New member sign in                                          ")
    print()
    print("                                      4. Quite                                                       ")
    print()

    ch = int(input("Enter your choice: "))
    #while true:

    if (ch == 1):  # customer login
        username = input("Enter username: ")
        password = input("Enter Password: ")
        l = login.loginUser(username, password)
       # if (l == 0):
        #    break
        #else:
         #   print("Wrong username / password")



    elif (ch == 2):  # admin login

        username = input("Enter username: ")
        password = input("Enter Password: ")
        l = admin_login.loginAdmin(username, password)
        #if (l == 0):
         #2
        # break

        #


    elif (ch == 3):  # new member sign in

        f_name = input("Enter your first name: ")
        l_name = input("Enter your last name: ")
        address = input("Enter street address: ")
        city = input("Enter city: ")
        state = input("Enter state: ")
        zip = input("Enter zip: ")
        phone = input("Enter phone: ")
        e_mail = input("Enter email: ")
        username = input("Enter username: ")
        print(
            "Remember: Having a strong password should be between 8-13 characters with some Upper Case, Digits, and special characters")
        password = input("\nEnter Password: ")

        r = login.insertUser(username, password, f_name, l_name)
        login.insertUserDetail(username, f_name, l_name, address, city, state, zip, phone, e_mail)
        # if (r == 1):
        #   login.loginUser(username, password)
        # else:
        #   print("Username maybe taken or password is not strong")

        # elif (ch == 2):
        #   username = input("Enter username: ")
        #  password = input("Enter Password: ")

        # l = login.loginUser(username, password)
        # f(l == 0):
        # break

        # elif(ch == 3):
        # break

    else:
        print("Invalid Input")




main()
#conn.commit()