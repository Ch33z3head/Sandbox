import folium
from IPython.display import display
import folium.map

# "latitude": 43.0393, "longitude": -87.90647,

map_cntr = [43.0393, -87.90647]
my_map = folium.Map(location=map_cntr,zoom_start=12)

folium.Marker(
     [43.0393, -87.90647],
     popup="Milwaukee",
     icon=folium.Icon(color="green", icon="info-sign")
).add_to(my_map)

display(my_map)