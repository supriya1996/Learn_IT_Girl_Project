#Get Direction Script

from googlemaps import GoogleMaps
from HTMLparser import HTMLparser
from sys import argv


#Code for coverting direction text in readable form
class MLstripper(HTMLparser):
        def_init_(self):
		     self.reset()
			 self.fed = []
			 
		def handle_data(self,d):
		     self.fed.append(d)
	    def get_data(self):
		     return ''.join(self.fed)
			 
def strip_tags(html):
       s = MLstripper()
	   s.fed(html)
	   return s.getdata()
	  

#create Google map object

mapService = GoogleMaps()                              #mapservice will help in accessing function of GoogleMap Class



#get direction from Google 

directions = mapService.directions(argv[1], argv[2])        #using GoogleMap Method i.e Direction and passing argument



#Print each step in direction to Console 
with open('C:/Users/Supriya/Desktop/directions.txt','w') as f:
       for steps in directions['Directions']['Routes'][0] ['Steps']:
             f.write(print strip_tags(step['descriptionHtml'] + '\r\n'))

