'''
Check if Palindrome - Checks if the string entered by the user is a palindrome. That is that it reads the same forwards as backwards like “racecar”
'''

text = input('Enter a word or sentence: ').lower()

if text == text[::-1]:
	print("Yes this is a palindrome")
else:
	print("No this is not a palindrome")