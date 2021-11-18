import sqlite3
import pandas as pd

class DataManager(object):
    '''
    Main SQL-facing object that allows the user/bot to grab, insert, or alter 
    data in the database associated with web scraping.
    '''
    def __init__(self):
        # Create a connection to the local database
        connection = sqlite3.connect("scrapingData.db")

        # Begin a query
        cursor = connection.cursor()

        # Try to create the table "people"
        try:
            # Create our command we want the database to process
            sql_command = """CREATE TABLE people (  
            person_number INTEGER PRIMARY KEY,  
            fname VARCHAR(20),  
            lname VARCHAR(30),  
            gender CHAR(1),  
            joining DATE);"""

            # Execute the command that we just made
            cursor.execute(sql_command)

        except sqlite3.OperationalError:
            print('"People" table already made...')

        # Add a row to the table we just made
        sql_command = """
        INSERT INTO people VALUES (3, "Alex", "Day", "M", "2020-11-15");
        """
        cursor.execute(sql_command)

        # Commit the commands we just executed
        connection.commit()

        print('Trying to get data...')

        com = """
        SELECT * FROM people;
        """
        cursor = connection.cursor()
        cursor.execute(com)
        ans = cursor.fetchall()
        print(ans)

        df = pd.read_sql_query("SELECT * FROM people;", connection)
        print(df.head())

        # Close our connection
        connection.close()

if __name__ == "__main__":
    manager = DataManager()
