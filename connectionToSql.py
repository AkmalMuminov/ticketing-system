import pandas

import mysql.connector

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

def doesUserExist(userName): 
    cursor.execute("SELECT * FROM ticketingSystem.users WHERE userName = '%s'" % str(userName))
    
    user = []
    for row in cursor:
        user.append(row)
    
    if len(user) == 0:
        return False
    else:
        return True

searcher = "closed"

print(queryByKeyword('test'))