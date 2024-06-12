'''
Pig Latin - Pig Latin is a game of alterations played on the English language game. To create the Pig Latin form of an English word the initial consonant sound is transposed to the end of the word and an ay is affixed (Ex.: "banana" would yield anana-bay). Read Wikipedia for more information on rules.
'''

import random 

consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']

text = input('Enter a word or sentence: ').lower().split()

print(text)

for word in text:
	newword = ''
	if word[0] in consonants and word[1] not in consonants:
		newword = word+word[0]
		newword = newword[1::] +'ay'
		text[text.index(word)] = newword
	elif word[0] in consonants and word[1] in consonants:
		newword = word+word[0]+word[1]
		newword = newword[2::] +'ay'
		text[text.index(word)] = newword
	else:
		newword = word+random.choice(['hay','way','yay'])
		text[text.index(word)] = newword

print(' '.join(text))
