import topiaAllFiles.src.topia.termextract.tag

tagger = tag.Tagger()
tagger.initialize()

def process(string):
    return tagger(string.replace("'", ''))

def extractNounsAndOr(string):
    taggedList = process(string)
    result = [element[0] for element in taggedList if element[1] == 'NN' or
                                                   element[1] == 'NNS' or
                                                   element[1] == 'NNP' or
                                                   element[1] == 'NNPS' or
                                                   element[0] == 'or']
    return result

def containsOr(string):
    taggedList = process(string)
    for tag in taggedList:
        if tag[0] == 'or':
            return True
    return False

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



def main(string):
    if containsOr(string):
        nouns = extractNounsAndOr(string)
        return separateWithOr(nouns)
    else:
        return ('Yes', 'No')

print main("Should I got to World-Championship today or Tesco tomorrow?")
print main("should I break up with my boyfriend and his brother?")
print main("UCL or Imperial")
print main("Should I got to Andrew's house today or Tesco tomorrow?")
