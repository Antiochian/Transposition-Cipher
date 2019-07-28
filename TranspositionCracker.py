
import TranspositionCipherDecrypt, detectEnglish #import required dependencies

def main():
    myMessage = input("Input message to be cracked, or press enter for example input:\n")
    if myMessage == "":
        #example message (text taken from Charles Babbage's wikipedia page, encrypted with a key of 10
        myMessage = """Cb b rssti aieih rooaopbrtnsceee er es no npfgcwu  plri ch nitaalr eiuengiteehb(e1  hilincegeoamn fubehgtarndcstudmd nM eu eacBoltaeteeoinebcdkyremdteghn.aa2r81a condari fmps" tad   l t oisn sit u1rnd stara nvhn fsedbh ee,n  e necrg6  8nmisv l nc muiftegiitm tutmg cm shSs9fcie ebintcaets h  aihda cctrhe ele 1O7 aaoem waoaatdahretnhechaopnooeapece9etfncdbgsoeb uuteitgna.rteoh add e,D7c1Etnpneehtn beete" evecoal lsfmcrl iu1cifgo ai. sl1rchdnheev sh meBd ies e9t)nh,htcnoecplrrh ,ide hmtlme. pheaLem,toeinfgn t e9yce da' eN eMp a ffn Fc1o ge eohg dere.eec s nfap yox hla yon. lnrnsreaBoa t,e eitsw il ulpbdofgBRe bwlmprraio po  droB wtinue r Pieno nc ayieeto'lulcih sfnc  ownaSserbereiaSm-eaiah, nnrttgcC  maciiritvledastinideI  nn rms iehn tsigaBmuoetcetias rn"""
        print("Function called without argument.\nCracking example input:\n%s\n" % (myMessage))
        crackTransposition(myMessage)
    else:
        crackTransposition(myMessage)

def crackTransposition(message): #main function
    
    for key in range(1,len(message)): #try every possible key from 1 to the message length
        
        result = TranspositionCipherDecrypt.decryptMessage(key, message) #decrypt with this key
        
        if detectEnglish.isEnglish(result): #call "isEnglish" function
            
            print("Possible match for key = %s:\n%s" % (key,result))
            decision = input("Keep looking? (Y/N): \n")
            if decision == "N" or decision == "n": #make case-insensitive
                print("Program exited successfully.\n")
                return
            print("Continuing...\n")

    print("Cracking attempt finished.\n")
            
if __name__ == "__main__":
    main()
        
