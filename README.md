# Transposition-Cipher
# ANTIOCHIAN // 2k19
                                                  
A basic suite of programs for encrypting, decrypting and testing a Columnar Transposition Cipher.
https://en.wikipedia.org/wiki/Transposition_cipher#Columnar_transposition 

  ----------------------
  TranspositionCipher.py
  ----------------------
  When the contained function encryptMessage(key, message) is called, this script translations a given "message" string according to a transposition cipher using the columnar method with a given "key" integer.

  If the script is run on its own, it does the same but with a hardcoded example message and key.

  -----------------------------
  TranspositionCipherDecrypt.py
  -----------------------------
  This program works the same but in reverse, and contains the decryptMessage(key,message) function.

  --------------------
  TranspositionTest.py
  --------------------
  This is a simple testing script that generates 15 random messages of 104-1,040 characters before comparing the above two scripts  to ensure consistency.
