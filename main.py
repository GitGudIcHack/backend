import json
import datetime
import web
import pypyodbc connection = pypyodbc.connect('Driver={SQL Server};'
                                              'Server=mhutti1.eu;'
                                              'Database=ichack'
                                              'uid=ichack;pwd=ichack')

# Creates a new row in thte COMMETS database with values from the input tags.
def newCommentsEntry(tags):
    cursor = connection.cursor()
    user_id, question_val, option1, option2 = tags
    timestamp = datetime.datetime.now() # What to do about this formatting?]
    SQLCommand = ("INSERT INTO COMMENTS " +
                  "(user_id," +
                  "question_id" +
                  "question_val" +
                  "option1" +
                  "count1" +
                  "option2" +
                  "count2" +
                  "timestamp) " +
                  "VALUES (?, ?, ?, ?, 0, ?, 0, ?)")
    Values = [user_id, question_id, question_val, option1, option2, timestamp]
    cursor.execute(SQLCommand,Values)
    connection.commit()
    connection.close()

# Extracts the given entry from a given question_id
def extractEntry(target, database, query, value):
    cursor = connection.cursor()
    SQLCommand = ("SELECT ?" +
                  "FROM ?" +
                  "WHERE ? = ?")
    Values = [target, database, query, value]
    cursoor.execute(SQLCommand,Values)
    connection.commit()
    connection.close()

def parse(url):
    tags = url.split('?')
    queryType = tags[0]
    if (queryType == askq):
        selection, username = tags
        if (selection == getOption0()): #Make sure Isaac formats this correctly
                SQLCommand = ("UPDATE COMMENTS " +
                      "SET count1 = count1 + 1" +
                      "WHERE question_val = ?"
        Values = [option0, option1, ]
    elif (queryType == authenticate):
        username, password = tags
        SQLCommand = ("UPDATE USERS" +
                      "(user_id," +
                      "username," +
                      "password) " +
                      "VALUES (?,?,?)")
    else:
        try:
            urllib2.urlopen("some url")
        except urllib2.HTTPError as err:
            raise
