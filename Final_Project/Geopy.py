from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent = "miroslawmamczur.pl")

adress = input(print('\nEnter the location you are looking for in the format (TheCity, 123 Somewhere Street).\n'))
location = geolocator.geocode(adress)
print(f'The coordinates for the indicated city {adress} are:{location}.')