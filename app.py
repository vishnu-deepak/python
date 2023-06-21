from flask import Flask
import mysql.connector

app = Flask(_name_)

@app.route('/')
def hello():
    # Connect to AWS RDS database
    cnx = mysql.connector.connect(
        host='vdb.cuipeazl8ijo.us-east-1.rds.amazonaws.com',
        user='vishnudeepak',
        password='vishnu0544',
        database='vdb'
    )

    # Create a cursor to execute SQL queries
    cursor = cnx.cursor()

    # Execute a sample SQL query
    cursor.execute("SELECT * FROM your_table")

    # Fetch all the rows from the result
    rows = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    cnx.close()

    # Return the rows as a response
    return str(rows)

if _name_ == '_main_':
    app.run()
