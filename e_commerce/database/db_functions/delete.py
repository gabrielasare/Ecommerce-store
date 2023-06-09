import sqlite3
import sys

## attempts to connect to the database
def delete_data(query):
    try:
        connection = sqlite3.connect("sqlite.db")

    except:
        print("Failed connection.")

        ## exits the program if unsuccessful
        sys.exit()

    ## cursor to send queries through
    cursor = connection.cursor()

    cursor.execute(query)
    connection.commit()

    cursor.close()
    connection.close()
