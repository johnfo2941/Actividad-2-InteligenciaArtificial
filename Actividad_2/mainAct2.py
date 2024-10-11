import heapq  # Importa la librería heapq, que proporciona una cola de prioridad eficiente.

# Definir el grafo del sistema de transporte masivo
class Grafo:
    def __init__(self):
        self.nodos = {}  # Diccionario que contendrá los nodos y sus conexiones.
    
    def agregar_nodo(self, nombre):
        self.nodos[nombre] = {}  # Añade un nodo al grafo con un diccionario vacío para sus conexiones.
    
    def agregar_arista(self, desde, hacia, peso):
        # Añade una conexión (arista) con un peso entre dos nodos en ambas direcciones (bidireccional).
        self.nodos[desde][hacia] = peso
        self.nodos[hacia][desde] = peso  # Si es bidireccional.

# Algoritmo de Dijkstra para encontrar la ruta más corta
def dijkstra(grafo, inicio, fin):
    # Inicializa una cola de prioridad con la distancia al nodo inicial (0, inicio).
    cola_prioridad = [(0, inicio)]
    # Diccionario que guarda las distancias más cortas conocidas desde el nodo inicial.
    distancias = {nodo: float('inf') for nodo in grafo.nodos}  # Inicialmente, todas las distancias son infinitas.
    distancias[inicio] = 0  # La distancia del nodo inicial a sí mismo es 0.
    # Diccionario para almacenar el camino más corto hacia cada nodo.
    camino = {nodo: None for nodo in grafo.nodos}  # Inicialmente, no hay camino conocido.

    while cola_prioridad:
        # Extrae el nodo con la menor distancia de la cola de prioridad.
        (distancia_actual, nodo_actual) = heapq.heappop(cola_prioridad)
        
        if nodo_actual == fin:
            break  # Si llegamos al nodo de destino, terminamos.

        # Explorar los vecinos del nodo actual.
        for vecino, peso in grafo.nodos[nodo_actual].items():
            distancia = distancia_actual + peso  # Calcula la distancia a través del nodo actual.
            if distancia < distancias[vecino]:  # Si es una mejor ruta, actualiza la distancia y el camino.
                distancias[vecino] = distancia
                camino[vecino] = nodo_actual  # Marca de dónde venimos.
                # Añade el vecino con la nueva distancia a la cola de prioridad.
                heapq.heappush(cola_prioridad, (distancia, vecino))
    
    # Reconstruir la ruta desde el nodo final al inicial.
    ruta = []
    nodo = fin
    while nodo is not None:
        ruta.append(nodo)  # Añade el nodo a la ruta.
        nodo = camino[nodo]  # Retrocede en el camino.
    ruta.reverse()  # Invertir la ruta para que vaya del inicio al fin.
    
    return ruta, distancias[fin]  # Devuelve la ruta y la distancia mínima.

# Crear el grafo del sistema de transporte
grafo = Grafo()
grafo.agregar_nodo("A")  # Añadir nodo A.
grafo.agregar_nodo("B")  # Añadir nodo B.
grafo.agregar_nodo("C")  # Añadir nodo C.
grafo.agregar_nodo("D")  # Añadir nodo D.
grafo.agregar_arista("A", "B", 1)  # Añadir arista entre A y B con peso 1.
grafo.agregar_arista("B", "C", 2)  # Añadir arista entre B y C con peso 2.
grafo.agregar_arista("A", "C", 2)  # Añadir arista entre A y C con peso 2.
grafo.agregar_arista("C", "D", 1)  # Añadir arista entre C y D con peso 1.

# Encontrar la mejor ruta de A a D
ruta, distancia = dijkstra(grafo, "A", "D")  # Ejecuta el algoritmo de Dijkstra para encontrar la mejor ruta de A a D.
print(f"La mejor ruta de A a D es: {ruta} con una distancia de {distancia}")  # Imprime la ruta y la distancia.
