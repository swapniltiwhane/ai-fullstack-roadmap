#understand string and use inbuilt functions available for string in python
#1. how to write string
name = "swapnil"
middle_name = 'Pralhad'
last_name = '''Tiwhane'''
print(f"First name: {name}, Middle Name: {middle_name}, Last Name: {last_name}")

#2. check given string is palindrome or not
def is_palindrome(user_string):
	if user_string.upper() == user_string[::-1].upper():
		print("Given string is palindrome")
	else:
		print("Given string is not palindrome")
user_input = input("Enter string to check: ")
is_palindrome(user_input);

#3. count vowels in string
vowels = 'aeiou'
def count_voawels(string):
	totalVoawels = 0;
	uniqueVowel=[];
	for item in string.lower():
		if(item in vowels and item not in uniqueVowel):
			uniqueVowel.append(item);
			totalVoawels +=1
	print(f"total vowels: {totalVoawels}")
	
count_voawels('ajabGajabKahani')

#4. check given password is strong or not
def checkPasswordStrength(password):
	password_length = len(password);
	if(password_length <8):
		print("password should have 8 or more character")
	elif(password_length >20):
		print("password should not be greater than 20 character")
	elif('password' in password.lower()):
		print("Password should not contain word password")
	elif not any(char.isdigit() for char in password):
		print("password much have atleast 1 numeric value")
	elif not any(char in '@#$%' for char in password):
		print("password much have atleast 1 special character from @#$%")
	elif(" " in password):
		print("password should not have space")
	else:
		print("Your password is strong")

user_password = input("Enter your password: ").strip()
checkPasswordStrength(user_password)

#5. Prompt formater
prompts = [
    "Explain Docker",
    "Teach me Python",
    "Create Angular Interview Questions",
    "Summarize AWS Bedrock"
]
def display_prompts():
	i = 0
	for ai_prompt in prompts:
		i += 1
		print(f"Prompt {i}. : {ai_prompt}")	