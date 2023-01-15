# import folium
# import numpy as np
# from folium.plugins import HeatMap
# import pandas as pd

# #Retorna mapa populado
# def buildMap(geocodes):

#     dados = np.matrix(geocodes)
#     dfa = pd.DataFrame(dados)

#     # mapa = folium.Map([-15.762507, -47.869977], zoom_start = 3, tiles = "cartodbpositron")
#     mapa = folium.Map([0,0], zoom_start = 3, tiles = "cartodbpositron")

#     HeatMap(dfa).add_to(mapa)
#     return mapa
