import re
import string
import random


def pass_strength(password):
	if len(password)<8:
		return "Weak Password. Use a password with at least 8 characters"
	if not re.search("[A-Z]",password):
		return "Weak Password. Please add in one capital letter in your password"
	if not re.search("[a-z]",password):
		return "Weak Password. Please add in one lowercase letter in your password"
	if not re.search("[0-9]",password):
		return "Weak Password. Please add in one number in your password"
	if not re.search("[!@#$%&^*~]",password):
		return "Weak Password. Please add in one special character in your password"
	return "Strong Password"

def generate_pass():
	char_pool = string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits
	password = ""

	for x in range(13):
		password = password + random.choice(char_pool)

	return password

user_input = input("Enter a password to check how strong it is: ")
print(pass_strength(user_input))
user_input1= input("Would you like to generate a new password?")
if user_input1.upper() == "YES" or user_input1.upper() == "Y":
	print("Your new password is:", generate_pass())  