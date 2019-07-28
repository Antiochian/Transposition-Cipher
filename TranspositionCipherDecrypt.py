#Transposition cipher decryption
import math

def main(): #example behaviour if run as script
    myMessage = 'Cenoonommstmme oo snnio. s s c'
    myKey = 8
    plaintext = decryptMessage(myKey, myMessage)
    print(plaintext) #output

def decryptMessage(key, ciphertext):
    width = math.ceil(len(ciphertext)/key)
    height = key
    plaintext = ['']*width #draws up columnar table
    shadedboxes = (height*width) - len(ciphertext) #number of leftover cells in table
#pointer coordinates, start at 0
    x = 0 #table column number
    y = 0 #table row number
    
    boxes_skipped = 0 #need this to adjust pointer accordingly
    while y < key - shadedboxes: #before we get to any shaded boxes
        while x < width: # iterating horizontally
            debugger = width*y + x
            plaintext[x] += ciphertext[width*y + x]
            x += 1
        y += 1 #reset x and go to next y
        x = 0

    for i in range(shadedboxes): #final few rows containing nullspaces
        while x < width - 1: # iterating horizontally but SKIPPING nulls in final column
                debugger = width*y + x
                plaintext[x] += ciphertext[width*y + x - boxes_skipped]
                x += 1
        boxes_skipped += 1 #this is to accommodate boxskip
        y += 1
        x = 0

        
    #output total strings catted together
    return ''.join(plaintext)

#if function is run as script, use default values
if __name__ == '__main__':
    main()
