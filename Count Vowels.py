'''
Count Vowels - Enter a string and the program counts the number of vowels in the text. For added complexity have it report a sum of each vowel found(???).
'''

vowels = ['a','e','i','o','u']

text = input('Enter a word or sentence: ').lower()

numvowels = 0
# sumvowels = 0

for letter in text:
	if letter in vowels:
		numvowels += 1

print(numvowels) 
