import random, sys, math, TranspositionCipher, TranspositionCipherDecrypt

def main():
    random.seed(42)

    for i in range(15): #run 15 tests
        message = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"*random.randint(4,40)

        message = list(message)
        random.shuffle(message)
        message = ''.join(message)

        print("Test #%s: %s..." % (i+1, message[:20]))

        for key in range(1,math.ceil(len(message)/2)): #test all possible keys 
            ciphertext = TranspositionCipher.encryptMessage(key,message)
            plaintext = TranspositionCipherDecrypt.decryptMessage(key,ciphertext)

            if plaintext != message:
                print("ERROR // Test #%s using key #%s failed!" % (i+1,key))
                print("Message reads: %s" % (message))
                print("Decryption reads: %s" % (plaintext))
                sys.exit(0)

    print("Test passed.")
                
if __name__ == "__main__":
    main()
