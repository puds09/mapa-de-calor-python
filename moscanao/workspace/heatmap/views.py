import os
import numpy as np
import pandas as pd

from .businessRole import zipcode
from .businessRole import map
from django.shortcuts import render, HttpResponse 
from django.views.decorators.csrf import csrf_protect
import folium
from folium.plugins import HeatMap
from geopy.geocoders import GoogleV3
from geopy.geocoders import Nominatim


class Mapa:
    mapa = folium.Map([-15.762507, -47.869977], zoom_start = 15)
    # mapa = folium.Map([0, 0], zoom_start = 15)
    global geocodes
    geocodes = []

    def __init__(self):
        pass

    def cep(self, local):
        # geolocator = Nominatim(user_agent="HEATMAP")
        geolocator = GoogleV3("AIzaSyCv11Ow__BGA0Yv7MmUZZQBg5StJoQLgcQ")

        # geocodes.append((-15.762507, -47.869977, 2))
        # location = geolocator.geocode("Universidade de Brasília, Brasília-DF, Brasil")
        try:
            location = geolocator.geocode(local)
            geocodes.append((location.latitude, location.latitude))
        except:
            pass

        # location = geolocator.geocode({"Florida, United States of America"})
        location = geolocator.geocode(components={"country": "BR", "state": "Distrito Federal"})
        print(location, "LLLLLLLLLLLLLLLL")
        print("em cima!!!!!!!!!!!!")
        geocodes.append((location.latitude, location.latitude))

        # location = geolocator.geocode("Pavilhão João Calmon") 
        # geocodes.append((location.latitude, location.latitude))

        print(geocodes)

        return geocodes


# formulário para inserir um novo foco de calor no mapa
def heat_form(request):
    return render(request, "heatmap/form.html")

def get_data(request):
    
    # Initiating Mapa Class to take the static argument mapa
    mapa = Mapa()

    local = request.GET["local"]
    # print(local)


    # Getting geocodes from form.html input
    geocodes = mapa.cep(local)
    # print(geocodes)

    mapa = mapa.mapa

    # Structuring the data
    dados = np.matrix(geocodes)
    dfa = pd.DataFrame(dados)

    print(dfa)

    # Actually populating
    HeatMap(dfa).add_to(mapa)

    return render(request, "heatmap/response.html")
    # return render(request, "heatmap/response.html", {"mapa_html": mapa_html})

@csrf_protect
def render_map(request):
    
    # Initiating Mapa Class to take the static argument mapa
    mapa = Mapa()
    # Getting the static mapa to add it the geocodes
    mapa = mapa.mapa

    mapa_html = mapa.save(os.path.join('workspace/heatmap/templates/heatmap', 'mapa_renderizado.html'))
    # mapa = mapa.get_root().render()
    # mapa_html_string = mapa.get_root().render()
    # mapa_html_string = mapa._repr_html_()
    # return mapa_html_string

    return render(request, "heatmap/mapa_renderizado.html")    


