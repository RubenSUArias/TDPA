"""Creado por Ruben Arias"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd
#Se lee la sabana de datos con los registros de flujo vehicular 
dviales=pd.read_csv("/content/drive/MyDrive/datos_viales/Datos_Viales.csv", encoding="latin-1")

#Se limpia la sabana de datos e identifican outliers en las coordenadas
#Outliers latitud
R=dviales[(-122>dviales['LONGITUD'])|(dviales['LONGITUD']>-85)|(13>dviales['LATITUD'])|(dviales['LATITUD']>34)|(dviales['LATITUD'].isnull())|(dviales['LONGITUD'].isnull())]
#Se construye un geodata frame con las coordenadas de los puntos
gdf = gpd.GeoDataFrame(R, geometry=gpd.points_from_xy(S['LATITUD'],R['LONGITUD']))
gdf.crs=4326
# importar las librerías necesarias para usar silhouette_score

from sklearn.metrics import silhouette_score
gdf.columns
entrenar=gdf[(gdf['Año']==2022)][['M', 'A', 'B', 'C2', 'C3', 'T3S2', 'T3S3', 'T3S2R4', 'Otros','A.1', 'B.1', 'C','D']]

# normalizar los datos de entrenar

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
entrenar_scal= scaler.fit_transform(entrenar)

# Regresar a data frame 
entrenar_scaled = pd.DataFrame(entrenar_scal, columns=entrenar.columns)

# Visualizar los datos
entrenar_scaled.head()

#  clasificar selected_columns en n clusters

from sklearn.cluster import KMeans
#from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
scaler.fit(entrenar)
features_std = scaler.transform(entrenar)

# Initialize the KMeans model with n_clusters=3

N=[]
Silhouette=[]
for i in range(2,10):
  kmeans = KMeans(n_clusters=i)

  # Fit the model to the selected columns
  model=kmeans.fit(features_std)

  # Get the cluster labels for each data point
  labels = kmeans.labels_

  # Print the cluster labels

  N.append(i)
  Silhouette.append(silhouette_score(features_std, labels))


#  imprimir N vs Silhouette

import matplotlib.pyplot as plt

plt.plot(N, Silhouette)
plt.xlabel('Number of clusters')
plt.ylabel('Silhouette score')
plt.show()

# KMeans model with n_clusters=2
##
N=[]
Silhouette=[]

kmeans = KMeans(n_clusters=2)

# entrenar el modelo con los datos 
model=kmeans.fit(features_std)

# obtener las columnas de cada uno
labels = kmeans.labels_

# 

N.append(i)
Silhouette.append(silhouette_score(features_std, labels))

new_observation=scaler.fit_transform(entrenar)

graficar=gdf[gdf['Año']==2022]
#Visualizar en folium
import matplotlib.pyplot as plt

# 
cmap = plt.cm.get_cmap('rainbow', len(set(labels)))

# 
graficar.explore(column='cluster', color=cmap)
