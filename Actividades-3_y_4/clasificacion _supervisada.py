import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Cargar dataset de transporte masivo
data = pd.read_csv(r'Actividades-3_y_4/dataset.csv')  # Ruta del DataSet

# Seleccionar variables predictoras (características) y la variable objetivo
X = data[['tiempo_viaje', 'numero_pasajeros', 'costo_operativo']]  # Ajusta según el dataset
y = data['ruta_eficiente']  # 1 si es eficiente, 0 si no lo es

# Dividir los datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el modelo de Árbol de Decisión
clf = DecisionTreeClassifier()

# Entrenar el modelo
clf.fit(X_train, y_train)

# Predecir los resultados en el conjunto de prueba
y_pred = clf.predict(X_test)

# Evaluar el modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Precisión del modelo: {accuracy * 100:.2f}%')

# Ejemplo de predicción
nueva_ruta = [[45, 200, 5000]]  # Ejemplo de una nueva ruta con tiempo, pasajeros y costo
prediccion = clf.predict(nueva_ruta)
print(f'La nueva ruta es {"eficiente" if prediccion[0] == 1 else "ineficiente"}')
