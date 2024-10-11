import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Cargar dataset de transporte masivo
data = pd.read_csv(r'Actividades-3_y_4/dataset.csv')  # Ruta del DataSet

# Verificar las columnas disponibles
print("Columnas del DataFrame:", data.columns)

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

# Opcional: Visualizar los clusters (si solo hay dos dimensiones)
plt.scatter(data['numero_pasajeros'], data['tiempo_viaje'], c=data['cluster'])
plt.xlabel('Número de pasajeros')
plt.ylabel('Tiempo de viaje')
plt.title('Agrupamiento de rutas de transporte')
plt.show()

