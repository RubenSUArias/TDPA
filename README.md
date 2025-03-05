# Análisis de flujo vehicular con k-means
El flujo vehicular es registrado y reportado por el Instituto Mexicano del Transporte, como datos públicos. 
En el presente trabajo, se analizan dichos datos para identificar clusters de comportamiento sil¡milar en los patrones de flujo vehicular. 

# Contenido 
-Archivo TDPA.py con todo el proceso de análisis en python. 
-Registro de flujo vehicular
# Proceso 

- Lectura de datos
- Limpieza (encontrar outliers, y homologar a enteros los datos)
- Seleccionar columnas y estandarizar
- Evaluar la cantidad de clusters óptimos
- Entrenar el modelo
- Evaluar
- Visualizar resultados

# Resultados 
Se encontró una cantidad considerable de datos erroneos en los registros de latitud y longitud por estar invertidos sus valores, los cuales se corrigieron. 
La cantidad óptima de clusters es de dos. 
Al visualizar los datos, se identifica que una de las categorías se corresponde a corredores viales de importancia comercial y la otra a carreteras de menor flujo mercante. 


