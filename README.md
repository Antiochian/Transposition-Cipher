# Transposition-Cracker // 2k19
                                                  
A basic suite of programs for encrypting, decrypting and testing a Columnar Transposition Cipher.

https://en.wikipedia.org/wiki/Transposition_cipher#Columnar_transposition 

# HOW TO USE:

To brute-force crack a message with an unknown key, either run TranspositionCracker.py or call the function TranspositionCracker.crackTransposition("ciphertext").

Also included are a suite of related utilities pertaining to the transposition cipher, including an encrypter, decrypter, randomised tester and a crude programmatic english-language detection setup.

  TranspositionCracker.py
 ----------------------
 This script takes in any ciphertext message (no key required!) and attempts to brute force a solution in conjunction with an english dictionary file. 

  detectEnglish.py
  -----------------
  This script takes a plaintext message and compares it to a dictionary file to guess whether the plaintext is English or not. Contains two optional parameters to tweak sensitivity, which default at 20% of the words must be english, and 80% of the characters must be Latin.
  
 
  TranspositionCipher.py
  ----------------------
  This script encrypts a plaintext message into a transposition cipher with a known key.
  If the script is run on its own, it does the same but with a hardcoded example message and key.

  
  TranspositionCipherDecrypt.py
  -----------------------------
  This script decrypts ciphertext into a plaintext message with a known key.
  If the script is run on its own, it does the same but with a hardcoded example ciphertext and key.
  
 
  TranspositionTest.py
  --------------------
  This is a simple testing script that generates 15 random messages of 104-1,040 characters before comparing the above two scripts  to ensure consistency.
