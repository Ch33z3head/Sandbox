from PIL import Image
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


#img= Image.open('C:\cygwin64\home\Jamie\Crypto\Mod 3\Org.jpg')
img= Image.open('F:\Crypto\Org.jpg')

imgData = img.tobytes()


key = 'Jags will choke!'

# iv genterated from os.urandom(16)
iv= b'9\xb3>\xca\x14\xe0\xb5\xb9~\xeb\xff\x92%\xde\xf14'  

''' Encrypt/Decryption Modes
ECB
OFB
CBC
'''

def encrypt_image(in_mode):
    mode = (in_mode)
    
    if mode =='ECB':
        cipher = AES.new(key.encode('utf8'), AES.MODE_ECB)
    elif mode == 'OFB':
        cipher = AES.new(key.encode('utf8'), AES.MODE_OFB, iv)
    elif mode == 'CBC':
        cipher = AES.new(key.encode('utf8'), AES.MODE_OFB, iv)
    else:
        print("Encryption Failed.")
 
    ct = cipher.decrypt(imgData)
    enc_img.frombytes(ct)
    enc_img.save("F:\Crypto\enc_Org.jpg")
    print(mode + " encyption of your image has been completed.")
return enc_image

def decrypt(in_mode):


#Print("Endter encrytpion mode (ECB, OFB, CBC)")

usr_input = input('Please enter encrytpion mode (ECB, OFB, CBC): ').upper()

if usr_input== 'ECB':
    in_mode = usr_input
elif usr_input == 'OFB':
    in_mode = usr_input
elif usr_input == 'CBC':
    in_mode = usr_input
else:
    print('Please enter one of the three mode.')

encrypt_image(in_mode)
    