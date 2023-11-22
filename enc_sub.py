from string import ascii_lowercase
import string
import random

LETTERS = ascii_lowercase
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def genRanKey():
    ranKey = list(LETTERS.lower())
    random.shuffle(ranKey)
    key = ''.join(ranKey)
    print('Key d/t: ', type(key))
    return ''.join(ranKey)



def translateMessage(message, key, mode):
    translated = ''
    charsA = LETTERS
    charsB = key
    
    print('########BEFORE swapping')
    print('charsA (LETTERS)',charsA)
    print('charsB (KEY): ', charsB)
    
    # If decrypt mode is detected, swap A and B
    if mode == 'D':
        charsA, charsB = charsB, charsA
        print("swapped a , = b, a")
        
        print('########AFTER swapping')
        print('charsA (KEY)',charsA)
        print('charsB (LETTERS): ', charsB)
    
    for symbol in message:
        if symbol.upper() in charsA:
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            translated += symbol
    return translated, key, mode
         
         

mod = ''
message = 'Go confidently in the direction of your dreams Live the life youve imagined Henry David Thoreau'

mode = 'E'
key = genRanKey()
print(genRanKey())
(translated, enc_key, mode) = translateMessage(message, key, mode)
print("Cipher Tx: ", translated)
print("Encryption Key: ", enc_key)

######### DECRPTION
mode = 'D'
ct = message
message = ct
key = enc_key
print('CIPHER TXT: ', message)
(translated, enc_key, mode) = translateMessage(message, key, mode)
print("Plain Tx: ", translated)
print("Encryption Key: ", enc_key)


'''
mode = 'D'
message = 'Nc ecrohdqrpuy hr plq dhsqephcr co ycks dsqxbg! Uhmq plq uhoq yckmq hbxnhrqd. -Lqrsy Dxmhd Plcsqxk'
key = 'xfedqonlhzvubrcjwsgpkmitya'

   
(enc_ranslated, enc_key, mode) = translateMessage(message, mode, key)

(dec_ranslated, enc_key, mode) = translateMessage(message, mode, key)
'''