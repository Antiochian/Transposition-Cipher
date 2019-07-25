#Transposition cipher encryption

import pyperclip

def main():
    myMessage = 'Common sense is not so common.'
    myKey = 8

    ciphertext = encryptMessage(myKey, myMessage)

#Print encrypted version (with pipe to resolve any spaces)
    print(ciphertext + '|')
#copy to clipboard
    pyperclip.copy(ciphertext)

def encryptMessage(key, message):
#each string represents a column in the grid (??)
    ciphertext = ['']*key

    for col in range(key): #0-7, 8 reps total
        pointer = col

        #keep looping until pointer goes past the end of the message
        while pointer < len(message):
            ciphertext[col] += message[pointer]

            #move pointer
            pointer += key

    #convert output into a string and return it
    return ''.join(ciphertext)

#If script is run as a script instead of a function, just call the function
if __name__=='__main__':
    main()
