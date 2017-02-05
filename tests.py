import Processing

def parseQuestionTests(question, expected):
    actual = main.parseQuestion(question)
    if (not actual == expected):
        print "Tests failed: expected %s, got %s." % (expected, actual)

def newCommentsEntryTests(tags, expected):
    actual = main.newCommentsEntryTests(tags)

def runTests():
    parseQuestionTests('Should I Go To Tesco Or Sainsbury\'s', ['Tesco', 'Sainsburys'])
    parseQuestionTests('trump or hillary?', ['trump', 'hillary'])
    parseQuestionTests('Memeperial or UCL-Memes-for-Light-Guided-Teens',
                       ['Memeperial', 'UCL-Memes-for-Light-Guided-Teens'])
    parseQuestionTests('Should i go to ICHack \'18?', ['Yes', 'No'])

runTests()
