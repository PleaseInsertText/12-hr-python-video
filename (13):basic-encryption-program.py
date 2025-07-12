import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)

key = chars.copy() #key = chars[:] would also work
random.shuffle(key)


print(f"CHARACTERS: {chars}")
print(f"KEY       : {key}")

#Encryption:
plain_text = input("\nEnter a message to encrypt: ")
print()
cipher_text = ""

for letter in plain_text:

    index = chars.index(letter)
    cipher_text += key[index]

print(f"ORIGINAL MESSAGE: {plain_text}")
print(f"ENCRYPTED MESSAGE: {cipher_text}")