import googlemaps from GoogleMaps
from sys import argv


gmaps = googlemaps.client(key = 'AIzaSyC07s4e51M2ztIyoRmyjt6Vb7ZNdCzwhB4')

my_distance = gmaps.distance_matrix(argv[1], argv[2])   #using distance matrix method from google map

print(my_distance);