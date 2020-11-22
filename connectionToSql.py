import pandas

import mysql.connector

conn = mysql.connector.connect(user='root',password='root_password',host='69.121.70.211',database='ticketingSystem',auth_plugin='mysql_native_password')


cursor = conn.cursor()

cursor.execute('SELECT id FROM ticketingSystem.users')

for row in cursor:
    print(row)
