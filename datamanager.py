import sqlite3

# Create a connection to the local database
connection = sqlite3.connect("myFirstTable.db")

# Begin a query
cursor = connection.cursor()

# Create our command we want the database to process
sql_command = """CREATE TABLE test (  
person_number INTEGER PRIMARY KEY,  
fname VARCHAR(20),  
lname VARCHAR(30),  
gender CHAR(1),  
joining DATE);"""

# Execute the command that we just made
cursor.execute(sql_command)

# Add a row to the table we just made
sql_command = """INSERT INTO people VALUES (1, "Alex", "Day", "M", "2020-11-15");"""
cursor.execute(sql_command)

# Commit the commands we just executed
connection.commit()

# Close our connection
connection.close()