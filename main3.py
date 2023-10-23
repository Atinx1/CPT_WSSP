from OSMPythonTools.overpass import overpassQueryBuilder, Overpass
import numpy as np
from shapely.geometry import Polygon
import folium
import geopandas as gpd

# Define a bounding box
bbox = {'latLower':59.9,'lonLower':10.7,'latHigher':60.0,'lonHigher': 10.8}

# Use the Overpass API to query data
overpass = Overpass()
query = overpassQueryBuilder(bbox=[bbox['latLower'],bbox['lonLower'],bbox['latHigher'],bbox['lonHigher']],
                             elementType=['way', 'relation'],
                             selector='\"natural\"=\"water\"',
                             includeGeometry=True)
result = overpass.query(query)

# Define a shapely polygon for the bounding box
bbox_polygon_obj = Polygon(np.array([[bbox['lonLower'],bbox['latLower']],
                                     [bbox['lonLower'],bbox['latHigher']],
                                     [bbox['lonHigher'],bbox['latHigher']],
                                     [bbox['lonHigher'],bbox['latLower']]]))

# Plot the results
m = folium.Map(location=[0.5*(bbox['latLower']+bbox['latHigher']), 0.5*(bbox['lonLower']+bbox['lonHigher'])],
               zoom_start=12, tiles='CartoDB positron')

for each in result.ways():
    coord_pairs = np.array(each.geometry()['coordinates'][0])
    polygon_obj = Polygon(coord_pairs)
    geo_j = folium.GeoJson(data=gpd.GeoSeries(polygon_obj).to_json(), style_function=lambda x: {'fillColor': 'orange'})
    geo_j.add_to(m)

geo_j_bbox = folium.GeoJson(data=gpd.GeoSeries(bbox_polygon_obj).to_json(), style_function=lambda x: {'fillColor': 'red'})
geo_j_bbox.add_to(m)


