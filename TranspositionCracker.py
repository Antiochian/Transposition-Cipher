
import TranspositionCipherDecrypt, detectEnglish

def main():
    myMessage = """Cb b rssti aieih rooaopbrtnsceee er es no npfgcwu  plri ch nitaalr eiuengiteehb(e1  hilincegeoamn fubehgtarndcstudmd nM eu eacBoltaeteeoinebcdkyremdteghn.aa2r81a condari fmps" tad   l t oisn sit u1rnd stara nvhn fsedbh ee,n  e necrg6  8nmisv l nc muiftegiitm tutmg cm shSs9fcie ebintcaets h  aihda cctrhe ele 1O7 aaoem waoaatdahretnhechaopnooeapece9etfncdbgsoeb uuteitgna.rteoh add e,D7c1Etnpneehtn beete" evecoal lsfmcrl iu1cifgo ai. sl1rchdnheev sh meBd ies e9t)nh,htcnoecplrrh ,ide hmtlme. pheaLem,toeinfgn t e9yce da' eN eMp a ffn Fc1o ge eohg dere.eec s nfap yox hla yon. lnrnsreaBoa t,e eitsw il ulpbdofgBRe bwlmprraio po  droB wtinue r Pieno nc ayieeto'lulcih sfnc  ownaSserbereiaSm-eaiah, nnrttgcC  maciiritvledastinideI  nn rms iehn tsigaBmuoetcetias rn"""
 #myMessage = 'H itietseplh shlimteosy r,  c!'
    crackTransposition(myMessage)

def crackTransposition(message):
    score = {}
    for key in range(1,len(message)):
        result = TranspositionCipherDecrypt.decryptMessage(key, message)
        if detectEnglish.isEnglish(result):
            score[key] = result
            print("Possible match for key = %s:\n%s" % (key,result))
            decision = input("Continue? (Y/N): \n")
            if decision == "N" or decision == "n":
                return

    input("Cracking finished. No more matches found. Press any key...")
            
if __name__ == "__main__":
    main()
        
