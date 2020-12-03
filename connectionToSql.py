import pandas
import mysql.connector
from datetime import datetime
now = datetime.now()
formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')

conn = mysql.connector.connect(user='root',password='root_password',host='69.121.70.211',database='ticketingSystem',auth_plugin='mysql_native_password')

cursor = conn.cursor()

def sqlToArray(cursor):
    array = []
    for row in cursor:
        array.append(row)   
    return array

# queryByID: This function uses passed ID number and checks if it exists in the DB.
# Return String: A string is returned when the ID number does not match a ticket in the DB.
# Return Array: An array is returned if the ID number exists in the DB.
def queryByID(idNumber):
    cursor.execute('SELECT * FROM ticketingSystem.tickets WHERE ID = '+str(idNumber))
    ticket = sqlToArray(cursor)
    return ticket

# queryByKeyword: This function uses passed word and checks if it char/string exists in ANY ticket name or description.
# Return Array: An array is returned if the word is associated with a ticket, the array is the ticket(s) that contains the word.
# Return String: A string is returned if the word is not associated with a ticket, the string informs that no such ticket does not exist.
def queryByKeyword(words):
    cursor.execute("SELECT * FROM ticketingSystem.tickets WHERE name LIKE '%s' OR description LIKE '%s'" % (str('%'+words+'%'), str('%'+words+'%')))
    tickets = sqlToArray(cursor)
    if not tickets:
        return 'The entered word does not exist in any existing ticket.'
    else:
        return tickets

# queryByStatus: This function uses passed status and returns all tickets with that status.
# Return Array: An array is returned if the status corresponds with a ticket in the DB, this array is the ticket(s) with the matching status.
# Return String: A String is returned if there is no ticket in the DB with passed status.
def queryByStatus(status):
    cursor.execute("SELECT * FROM ticketingSystem.tickets WHERE status = '%s'" % str(status))
    tickets = sqlToArray(cursor)
    return tickets

# updateStatusOfTicket: This function takes a uses the ticket ID to locate the ticket and then updates the ticket status based on the existing status.
# Return string: Returns appropriate string based on if the ticket ID given exists in the Database.
def updateStatusOfTicket(ticketID, ticketStatus):
    checkExists = queryByID(ticketID)
    if not checkExists:
        return 'There is no ticket associated with this ticket ID.'
    else:
        if(ticketStatus.lower() == 'open'):
            ticketStatus = 'Closed'
        else:
            ticketStatus = 'Open'
        cursor.execute("UPDATE ticketingSystem.tickets SET status = '%s' WHERE ID = %s" % (str(ticketStatus), str(ticketID)))
        return 'Ticket Updated'
    

# doesUserExist: This function takes a username and checks against our database to see if there's a match.
# Return true: The inputted username exists in our SQL database.
# Return false: The inputted username does not exist in our SQL database.
def doesUserExist(userName): 
    cursor.execute("SELECT * FROM ticketingSystem.users WHERE userName = '%s'" % str(userName))
    user = sqlToArray(cursor)
    if not user:
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

