import sqlite3

from sympy import true

conn = sqlite3.connect('client.db')

c = conn.cursor()


def updateInfo(username):
    c.execute("SELECT c.cID, c.firstname, c.lastname, c.address, c.city, c.state,"
              "c.zip, c.phoneNumber, c.email FROM CLIENT AS c WHERE cID=?", (username,))
    record = c.fetchall()
    print(
        "-------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print('{:<15} {:<20} {:<20} {:<35} {:<15} {:<10} {:<10} {:<15} {:<15}'.format('CID', 'First name', 'Last name',
                                                                                  'Address', 'City', 'State',
                                                                                  'Zipcode', 'Phone number', 'E-mail'))
    print(
        "-------------------------------------------------------------------------------------------------------------------------------------------------------------")
    for r in record:
        print(
            '{:<15} {:<20} {:<20} {:<35} {:<15} {:<10} {:<10} {:<15} {:<15}'.format(r[0], r[1], r[2], r[3], r[4], r[5],
                                                                                    r[6], r[7], r[8]))

    while true:
        update_in = input("To update first and last name, Enter 'n' or\n"
                          "To update your address, Enter 'a' or \n"
                          "To update your phone number, Enter 'p' or \n"
                          "To update your E-mail, Enter 'e': \n"
                          "To go back to main menu, Press enter.")
        if (update_in == "a"):
            new_adress = input("Enter street: ")
            new_city = input("Enter city: ")
            new_state = input("Enter state: ")
            new_zip = input("Enter zip: ")
            c.execute('''UPDATE CLIENT SET address = ?, city=?, state=?, zip=? WHERE cID=?''',
                      (new_adress, new_city, new_state, new_zip, username,))
            c.execute("SELECT c.cID, c.firstname, c.lastname, c.address, c.city, c.state,"
                      "c.zip, c.phoneNumber, c.email FROM CLIENT AS c WHERE cID=?", (username,))
            rec = c.fetchall()
            print(
                "-------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print('{:<15} {:<20} {:<20} {:<35} {:<15} {:<10} {:<10} {:<15} {:<15}'.format('CID', 'First name',
                                                                                          'Last name',
                                                                                          'Address', 'City', 'State',
                                                                                          'Zipcode', 'Phone number',
                                                                                          'E-mail'))
            print(
                "-------------------------------------------------------------------------------------------------------------------------------------------------------------")
            for r in rec:
                print('{:<15} {:<20} {:<20} {:<35} {:<15} {:<10} {:<10} {:<15} {:<15}'.format(r[0], r[1], r[2], r[3],
                                                                                              r[4],
                                                                                              r[5], r[6], r[7], r[8]))
                break
            print(
                "-------------------------------------------------------------------------------------------------------------------------------------------------------------")

        elif (update_in == "p"):
            new_phone = input("Enter phone number: ")
            c.execute('''UPDATE CLIENT SET phoneNumber = ? WHERE cID=?''', (new_phone, username,))
            c.execute("SELECT c.cID, c.firstname, c.lastname, c.address, c.city, c.state,"
                      "c.zip, c.phoneNumber, c.email FROM CLIENT AS c WHERE cID=?", (username,))
            rec = c.fetchall()
            print(
                "-------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print('{:<15} {:<20} {:<20} {:<35} {:<15} {:<10} {:<10} {:<15} {:<15}'.format('CID', 'First name',
                                                                                          'Last name',
                                                                                          'Address', 'City', 'State',
                                                                                          'Zipcode', 'Phone number',
                                                                                          'E-mail'))
            print(
                "-------------------------------------------------------------------------------------------------------------------------------------------------------------")
            for r in rec:
                print('{:<15} {:<20} {:<20} {:<35} {:<15} {:<10} {:<10} {:<15} {:<15}'.format(r[0], r[1], r[2], r[3],
                                                                                              r[4],
                                                                                              r[5], r[6], r[7], r[8]))
                break
            print(
                "-------------------------------------------------------------------------------------------------------------------------------------------------------------")
        elif (update_in == "e"):
            new_email = input("Enter E-mail: ")
            c.execute('''UPDATE CLIENT SET email = ? WHERE cID=?''', (new_email, username,))
            c.execute("SELECT c.cID, c.firstname, c.lastname, c.address, c.city, c.state,"
                      "c.zip, c.phoneNumber, c.email FROM CLIENT AS c WHERE cID=?", (username,))
            rec = c.fetchall()
            print(
                "-------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print('{:<15} {:<20} {:<20} {:<35} {:<15} {:<10} {:<10} {:<15} {:<15}'.format('CID', 'First name',
                                                                                          'Last name',
                                                                                          'Address', 'City', 'State',
                                                                                          'Zipcode', 'Phone number',
                                                                                          'E-mail'))
            print(
                "-------------------------------------------------------------------------------------------------------------------------------------------------------------")
            for r in rec:
                print('{:<15} {:<20} {:<20} {:<35} {:<15} {:<10} {:<10} {:<15} {:<15}'.format(r[0], r[1], r[2], r[3],
                                                                                              r[4],
                                                                                              r[5], r[6], r[7], r[8]))
                break
            print(
                "-------------------------------------------------------------------------------------------------------------------------------------------------------------")

        elif (update_in == "n"):
            new_firstname = input("Enter First name: ")
            new_lastname = input("Enter Last name: ")
            c.execute('''UPDATE CLIENT SET firstname = ?, lastname=? WHERE cID=?''',
                      (new_firstname, new_lastname, username,))
            c.execute("SELECT c.cID, c.firstname, c.lastname, c.address, c.city, c.state,"
                      "c.zip, c.phoneNumber, c.email FROM CLIENT AS c WHERE cID=?", (username,))
            rec = c.fetchall()
            print(
                "-------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print('{:<15} {:<20} {:<20} {:<35} {:<15} {:<10} {:<10} {:<15} {:<15}'.format('CID', 'First name',
                                                                                          'Last name',
                                                                                          'Address', 'City', 'State',
                                                                                          'Zipcode', 'Phone number',
                                                                                          'E-mail'))
            print(
                "-------------------------------------------------------------------------------------------------------------------------------------------------------------")
            for r in rec:
                print('{:<15} {:<20} {:<20} {:<35} {:<15} {:<10} {:<10} {:<15} {:<15}'.format(r[0], r[1], r[2], r[3],
                                                                                              r[4],
                                                                                              r[5], r[6], r[7], r[8]))
                break
            print(
                "-------------------------------------------------------------------------------------------------------------------------------------------------------------")


        elif (update_in == ""):
            break

    conn.commit()
