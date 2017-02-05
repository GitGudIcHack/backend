import json
import datetime
import web
import os
import pypyodbc connection = pypyodbc.connect('Driver={SQL Server};'
                                              'Server=mhutti1.eu;'
                                              'Database=ichack'
                                              'uid=ichack;pwd=ichack')

# Creates a new row in thte COMMENTS database with values from the input tags.
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
    cursor.execute(SQLCommand, Values)
    connection.commit()
    connection.close()

def increment(query, question_id):
    cursor = connection.cursor()
    SQLCommand = ("UPDATE COMMENTS " +
                 "SET ? = ? + 1 " +
                 "WHERE question_id = ?")
    Values = [query, query, question_id]
    cursor.execute(SQLCommand, Values)
    connection.commit()
    connection.close()

    # Extracts the given entry from a field (query) that takes a particular
    # value, and returns the target field of that row.
def extractEntry(target, database, query, value): # wtf does this return
    cursor = connection.cursor()
    SQLCommand = ("SELECT ? " +
                  "FROM ? " +
                  "WHERE ? = ?")
    Values = [target, database, query, value]
    cursor.execute(SQLCommand, Values)
    connection.commit()
    connection.close()

def exists(username): # wtf does this return
    cursor = connection.cursor()
    SQLCommand = ("IF EXITS (SELECT * FROM COMMENTS " +
                  "WHERE username = ?)")
    Values = [username]
    cursor.execute(SQLCommand, Values)
    connection.commit()
    connection.close()

def returnJson(question_id):
    rtnTypes = ['user_id'
                ,'question_val'
                ,'option1'
                ,'count1'
                ,'option2'
                ,'count2'
                'timestamp'
                ]
    rtnVals = []
    for (rtn in rtntypes):
        rtnVals.add(extractEntry(rtn, 'COMMENTS', 'question_id', question_id))
    rtn = {'user_id': rtnVals[0]
           ,'question_id': question_id
           ,'question_val': rtnVals[1]
           ,'option1': rtnVals[2]
           ,'count1': rtnVals[3]
           ,'option2': rtnVals[4]
           ,'count2': rtnVals[5]
           ,'timestamp': rtnVals[6]
           }
    return rtn

def parse(url):
    tags = url.split('?') # What about formatting with =
    queryType = tags[0]
    if (queryType == ansQ):
        question_id, selection, username = tags[1:]
        increment(selection, question_id)

    elif (queryType == authenticate):
        username, pwd = tags[1:] # formatting must be correct
        if not (exists(username) &&
                pwd == extractEntry('password',
                                    'COMMENTS',
                                    'username',
                                    username)):
            raise
    elif (queryType == get):
        question_id = tags[1]
        returnJson(question_id)
    else:
        try:
            urllib2.urlopen('some url')
        except urllib2.HTTPError as err:
            raise

url = "http://www.website.com/?ansQ?option1?boris"
# url = os.environ["REQUEST_URI"]
print parse(url) # change this line as necessary
