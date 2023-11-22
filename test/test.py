import string
import random


def substitution(plaintext):
    LETTERS = [*range(26)] #Number range respresting
    print(LETTERS)
    random.shuffle(LETTERS)
    print(LETTERS)
    cipher = plaintext.upper()
    print(cipher)
    
    for i in range(26):
        pt = chr(65+i) #chr(97 = 'A')
        #print('PT: ',pt, ' i:',i)
        print('PT: ',pt, 'letter from key: ',chr(65+LETTERS[i]))
        cipher = cipher.replace(pt, chr(65+LETTERS[i])) #chr(97 = 'z')
        print(cipher)
    return cipher,LETTERS

plaintext = 'Go confidently in the direction of your dreams Live the life youve imagined Henry David Thoreau'

'''
def dec_substitution(ctext, key):
    print(LETTERS)
    cipher = plaintext.upper()
    print(cipher)
    
    for i in range(26):
        pt = chr(65+i) #chr(97 = 'A')
        #print('PT: ',pt, ' i:',i)
        print('PT: ',pt, 'letter from key: ',chr(65+LETTERS[i]))
        cipher = cipher.replace(pt, chr(65+LETTERS[i])) #chr(97 = 'z')
        print(cipher)
    return cipher,LETTERS
'''

(ct,ltrs) = substitution(plaintext)
print(ct, ltrs)
