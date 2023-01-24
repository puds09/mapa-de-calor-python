import numpy as np
import pandas as pd

from django.shortcuts import render, HttpResponse 
import folium
from folium.plugins import HeatMap
from geopy.geocoders import Nominatim


class Mapa:
    mapa = folium.Map([-15.762507, -47.869977], zoom_start = 8)
    # Para guardar o mapa em html
    mapa_renderizado = ""
    #  Para guardar as coordenadas
    global geocodes
    geocodes = []

    #Static known coordenates:
    #-------------------------
    # geocodes.append( (-15.76, -47.86) )
    # geocodes.append( (-15.76666, -47.8738) )
    # geocodes.append( (-15.76666, -47.8738) )
    # geocodes.append( (-15.76666, -47.8738) )
    # geocodes.append( (-15.76666, -47.8738) )
    # geocodes.append( (-15.76666, -47.8738) )
    # geocodes.append( (-15.76666, -47.8738) )
    # geocodes.append( (-15.755999, -47.870851 ) )
    # geocodes.append( (-15.760564, -47.466709 ) )
    # geocodes.append( (-15.760564, -47.466709 ) )
    # geocodes.append( (-15.760564, -47.466709 ) )

    def __init__(self):
        pass

    def cep(self,  request, local):
        geolocator = Nominatim(user_agent="HEATMAP")

        try:
            global geocodes
            location = geolocator.geocode(local)
            geocodes.append((location.latitude, location.longitude))
            return True
        except:
            return False


# formulário para inserir um novo foco de calor no mapa
def heat_form(request):
    return render(request, "heatmap/form.html")

# Find the coordenates and put its dataFrama on map
def get_data(request):
    
    # Initiating Mapa Class to take the static argument mapa
    mapa = Mapa()
    local = request.GET["local"]

    local_valido = mapa.cep(request, local)

    # Go to "Erro page"
    if not local_valido: 
        return render(request, "heatmap/erro.html")

    #else:
    # Retrieving coordenates 
    global geocodes

    # Retrieving the object map
    mapa = mapa.mapa

    # Structuring the data
    dados = np.matrix(geocodes)
    dfa = pd.DataFrame(dados)

    # Actually populating
    HeatMap(dfa).add_to(mapa)
    
    # Getting the static map to add to it the geocodes
    mapa_objeto = mapa
    
    # Retrieving "html map code"
    mapa_string = mapa_objeto._repr_html_()

    #Assigning the static Map.mapa_renderizado with the "html map code"
    mapa_objeto.mapa_renderizado = mapa_string 

    # Go to "Informações Enviadas com Sucesso - Veja mapa de calor"
    return render(request, "heatmap/response.html")


def modal_mapa(request):
    # Initiating Mapa Class to take the static argument mapa
    mapa = Mapa()
    
    mapa = mapa.mapa
    html_mapa = mapa.mapa_renderizado

    #Responsing actually the html code
    return HttpResponse(html_mapa)
