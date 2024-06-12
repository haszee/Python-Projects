'''
Find Cost of Tile to Cover W x H Floor - Calculate the total cost of tile it would take to cover a floor plan of width and height, using a cost entered by the user.
'''

while True:
	try:
		price = float(input('Enter the cost of 1 tile: '))
		break
	except ValueError:
		print('Please enter a number that has decimal places')

while True:
	try:
		width = float(input('Enter the width of the floor: '))
		break
	except ValueError:
		print('Please enter a number that has decimal places')

while True:
	try:
		length = float(input('Enter the length of the floor: '))
		break
	except ValueError:
		print('Please enter a number that has decimal places')

# assume each tile is 1x1
area_tile = 1
area_floor = width * length

tile_cost = price/area_tile

floor_cost = tile_cost * area_floor

print(f'The total cost of tiles to cover an area (WxH) {width}x{length} is ${floor_cost}.')
