import psycopg2
# first you start by importing psycopg2
connection = psycopg2.connect(database="postgres",
                user="postgres", password="1111")
# create a connection using the database name, user
# name and password
cursor = connection.cursor()
# create the cursor with the connection created

cursor.execute('DROP TABLE IF EXISTS table10;')
# the line above is there to take down the table if
# it exists
cursor.execute(
    """CREATE TABLE table10(
        id INTEGER PRIMARY KEY,
        complete BOOLEAN NOT NULL DEFAULT False
    );
    """
)
# the block of code above is used to create the table
# take note of the triple quotation marks, triple 
# quotes allow multiline text in python

cursor.execute('INSERT INTO table10 (id, complete)'
               + 'VALUES (1,True);')

cursor.execute('INSERT INTO table10 (id, complete)'
               + 'VALUES (%s,%s);',(2,False))

SQL ='INSERT INTO table10 (id, complete) VALUES (%(id)s,%(complete)s);'
DATA = {'id': 3, "complete":True}

cursor.execute(SQL,DATA)
# the lines of code above are used to insert data into the table
# I used 3 different techniques to do this.

cursor.execute('SELECT * FROM table10')
# the line above is used to get data from the table

result = cursor.fetchone()
result1 = cursor.fetchall()
result2 = cursor.fetchmany(2)
# the fetch function is used to get data, it allows us to 
# see the output in our terminal when we run our python code.
# there are several types of fetch function, they are all above.
# only fetchmany takes argument


print("fetchone",result)
print("fetchall",result1)
print("fetchmany",result2)
# print function is for printing the result 

connection.commit()
# commit. so it does the execution on the db.
connection.close()
cursor.close()
# the last 2 lines are for closing the connection
# it doesn't close automatically.