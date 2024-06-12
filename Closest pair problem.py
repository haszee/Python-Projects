'''
Closest pair problem - The closest pair of points problem or closest pair problem is a problem of computational geometry: given n points in metric space, find a pair of points with the smallest distance between them.
'''

pointlist = []

while True:
	coor = input('Enter x & y coordinates of point as x,y: ').split(',')
	pointlist.append(coor)
	addmore = input('Do you wish to add more (y or n): ')
	if addmore == 'n':
		break
	else:
		continue

dictlist = {}
for i in range(len(pointlist)):
	dictlist[i+1] = pointlist[i]

print(dictlist)

dsmallest = 0
pairsmallest = []

for i in range(0,len(dictlist)-1):
	x1 = int(dictlist[i+1][0])
	y1 = int(dictlist[i+1][1])

	x2 = int(dictlist[i+2][0])
	y2 = int(dictlist[i+2][1])

	print(x1,y1)
	print(x2,y2)
	d = round(((x1-x2)**2 + (y1-y2)**2)**0.5,2)
	
	print(d)

	keys = list(dictlist.keys())
	print(keys)

	if dsmallest == 0 or dsmallest == d:
		dsmallest = d

		pairsmallest.append([keys[i],keys[i+1]])
	elif d < dsmallest:
		dsmallest = d
		pairsmallest = []
		pairsmallest.append([keys[i],keys[i+1]])			

print('Smallest distance:',dsmallest)
print('Smallest pair(s) of points:',pairsmallest)