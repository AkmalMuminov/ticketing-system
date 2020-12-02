import pandas

import mysql.connector

from datetime import datetime
now = datetime.now()
formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')

conn = mysql.connector.connect(user='root',password='root_password',host='69.121.70.211',database='ticketingSystem',auth_plugin='mysql_native_password')

cursor = conn.cursor()

def queryByID(idNumber):
    ticket = []
    cursor.execute('SELECT * FROM ticketingSystem.tickets WHERE ID = '+str(idNumber))
    for row in cursor:
        ticket.append(row)
    return ticket

def queryByKeyword(words):
    tickets = []
    cursor.execute("SELECT * FROM ticketingSystem.tickets WHERE name LIKE '%s' OR description LIKE '%s'" % (str('%'+words+'%'), str('%'+words+'%')))
    for row in cursor:
        tickets.append(row)
    return tickets

def queryByStatus(status):
    tickets = []
    cursor.execute("SELECT * FROM ticketingSystem.tickets WHERE status = '%s'" % str(status))
    for row in cursor:
        tickets.append(row)
    return tickets

def updateStatusOfTicket(ticketID, ticketStatus):
    if(ticketStatus.lower() == 'open'):
        ticketStatus = 'Closed'
    else:
        ticketStatus = 'Open'
    cursor.execute("UPDATE ticketingSystem.tickets SET status = '%s' WHERE ID = %s" % (str(ticketStatus), str(ticketID)))

# doesUserExist: This function takes a username and checks against our database to see if there's a match.
# Return true: The inputted username exists in our SQL database
# Return false: The inputted username does not exist in our SQL database
def doesUserExist(userName): 
    cursor.execute("SELECT * FROM ticketingSystem.users WHERE userName = '%s'" % str(userName))
    user = []
    for row in cursor:
        user.append(row)
    if len(user) == 0:
        return False
    else:
        return True

# addTicket: This function adds a new ticket to the databse. Input the name of the ticket, a description, and the ticket status.
# Note that ID will automatically be filled in with SQL's auto-increment, and the date will automatically fill in with the time of execution. 
# Example: addTicket('Python ticket Testing', 'Adding ticket with python', 'closed')
def addTicket(name, description, status):
    sql = "INSERT INTO tickets (name, description, date, status) VALUES (%s, %s, %s, %s)"
    val = (str(name), str(description), formatted_date, str(status))
    cursor.execute(sql, val)    

#searcher = "closed"

#updateStatusOfTicket(1,'closed')

# The commit method is necessary to commit changes that modify / add data to the database. 
conn.commit()

