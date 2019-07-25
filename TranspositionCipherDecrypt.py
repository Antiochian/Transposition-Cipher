#Transposition cipher decryption
import math

def main():
    #example message and key
    myMessage = 'Cenoonommstmme oo snnio. s s c'
    myKey = 8

    plaintext = decryptMessage(myKey, myMessage)
    print(plaintext) #output result

def decryptMessage(key, ciphertext):
    width = math.ceil(len(ciphertext)/key)
    height = key
    plaintext = ['']*width
    shadedboxes = (height*width) - len(ciphertext) #determine number of unused boxes
#pointer coordinates
    x = 0
    y = 0
    
    boxes_skipped = 0 #need this to adjust index accordingly

    while y < key - shadedboxes: #while there are no shaded boxes
        while x < width: # iterating horizontally
            debugger = width*y + x
            plaintext[x] += ciphertext[width*y + x]
            x += 1
        y += 1
        x = 0

    for i in range(shadedboxes): #final few rows containing nullspaces
        while x < width - 1: # iterating horizontally but SKIPPING nulls
                debugger = width*y + x
                plaintext[x] += ciphertext[width*y + x- boxes_skipped]
                x += 1
        boxes_skipped += 1 #this is to accommodate boxskip
        y += 1
        x = 0

        
    #OUTPUT total strings catted
    return ''.join(plaintext)

#if function is run as script, use default values
if __name__ == '__main__':
    main()
