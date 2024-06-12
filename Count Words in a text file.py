
'''
Count Words in a text file - Counts the number of individual words in a string. For added complexity read these strings in from a text file and generate a summary.
'''

f = open('file1.txt', 'r')

symbols =  '!|"''.,#=@$%^&*()<>{}[]:;~`-+/?'

numbers = '0123456789'

count = 0

words_list = f.read().split()

for word in words_list:
	if word in symbols or word[0] in numbers:
		pass
	else:
		count += 1

print(count)