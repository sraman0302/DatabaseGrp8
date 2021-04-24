import login


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

            r = login.insertUser(f_name, l_name, username, password)
            if(r == 1):
                login.loginUser(username, password)
            else:
                print("Username maybe taken or password is not strong")

        elif(ch == 2):
            username = input("Enter username: ")
            password = input("Enter Password: ")

            l = login.loginUser(username, password)
            if(l == 0):
                break

        elif(ch == 3):
            break

        else:
            print("Invalid Input")


main()
