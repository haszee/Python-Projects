'''
Collatz Conjecture - Start with a number n > 1. Find the number of steps it takes to reach one using the following process: If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.
'''

# while True:
# 	try:
# 		number = int(input('Enter a number greater than 1: '))
# 		assert number > 1
# 		break
# 	except:
# 		print('Wrong number')

# # USING RECURSION
# def collatz(number,count = 0):
#     if number == 1:
#         return count
#     if number%2 == 0:
#         return collatz(number/2,count+1)   
#     else:
#         return collatz(number*3+1,count+1)

# count = collatz(number)

# USING WHILE LOOP
# count = 0

# while number != 1:
# 	if number%2 == 0:
# 		number /= 2
# 	else:
# 		number = 3*number + 1
# 	print(number)
# 	count += 1

# print(count)

#---------------------------------------------------------------------------

'''
Sorting - Implement two types of sorting algorithms: Merge sort and bubble sort.
'''

# import random

# mylist = []
# for i in range(10):
# 	mylist.append(random.randint(0,100))

# print(mylist)

# def mergesort(mylist):
# 	if len(mylist) == 1:
# 		return mylist
# 	else:
# 		midlist1 = mylist[:int(len(mylist)/2)]
# 		midlist2 = mylist[int(len(mylist)/2):]

# 		sublist1 = mergesort(midlist1)
# 		sublist2 = mergesort(midlist2)

# 		i = 0 # iterator for sublist1
# 		j = 0 # iterator for sublist2
# 		k = 0 # iterator for inserting at current position of mylist

# 		while i<len(sublist1) and j<len(sublist2):
# 			if sublist1[i] < sublist2[j]:
# 				mylist[k] = sublist1[i]
# 				i += 1
# 			else:
# 				mylist[k] = sublist2[j]
# 				j += 1
# 			k += 1 

# 		# add any remaining elements
# 		while i < len(sublist1):
# 			mylist[k] = sublist1[i]
# 			i += 1
# 			k += 1

# 		while j < len(sublist2):
# 			mylist[k] = sublist2[j]
# 			j += 1
# 			k += 1
		
# 		return mylist

# print(mergesort(mylist))

# def bubblesort(mylist):
# 	for i in range(len(mylist)):
# 		swapped = False
# 		for j in range(0,len(mylist)-1):
# 			if mylist[j] > mylist[j+1]:
# 				mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
# 				swapped = True
# 		if not swapped:
# 			return mylist

# print(bubblesort(mylist))


#---------------------------------------------------------------------------

'''
Closest pair problem - The closest pair of points problem or closest pair problem is a problem of computational geometry: given n points in metric space, find a pair of points with the smallest distance between them.
'''

# pointlist = []

# while True:
# 	coor = input('Enter x & y coordinates of point as x,y: ').split(',')
# 	pointlist.append(coor)
# 	addmore = input('Do you wish to add more (y or n): ')
# 	if addmore == 'n':
# 		break
# 	else:
# 		continue

# dictlist = {}
# for i in range(len(pointlist)):
# 	dictlist[i+1] = pointlist[i]

# print(dictlist)

# dsmallest = 0
# pairsmallest = []

# for i in range(0,len(dictlist)-1):
# 	x1 = int(dictlist[i+1][0])
# 	y1 = int(dictlist[i+1][1])

# 	x2 = int(dictlist[i+2][0])
# 	y2 = int(dictlist[i+2][1])

# 	print(x1,y1)
# 	print(x2,y2)
# 	d = round(((x1-x2)**2 + (y1-y2)**2)**0.5,2)
	
# 	print(d)

# 	keys = list(dictlist.keys())
# 	print(keys)

# 	if dsmallest == 0 or dsmallest == d:
# 		dsmallest = d

# 		pairsmallest.append([keys[i],keys[i+1]])
# 	elif d < dsmallest:
# 		dsmallest = d
# 		pairsmallest = []
# 		pairsmallest.append([keys[i],keys[i+1]])			

# print('Smallest distance:',dsmallest)
# print('Smallest pair(s) of points:',pairsmallest)

#---------------------------------------------------------------------------

'''
Sieve of Eratosthenes - The sieve of Eratosthenes is one of the most efficient ways to find all of the smaller primes (below 10 million or so).
'''

# n = int(input('Enter an integer: '))

# def sieve(n):
# 	primelist = [True for i in range(n+1)]
# 	pos = 2 # both index position & corresponding number

# 	while pos*pos <= n:
# 		if primelist[pos] == True:
# 			for i in range(pos*pos,n+1,pos):
# 				primelist[i] = False
# 		pos += 1

# 	for i in range(2,n+1):
# 		if primelist[i]:
# 			print(i)

# sieve(n)


