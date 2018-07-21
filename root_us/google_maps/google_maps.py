import os
import googlemaps


GOOGLE_MAPS_API_KEY = os.environ.get('GOOGLE_MAPS')
print(GOOGLE_MAPS_API_KEY)

gmaps_client = googlemaps.Client(key=GOOGLE_MAPS_API_KEY)



