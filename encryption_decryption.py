import string

chars = list(string.printable)
encrypt_dict = {}
decrypt_dict = {}

def encrypt_decrypt_codes():
	i = 0
	while i < (len(chars)):
		encrypt_dict[chars[i]] = i
		decrypt_dict[i] = chars[i]
		i = i + 1

def encrypt():
	message = raw_input("Enter your secret message? > ")
	for i in message: 
		if i = encrypt_dict[i]
	return encrypt_dict[i]
	print encrypt_dict[i]

def decrypt():
	message = raw_input("Enter the message you'd like to decrypt? > ")

# def test():

# def readfile():

# def writefile():

encrypt_decrypt_codes()
encrypt()
decrypt()

print encrypt_dict
print decrypt_dict