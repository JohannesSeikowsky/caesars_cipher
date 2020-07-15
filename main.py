""" Caesars Cipher Encryption

Caesars Cipher is an easy way to encryt messages.
The system is based on having one specific numerical 
encryption key which could be any whole number.

Each letter in the message which is to be
encrypted will then be replaced by the letter which
is that many letters "down" the alphabet.

So for instance encrypting the letter "A" with an
encryption key of 3 would result in a "D". This 
simple procedure is then applied to each letter of 
the message using the encryption key that has been
chosen.

The code below implements two functions - one that 
encrypts individual characters in this fashion. And 
another that encrypts pieces of text.
"""


import string
import random


alphabet_lower = string.ascii_lowercase
alphabet_upper = string.ascii_uppercase
alphabet = alphabet_lower + alphabet_upper


def caesar_encrypt_char(alphabet, char, encrypt_key):
	""" Encrypt a single character according to the Caesars cipher system.
	Pass in lower or uppercase alphabets to maintain the case-sensitivity 
	of the encryption. 
	"""
	char_index = alphabet.index(char)
	encrypted_index = char_index + encrypt_key

	# Start at the "beginning" if the encrypted character would be 
	# "beyond" the end of the alphabet.
	if encrypted_index > len(alphabet)-1:
		encrypted_index = encrypted_index % len(alphabet)

	encrypted_char = alphabet[encrypted_index]
	return encrypted_char


def caesar_encrypt_text(text, encrypt_key):
	""" Encrypt a text according to the Caesars cipher system by encrypting 
	each character individually and appending it to the encryption.
	"""
	encrypted_text = ""
	for char in text:
		if char in alphabet_lower:
			encrypted_text += caesar_encrypt_char(alphabet_lower, char, encrypt_key)

		if char in alphabet_upper: 
			encrypted_text += caesar_encrypt_char(alphabet_upper, char, encrypt_key)

		if char not in alphabet:
			encrypted_text += char
	return encrypted_text


# Use
plain_text = input("Text to encrypt:\n")
encrypt_key = int(input("Caesars Cipher Encryption Key:\n"))
encrypted_text = caesar_encrypt_text(plain_text, encrypt_key)
print(encrypted_text)
