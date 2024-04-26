'''
Inverted index - An Inverted Index is a data structure used to create full text search. Given a set of text files, implement a program to create an inverted index. Also create a user interface to do a search using that inverted index which returns a list of files that contain the query term / terms. The search index can be in memory.
'''

import re 
import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
ps = PorterStemmer()

def createindex(wordset,file,query):
	index = dict()
	foundword = dict()

	if query in wordset:
		index[file] = True
	else:
		index[file] = False


def stem(wordlist1):
	wordset = set()
	for word in wordlist1:
		wordlist.add(word)
		wordlist.add(ps.stem(word))
	return wordset

def searchword(filelist):
	query = input('Enter a search term: ').lower()

	for file in filelist:
		openfile = open(file)
		words = openfile.read().lower()
		wordlist1 = ''.join(re.findall(r'[^\!"#$%&\'()*+,-./:;<=>?@[\]^_`{}|~]+',words)).split()

		# nostopwords = [word for word in wordlist1 if not word in stopwords.words()]

		wordset = stem(wordlist1)	
		inverseindex = createindex(wordset,file,query)	

		# print(wordset)

	# 	if query in wordset:
	# 		print(f'{query} is found in {file}')

	# searchagain = input('Search another term? (y or n): ')
	# if searchagain == 'y':
	# 	searchword(filelist)
	# else:
	# 	return


if __name__ == '__main__':
	filelist = ['file1.txt', 'file2.txt', 'file3.txt']
	tokenlist = []
	searchword(filelist)


