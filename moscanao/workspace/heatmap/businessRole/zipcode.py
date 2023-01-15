from geopy.geocoders import Nominatim
from geopy.geocoders import GoogleV3
from . import map
def cep():

    # geolocator = Nominatim(user_agent="HEATMAP")
    geolocator = GoogleV3("AIzaSyCv11Ow__BGA0Yv7MmUZZQBg5StJoQLgcQ")
    geocodes = []

    location = geolocator.geocode("175 5th Avenue NYC")
    geocodes.append((location.latitude, location.latitude))
    location = geolocator.geocode("Pavilhão João Calmon") 
    geocodes.append((location.latitude, location.latitude))
    location = geolocator.geocode("Quadra 101 Conjunto 14, Recanto das Emas, Brasilia")
    geocodes.append((location.latitude, location.latitude))

    return geocodes
    