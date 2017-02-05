### CREATED BY JUN YOUNG ON 2016-02-04 FOR GITGUDDECISIONS.
### NAME IS A WORKING PROJECT NAME.

# Used for creating json strings to be parsed back to the website
import json
# Used for retrieving the URL from the server.
import urlparse
# import QuestionProcessing
import MySQLdb # Will need to import to web server.

headingsCOMMENTS = ['question_val'
                   ,'option1'
                   ,'count1'
                   ,'option2'
                   ,'count2'
                   ]

# Open the database connection
db = MySQLdb.connect(host='mhutti1.eu', # check this info
                     user='ichack',
                     passwd='ichack',
                     db='ichack')

# prepare a cursor object using cursor() method.
cursor = db.cursor()


# A half-assed implementation to avoid major bugs from len(options) < 2 case
#def parseQuestion(question):
#    options = QuestionProcessing.main(question)
#    if len(options) > 1:
#        return options
#    return ["Yes", "No"]

# Creates a new row in the COMMENTS database with values from the input tags.
def newCommentsEntry(tags):
    question_val, option1, option2 = tags # Change once Ilyas done.
    sql = "INSERT INTO COMMENTS \
           question_id, \
           question_val, \
           option1, \
           count1, \
           option2, \
           count2) \
           VALUES (%s, %s, %s, %s, 0, %s, 0, %d)" % (question_id,
                                                     question_val,
                                                     option1,
                                                     count1,
                                                     option2,
                                                     count2)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

# Increments the cell reference (x,y) : x = question_id; y = query by +1.
def increment(query, question_id):
    sql = "UPDATE COMMENTS \
           SET %s = %s + 1 \
           WHERE question_id = %s" % (query, query, question_id)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

def findTarget(target, resultRow):
    try:
        return resultRow[headingsCOMMENTS.index(target)]
    except:
        raise

# Extracts the given entry from a field (query) that takes a particular
# value, and returns the target field of that row.
def extractEntry(target, query, queryValue):
    sql = "SELECT * FROM COMMENTS \
           WHERE %s = %s" (query, queryValue)
    try:
        cursor.execute(sql)
        resultRow = cursor.fetchone()
        return findTarget(target, resultRow)
    except:
        db.rollback()
        raise

def returnJson(question_id):
    rtnVals = []
    for heading in headingsCOMMENTS:
        rtnVals.add(extractEntry(heading, 'question_id', question_id))
    rtn = {'question_id': question_id
           ,'question_val': rtnVals[1]
           ,'option1': rtnVals[2]
           ,'count1': rtnVals[3]
           ,'option2': rtnVals[4]
           ,'count2': rtnVals[5]
           }
    return json.dumps(rtn, ensure_ascii=False)

def genNewID():
    sql = "MAX(question_id) \
           AS HighestID \
           FROM COMMENTS"
    try:
        cursor.execute(sql)
        results = cursor.fetchone()
        return results + 1
    except:
        return 0

def parse(url):
    tags = url.split('?') # keep in mind not to use =
    queryType = tags[1]
    if (queryType == ansQ):
        question_val, selection = tags[2:]
        question_id = extractEntry('question_id',
                                   'question_val',
                                   question_val)
        increment(selection, question_id)
    elif queryType == makeQ:
        newCommentsEntry(tags[2:])
    elif queryType == get:
        question_id = tags[2]
        returnJson(question_id)
    else:
        try:
            urllib2.urlopen('some url')
        except urllib2.HTTPError as err:
            raise

# url = "http://www.website.com/?ansQ?option1?boris"
url = urlparse.parse_qs(urlparse.urlparse(self.path).query).get('imsi', None)
db.close()
