import login
import admin_login
import sqlite3

from sympy import true


# conn = sqlite3.connect('mypersonal.db')

# c = conn.cursor()


def main():
    while true:
        print("*****************************************************************************************************")
        print("**--------                                                                                 --------**")
        print("**---                            Welcome to Online Book-Store                                   ---**")
        print("**--------                                                                                 --------**")
        print("*****************************************************************************************************")
        print("* ---------------                                                                   --------------- *")
        print("* ------                              1. Customer Login                                      ------ *")
        print("* ---------------                                                                   --------------- *")
        print("* ------                              2. Admin Login                                         ------ *")
        print("* ---------------                                                                   --------------- *")
        print("* ------                              3. New member sign in                                  ------ *")
        print("* ---------------                                                                   --------------- *")
        print("* ------                              4. Quite                                               ------ *")
        print("* ---------------                                                                   --------------- *")
        print("*****************************************************************************************************")
        print()
        try:
            ch = int(input("Enter your choice: "))

            if (ch == 1):  # customer login
                username = input("Enter username: ")
                password = input("Enter Password: ")
                login.loginUser(username, password)

            elif (ch == 2):  # admin login

                username = input("Enter username: ")
                password = input("Enter Password: ")
                admin_login.loginAdmin(username, password)

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
                    "Remember: Having a strong password should be between 8-13 characters with some Upper Case, Digits, "
                    "and special characters")
                password = input("\nEnter Password: ")

                login.insertUser(username, password, f_name, l_name)
                login.insertUserDetail(username, f_name, l_name, address, city, state, zip, phone, e_mail)

            elif (ch == 4):
                print(
                    "*****************************************************************************************************")
                print(
                    "**--------                                                                                 --------**")
                print(
                    "**---                            Thank You for visiting                                         ---**")
                print(
                    "**--------                         Online Book-Store                                       --------**")
                print(
                    "*****************************************************************************************************")
                break
        except ValueError:
            print("No such command exists. try again...")


main()
# conn.commit()
