# - folium 모듈 이용
import folium
# 35.94717219388294, 126.97112874673742
umap = folium.Map(location=[35.94717219388294, 126.97112874673742], zoom_start=11)

folium.Marker(location=[35.94717219388294, 126.97112874673742], icon=folium.Icon(color='red'), 
popup='우리집').add_to(umap)

umap.save('./multi/0713/우리집.html')