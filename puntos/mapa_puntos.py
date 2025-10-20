import folium

ubicaciones = [
    {"nombre": "Caracas", "lat": 10.4806, "lng": -66.9036},
    {"nombre": "Maracaibo", "lat": 10.6545, "lng": -71.6519},
    {"nombre": "Valencia", "lat": 10.162, "lng": -68.0077}
]

mapa = folium.Map(location=[10.5, -66.9], zoom_start=6)

for u in ubicaciones:
    folium.Marker(
        location=[u["lat"], u["lng"]],
        popup=f"{u['nombre']}"
    ).add_to(mapa)

mapa.save("mapa_ubicaciones.html")

print("Mapa generado correctamente.")

