#Detect English %
#This call-only function returns a "score" between 0 and 1 of "english-ness"
#to use this script a dictionary file "dictionary.txt" is required

def processText(plaintext): #this function takes input text, removes odd characters (?!@~#£& etc...)
    upper_text = plaintext.upper()
    known_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ \t \n"
    processed_text = []
    for char in upper_text:
        if char in known_chars:
            processed_text.append(char) #append() is much faster than +=, important for large dictionary files
    return ''.join(processed_text)

def loadWordList(): #this function reads a "simple_dictionary.txt" file
    dictionaryFile = open("simple_dictionary.txt")
    WordList = {} #set up dictionary of english words

    for item in dictionaryFile.read().split('\n'):
        WordList[item] = None #add each item in dictionary file to dictionary object
    dictionaryFile.close()
    return WordList

def countWords(message, WORD_LIST): #this function finds the percentage of words (delineated with spaces) in "message" that are also in "WORD_LIST"
    messagelist = message.split()
    if messagelist == []: #edge case to catch divide-by-zero errors
        return 0.0  
    matches = 0
    for word in messagelist:
        if word in WORD_LIST:
            matches += 1
    return (float(matches) / len(messagelist)) #number between 0 and 1

def isEnglish(plaintext,wordpercent = 0.20, letterpercent = 0.80): #primary function to be called, with default parameters for how stringent the "isenglish" condition is
    WORD_LIST = loadWordList() #call each aforementioned function
    processed_text = processText(plaintext)
    letterscore = (len(processed_text)/len(plaintext))
    wordscore = countWords(processed_text,WORD_LIST)
    if wordscore >= wordpercent:
        wordmatch = True
    else:
        wordmatch = False
    if letterscore >= letterpercent:
        letterscore = True
    else:
        letterscore = False
        
    return (wordmatch and letterscore) #boolean output - True for is english, False for is NOT english

#didn't bother with main() function as this should never be run as a script
