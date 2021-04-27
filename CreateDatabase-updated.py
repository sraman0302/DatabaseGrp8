import sqlite3

conn = sqlite3.connect('bookstore.db')

c = conn.cursor()

#create tables

c.execute( '''CREATE TABLE BOOK( [ISBN] TEXT PRIMARY KEY, [author] text, [year] integer, [title] text, [price] integer)''')

c.execute('''CREATE  TABLE CUSTOMER ([cID] INTEGER PRIMARY KEY, [firstname] text, [lastname] text, [phoneNumber] integer, [email] text, [address] text)''' )

c.execute('''CREATE  TABLE CART ([cID] text, [ISBN] text, [price] integer, [title] text, PRIMARY KEY(cID, ISBN))''' )

c.execute('''CREATE  TABLE ADMINISTRATION([User_ID] integer PRIMARY KEY, [password] text, [firstname] text, [lastname] text)''')



c.execute('''INSERT INTO BOOK VALUES(60935464,'Harper Lee',1960,'To Kill a Mocking Bird',10)''')
c.execute(''' INSERT INTO BOOK VALUES(452284236,'George Orwell',1950 ,'1984', 11.99)''')
c.execute(''' INSERT INTO BOOK VALUES(9780544003415,'J.R.R Tolkien ',1955 ,'The Lord of the Rings' ,13 )''')
c.execute(''' INSERT INTO BOOK VALUES(1439550050,'J.D Salinger ',2008 ,'The Catcher In the Rye' ,20 )''')
c.execute(''' INSERT INTO BOOK VALUES(743273567 ,'Fitzgerald, F. Scott ',2004 ,'The Great Gatsby' , 10)''')
c.execute(''' INSERT INTO BOOK VALUES( 1583030484,'William Golding ',1998 ,'Lord of The Flies',35)''')
c.execute(''' INSERT INTO BOOK VALUES(143039431 ,'John Steinbeck ',2006,'The Grapes of Wrath' , 18)''')
c.execute(''' INSERT INTO BOOK VALUES( 1451635621,'Margaret Mitchell',2011 ,'Gone With the Wind' ,15 )''')
c.execute(''' INSERT INTO BOOK VALUES(808514571 ,'Kurt Vonnegut',1991 ,'Slaughterhouse-five' , 13)''')
c.execute(''' INSERT INTO BOOK VALUES(679723161 ,'Vladimir Nabokov ',1989 ,'Lolita' ,16 )''')
c.execute(''' INSERT INTO BOOK VALUES(1779501129 ,'Alan Moore ',2019 ,'Watchmen' ,16 )''')
c.execute(''' INSERT INTO BOOK VALUES(451531671 ,'H.G.Wells ',2010 ,'The Invisible Man' ,5 )''')
c.execute(''' INSERT INTO BOOK VALUES( 140283293,'Jack Kerouac ',1999 ,'On The Road' ,11 )''')
c.execute(''' INSERT INTO BOOK VALUES(1501121960 ,'Ernest Hemmingway ',2016 ,'The Sun Also Rises' , 12)''')
c.execute(''' INSERT INTO BOOK VALUES( 156711427,'Forster, E.M.',1965 ,'A Passage to India' ,16 )''')
c.execute(''' INSERT INTO BOOK VALUES(671489410 ,'Lewis Carol',1979 ,'Alice in Wonderland' , 5)''')
c.execute(''' INSERT INTO BOOK VALUES(156907399 ,'Virginia Woolf ',1989 ,'To The LightHouse' ,16 )''')
c.execute(''' INSERT INTO BOOK VALUES(679732268 ,'William Faulkner ',1990 ,'Light In August' , 17)''')

conn.commit()
conn.commit()

