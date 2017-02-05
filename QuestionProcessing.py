from topia.termextract import tag

tagger = tag.Tagger()
tagger.initialize()

#removes all apostrophes due to limited functionality
#of the nlp module. sad :(
def process(string):
    return tagger(string.replace("'", ''))

#checkes for 4 types of nouns and whether the string is an 'or'
#rejects the rest
def extractNounsAndOr(string):
    taggedList = process(string)
    result = [element[0] for element in taggedList if element[1] == 'NN' or
                                                   element[1] == 'NNS' or
                                                   element[1] == 'NNP' or
                                                   element[1] == 'NNPS' or
                                                   element[0] == 'or']
    return result

#returns boolean of whether the string contains an 'or'
def containsOr(string):
    taggedList = process(string)
    for tag in taggedList:
        if tag[0] == 'or':
            return True
    return False

#partitions the list of nouns at the position of 'or'
#returns a tuple of the two partitions with th nouns concatenated
def separateWithOr(nouns):
#pre: the list nouns contains 'or'
    checker = True
    counter = 0
    while checker:
        if nouns[counter] == 'or':
            a = nouns[:counter]
            b = nouns[counter + 1:]
            return (' '.join(a), ' '.join(b))
        counter += 1


#main function of the file that provides the desired functionality
#returns the two options arising from the question
#can be Yes or No, or significant keywords from the question
def main(string):
    if containsOr(string):
        nouns = extractNounsAndOr(string)
        return separateWithOr(nouns)
    else:
        return ('Yes', 'No')
