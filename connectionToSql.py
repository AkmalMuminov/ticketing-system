import pandas
import mysql.connector
from datetime import datetime
now = datetime.now()
formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')

conn = mysql.connector.connect(user='root',password='root_password',host='69.121.70.211',database='ticketingSystem',auth_plugin='mysql_native_password')

cursor = conn.cursor()


def dateCleaner(date):
    date = date[14: len(date)-1]
    date = date.split(', ', 2)
    cleanDate = date[1]+'-'+date[2]+'-'+date[0]
    return cleanDate


def queryCleaner(query):
    query = str(query)
    indexStart = query.index("date")
    indexEnd = query.index(")")
    cleanDate = dateCleaner(query[indexStart:indexEnd]+')')
    query = query[0:indexStart] + cleanDate + query[indexEnd+1:len(query)]
    if 'date' in query:
        indexStart = query.index("date")
        indexEnd = query.index(")")
        cleanDate = dateCleaner(query[indexStart:indexEnd]+')')
        query = query[0:indexStart] + cleanDate + query[indexEnd+1:len(query)]
    query = query.replace("(",'').replace("'",'').replace(")",'')
    return query


def arrayCleaner(arrayOfQueries):
    i = 0
    for i in range(len(arrayOfQueries)):
        arrayOfQueries[i] = queryCleaner(arrayOfQueries[i])
    return arrayOfQueries


def sqlToArray(cursor):
    array = []
    for row in cursor:
        array.append(row)
    return array


def queryDefault():
    cursor.execute('SELECT * FROM ticketingSystem.tickets')
    ticket = sqlToArray(cursor)
    ticket = arrayCleaner(ticket)
    print(ticket)

# queryByID: This function uses passed ID number and checks if it exists in the DB.
# Return String: A string is returned when the ID number does not match a ticket in the DB.
# Return Array: An array is returned if the ID number exists in the DB.
def queryByID(idNumber):
    cursor.execute('SELECT * FROM ticketingSystem.tickets WHERE ID = '+str(idNumber))
    ticket = sqlToArray(cursor)
    ticket = arrayCleaner(ticket)
    if not ticket:
        print('False')
        return False
    else:
        print(ticket)
        return ticket

# queryByKeyword: This function uses passed word and checks if it char/string exists in ANY ticket name or description.
# Return Array: An array is returned if the word is associated with a ticket, the array is the ticket(s) that contains the word.
# Return String: A string is returned if the word is not associated with a ticket, the string informs that no such ticket does not exist.
def queryByKeyword(words):
    cursor.execute("SELECT * FROM ticketingSystem.tickets WHERE name LIKE '%s' OR description LIKE '%s'" % (str('%'+words+'%'), str('%'+words+'%')))
    tickets = sqlToArray(cursor)
    tickets = arrayCleaner(tickets)
    if not tickets:
        return 'The entered word does not exist in any existing ticket.'
    else:
        print(tickets)

# queryByStatus: This function uses passed status and returns all tickets with that status.
# Return Array: An array is returned if the status corresponds with a ticket in the DB, this array is the ticket(s) with the matching status.
# Return String: A String is returned if there is no ticket in the DB with passed status.
def queryByStatus(status):
    cursor.execute("SELECT * FROM ticketingSystem.tickets WHERE status = '%s'" % str(status))
    tickets = sqlToArray(cursor)
    tickets = arrayCleaner(tickets)
    print(tickets)


def queryByLastUser(lastUser):
    cursor.execute("SELECT * FROM ticketingSystem.tickets WHERE lastUser = '%s'" % str(lastUser))
    tickets = sqlToArray(cursor)
    tickets = arrayCleaner(tickets)
    print(tickets)


def queryByDate(date):
    cursor.execute("SELECT * FROM ticketingSystem.tickets WHERE dateCreated = '%s' OR dateResolved = '%s'" % (str(date), str(date)))
    tickets = sqlToArray(cursor)
    tickets = arrayCleaner(tickets)
    print(tickets)

# updateStatusOfTicket: This function takes a uses the ticket ID to locate the ticket and then updates the ticket status based on the existing status.
# Return string: Returns appropriate string based on if the ticket ID given exists in the Database.
def updateStatusOfTicket(ticketID):
    checkExists = queryByID(ticketID)
    if not checkExists:
        return 'There is no ticket associated with this ticket ID.'
    else:
        cursor.execute("UPDATE ticketingSystem.tickets SET status = 'Closed', dateResolved = '%s' WHERE ID = %s" % (formatted_date, str(ticketID)))
        conn.commit()
        return 'Ticket Updated'


def updateCategory(ticketID, newCat):
    cursor.execute("UPDATE ticketingSystem.tickets SET category = '%s' WHERE ID = %s" % (str(newCat), str(ticketID)))
    conn.commit()

def updateName(ticketID, newName):
    cursor.execute("UPDATE ticketingSystem.tickets SET name = '%s' WHERE ID = %s" % (str(newName), str(ticketID)))
    conn.commit()

def updateDescription(ticketID, newDescrip):
    cursor.execute("UPDATE ticketingSystem.tickets SET description = '%s' WHERE ID = %s" % (str(newDescrip), str(ticketID)))
    conn.commit()

def updateLastUser(ticketID, newLastUser):
    cursor.execute("UPDATE ticketingSystem.tickets SET lastUser = '%s' WHERE ID = %s" % (str(newLastUser), str(ticketID)))
    conn.commit()


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
def addTicket(name, description, status, lastUser, category):
    sql = "INSERT INTO tickets (name, description, status, lastUser, category, dateCreated) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (str(name), str(description), str(status), str(lastUser), str(category), formatted_date)
    cursor.execute(sql, val)
    conn.commit()


# addUser: This function adds a new user to the database. Input the username and password.
# Note that the user's ID will be automatically assigned with SQL's auto-increment.
# Example: addUser('PythonTest', 'abc123')
def addUser(userName, password):
    sql = "INSERT INTO users (userName, password) VALUES (%s, %s)"
    val = (str(userName), str(password))
    cursor.execute(sql, val)
    conn.commit()


def userLogin(userName, password):
    val = (str(userName), str(password))
    sql = "SELECT * FROM users WHERE userName = %s AND password = %s"
    cursor.execute(sql, val)
    login = sqlToArray(cursor)
    if not login:
        print('False')
    else:
        print('True')


#----------------------TEST CASES/ERRORS TO BE FIXED AND REMOVED ----------------------------------

#print(queryCleaner("(1, 'test2', '2', datetime.date(2020, 12, 2), 'closed')"))
#array = queryByStatus('closed')
#print(array[1])
#print(arrayCleaner(array))
#print(len(array))
#print(len(queryByStatus('closed')))
#array = queryByStatus('closed')
#print(len(queryByStatus('closed')))
#print(arrayCleaner(array))
#dateCleaner('datetime.date(2020, 12, 2)')

#template array [(1, 'test2', '2', datetime.date(2020, 12, 2), 'closed'), (2, 'test1', '1', datetime.date(2020, 12, 2), 'closed')]
#template date  datetime.date(2020, 12, 2)
#                             12-2-2020

#searcher = "closed"

#updateStatusOfTicket(1,'closed')



# The commit method is necessary to commit changes that modify / add data to the database. 
conn.commit()

