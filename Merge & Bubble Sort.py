
'''
Merge & Bubble Sort - Implement two types of sorting algorithms: Merge sort and bubble sort.
'''

import random

mylist = []
for i in range(10):
	mylist.append(random.randint(0,100))

print(mylist)

def mergesort(mylist):
	if len(mylist) == 1:
		return mylist
	else:
		midlist1 = mylist[:int(len(mylist)/2)]
		midlist2 = mylist[int(len(mylist)/2):]

		sublist1 = mergesort(midlist1)
		sublist2 = mergesort(midlist2)

		i = 0 # iterator for sublist1
		j = 0 # iterator for sublist2
		k = 0 # iterator for inserting at current position of mylist

		while i<len(sublist1) and j<len(sublist2):
			if sublist1[i] < sublist2[j]:
				mylist[k] = sublist1[i]
				i += 1
			else:
				mylist[k] = sublist2[j]
				j += 1
			k += 1 

		# add any remaining elements
		while i < len(sublist1):
			mylist[k] = sublist1[i]
			i += 1
			k += 1

		while j < len(sublist2):
			mylist[k] = sublist2[j]
			j += 1
			k += 1
		
		return mylist

print(mergesort(mylist))

def bubblesort(mylist):
	for i in range(len(mylist)):
		swapped = False
		for j in range(0,len(mylist)-1):
			if mylist[j] > mylist[j+1]:
				mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
				swapped = True
		if not swapped:
			return mylist

print(bubblesort(mylist))