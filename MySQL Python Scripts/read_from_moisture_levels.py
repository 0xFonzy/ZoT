#read moisture_levels
import mysql.connector
cnx = mysql.connector.connect(user='alfonsoaranzazu', password='Broncos7',
                              host='informatics117.cjtlenhgjvw5.us-west-1.rds.amazonaws.com',
                              port='3306',
                              database='informatics117db')
cursor = cnx.cursor()

command = ("SELECT * FROM moisture_levels")

cursor.execute(command)

for data in cursor:
    print(data)

