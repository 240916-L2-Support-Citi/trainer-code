import psycopg # This brings in any outside libraries or modules that don't come in by default.
               # Note, we import psycopg not psycopg3 or something like that. 
               # P.S. Note: We are using psycopg3 for this! Not 2. Always make sure you are viewing the correct
               # documentation. 

import os # Importing OS so I can write to my file.

# Try-Except-Finally(optional)

fileName = "./logs/sql-output-log.txt" # File name/path for my log

try: # Code that I think may cause some sort of error, will go in my try.
     # Things like, connecting and working with a SQL database, reading/writing to a file.
     # Also things like working with outside APIs or external tools. 
    with psycopg.connect( # Using "with" simplifies the disposal of objects after we finish our "try"
        "dbname=chinook user=jon password=ellie host=/var/run/postgresql port=5432"
    ) as connection: # We are calling the psycopg.connect() function, that returns a connection object. 
    # We then assign it to a variable we can easily reference, in my case "connection"
    # Connection handles the connection to the db
    # We need to create a cursor (a psycopg library object) to actually do CRUD operations against our database
        with connection.cursor() as my_cursor:

            #If I want to execute a SQL query, I use my cursor to do so.
            #First, lets do a select.
            my_cursor.execute("SELECT * FROM album")

            records = my_cursor.fetchall() # This returns a list of tuples, that correspond to the rows in the table
            for row in records:
                # Here we open our file, and append each record into our sql-output-log.txt
                with open(fileName, 'a') as file:
                    file.write(str(row) + "\n") # Manually adding a new line, for readability. 

                print(row)
                print(type(row))

            

            print(type(records))

            # Lets do an insert, based on user input

            # First, let me get my user input
            new_actor_fname = input("Enter a first name: ")
            new_actor_lname = input("Enter a last name: ")

            # Use the cursor to execute the INSERT
            my_cursor.execute(
                "INSERT INTO actor (first_name, last_name) VALUES (%s, %s)", # Use placeholders to parameterize our query
                (new_actor_fname, new_actor_lname)
            )

except Exception as e:
    print("Error connecting to my db: ", e)

# finally: # Any code that we want to have run after our try, REGARDLESS of whether 
# an exception was raised during the running of that code, we put in the finally. 
