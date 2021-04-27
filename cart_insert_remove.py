import sqlite3

conn = sqlite3.connect('bookstore.db')

c = conn.cursor()

def bookAvailability(ISBN):         #checks availibility of Books
   # ISBN = input('ISBN ')
    if c.execute('''SELECT * FROM BOOK as B WHERE ? = B.ISBN''',(ISBN,)).fetchone():
        print("Found")
        return True
    else:
        print("Not found")
        return False
    



def addToCart(): #  have parameters isbn and cid

    ISBN = input('ISBN ')
    cID = input('cID ')

    availability = bookAvailability(ISBN)     # gets availability
    print(availability)
   
    if(availability == False):
        print("book not found.  \n")
        return


    for value in c.execute('''SELECT title FROM BOOK as B WHERE ? == B.ISBN ''',(ISBN,)):     # gets title for cart table
        title = value[0]    
        break
    else:
        print("book not found")
    for row in c.execute('''SELECT price FROM BOOK as B WHERE ? == B.ISBN ''',(ISBN,)):          #gets price for cart table
        price = row[0]    
        break
    else:
        print("book not found")

    

    c.execute('''INSERT INTO CART (cID,ISBN,price,title) VALUES(?,?,?,?)''', (cID,ISBN,price,title,))
    print("added to cart. ")




def removeFromCart(): # parameters isbn and cID

    ISBN = input('ISBN ')
    cID = input('cID ')

    c.execute('''DELETE FROM CART as C WHERE ? = C.ISBN AND ? = C.cID ''', (ISBN,cID))

def priceInCart(): # cID parameter

    cID = input('cID ')

    for row in c.execute('''SELECT C.price, C.title, C.ISBN FROM CART as C WHERE ? == C.cID ''',(cID,)):          #gets price for cart table
        price = row[0]   
        title = row[1] 
        ISBN = row[2]
        break
    else:
        print("book not found")

  #  print(price)
    print("price is:", price, "$ for", title,  "ISBN: ", ISBN)



def main():

    while(True):
        print("1. ADD to Cart ")
        print("2. Remove item in Cart ")
        print("3. Print Cart ")
        print("4. Price of all items in cart ")
        print("5. EXIT")

        choice = int(input("your choice: "))
        
        if(choice == 1):
            addToCart()
        elif(choice == 2):
            removeFromCart()

        elif(choice == 3):
            cID = input("cID: ")
            c.execute(''' SELECT * FROM CART as C  WHERE ? == C.cID ''', (cID,))
            print(c.fetchall())
       
        elif(choice == 4):
            priceInCart()

        elif(choice == 5):
            break;

        else:
            print("invalid input")
    

main()

conn.commit()