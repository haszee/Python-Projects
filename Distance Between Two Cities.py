'''
Distance Between Two Cities - Calculates the distance between two cities and allows the user to specify a unit of distance. This program may require finding coordinates for the cities like latitude and longitude.
'''

from pygeocoder import Geocoder
import sys
from math import radians, sin, cos, sqrt, atan2


def get_distance(lat1, lon1, lat2, lon2):
	R = 6371  # Earth radius in kilometers
	dlat = radians(lat2 - lat1)
	dlon = radians(lon2 - lon1)
	a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
	c = 2 * atan2(sqrt(a), sqrt(1 - a))
	distance = R * c
	return distance

def main():
	city1 = input('Enter a city: ')
	city2 = input('Enter another city: ')
	units = input('Enter the units (kilometers(km) or miles(m)): ')

	city1_loc = Geocoder.geocode(city1)[0].coordinates
	city2_loc = Geocoder.geocode(city2)[0].coordinates

	print(city1_loc)
	print(city2_loc)


	print('The latitude of Edmonton is: ', location1.latitude)
	print('The longitude of Edmonton is: ', location1.longitude,'\n')

	print('The latitude of Calgary is: ', location2.latitude)
	print('The longitude of Calgary is: ', location2.longitude)

	distance = get_distance(location1.latitude,location1.longitude,location2.latitude,location2.longitude)

if __name__ == '__main__':
	sys.exit(main())