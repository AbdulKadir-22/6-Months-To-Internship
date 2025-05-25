import random
import string

chars = " " + string.punctuation + string.ascii_letters + string.digits
chars = list(chars)
key = chars.copy()
random.shuffle(key)

#Encryption Program 
plain_text = input("Enter your text: ")
Encrypted_text = ""

for letter in plain_text:
    index = chars.index(letter)
    Encrypted_text += key[index]

print(f"Your text is {Encrypted_text}")


#Decryption Program 
Encrypted_text = input("Enter the text you want to decrypt: ")
Decrypted_text = " "

for letter in Encrypted_text:
    index = key.index(letter)
    Decrypted_text += chars[index]

print(f"Your text is {Decrypted_text}")