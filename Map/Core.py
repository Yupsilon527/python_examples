import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")

vgroup = folium.FeatureGroup(name = "Volcanoes")

def colorelevation(h):
    if h<1000:
        return "green"
    elif h>=3000:
        return "red"
    else:
        return "orange"



for lat,lon,elev in zip(data["LAT"],data["LON"], data["ELEV"]):
    
    vgroup.add_child(folium.CircleMarker(
        location = (lat,lon),
        radius = 6,
        popup = str(elev)+"m",
        color= "grey",
        fill_color=colorelevation(elev),
        fill_opacity=0.75
    ))

bgroup = folium.FeatureGroup(name = "Borders")
bgroup.add_child(folium.GeoJson(data = open("world.json","r",encoding="utf-8-sig").read()))

map = folium.Map(location = (37.13,-113.51),zoom_start = 6)
map.add_child(bgroup)
map.add_child(vgroup)
map.add_child(folium.LayerControl())
map.save("output.html")

print("Success!")