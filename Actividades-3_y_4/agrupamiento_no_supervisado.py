import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Cargar dataset de transporte masivo
data = pd.read_csv(r'Actividades-3_y_4/dataset.csv')  # Ruta del DataSet

# Verificar las columnas disponibles
print(data.columns)

# Seleccionar las características que se usarán para el agrupamiento
X = data[['numero_pasajeros', 'tiempo_viaje', 'horas_pico']]  # Ajusta según el dataset

# Crear el modelo K-means
kmeans = KMeans(n_clusters=3)

# Entrenar el modelo
kmeans.fit(X)

# Obtener los clusters asignados
data['cluster'] = kmeans.labels_

# Imprimir resultados
print("Clústeres asignados a cada ruta:")
print(data[['nombre_ruta', 'cluster']])  # Asegúrate de usar el nombre correcto
