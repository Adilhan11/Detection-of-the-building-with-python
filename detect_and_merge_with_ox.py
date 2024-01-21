import osmnx as ox
import matplotlib.pyplot as plt
import warnings 
import pandas as pd
warnings.filterwarnings("ignore")

place_name = "Yukarı Bahçelievler Mahallesi, Çankaya, Ankara"

# Fetch OSM street network from the location
graph = ox.graph_from_place(place_name)

type(graph)

# Plot the streets
fig , ax = ox.plot_graph(graph)

# Retrieve nodes and edges
nodes , edges = ox.graph_to_gdfs(graph)

nodes.head()

edges.head()

# Get place boundary related to the place name as a geodataframe
area = ox.geocode_to_gdf(place_name)

# Check the data type
type(area)

# Plot the area:
area.plot(figsize=(12,8))

# List key-value pairs for tags
tags = {"building": True}

buildings = ox.geometries_from_place(place_name,tags)

len(buildings)

buildings.head()

print(buildings.columns)


# List key-value pairs for tags
tags2 =  {"amenity":"restaurant"}

# Retrieve restaurants
restaurants = ox.geometries_from_place(place_name,tags2)

# How many restaurants do we have?
len(restaurants)

# Available columns
restaurants.columns.values


fig, ax = plt.subplots(figsize=(12,8))

# Plot the footprint
area.plot(ax=ax,facecolor="yellow")

# Plot street edges
edges.plot(ax=ax,linewidth = 1,edgecolor="gray")


# Plot buildings
buildings.plot(ax=ax,facecolor="silver",alpha=0.6)

# Plot restaurants
restaurants.plot(ax=ax,facecolor="red",)


# List key-value pairs for tags
tags = {"leisure":"park","landuse":"grass"}


# Get the data
park = ox.geometries_from_place(place_name,tags)


# Check the result
park.head()

park.plot(color="green")


fig, ax = plt.subplots(figsize=(12,8))
# Plot the footprint
area.plot(ax=ax,facecolor="yellow")
# Plot street edges
edges.plot(ax=ax,linewidth = 1,edgecolor="gray")
# Plot buildings
buildings.plot(ax=ax,facecolor="silver",alpha=0.6)
# Plot restaurants
restaurants.plot(ax=ax,facecolor="red")
# Plot park
park.plot(ax = ax , facecolor="green")
plt.show()