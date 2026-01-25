# Bloque 1: Creando y usando una Clase(Ejercicios 9-1 a 9-3)
# Aqui aprendimos el "plano" básico: el método (__init__) el constructor
# y cómo crear instancias (onjetos reales).

# 9-1 Restaurante: El parárametro self es la clave: la forma en que el objeto se refiere a sí mismo.
class Restaurant:
    """Un modelo simple de un restaurante""" # Cadena de documentacion con la descripcion  de lo 
                                             # realizaran nuestras clases y/o métodos

    def __init__(self, restaurant_name, cuisine_type): # Contructor 
        """Inicializa nombre y tipo de cocina."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        # atributo agregado ejercicio 9-4
        self.number_server = 0 # Valor por defecto

    def describe_restaurant(self):
        """Muestra la descripcion del restaurante."""
        print(f"El restaurante {self.restaurant_name} sirve comida {self.cuisine_type}.")

    def open_restaurant(self):
        """Indica que el restaurant esta abierto."""
        print(f"El restaurant {self.restaurant_name} esta abierto.")

    # Funciones extra del ejercicio 9-4 
    def set_number_served(self, number_served):
        self.set_number_served = number_served

    def increment_number_served(self, increment_number_served):
        self.increment_number_served = increment_number_served

# Crear la instancia que obtendra los argumentos para luego imprimir sus valores
mi_restaurante = Restaurant("Sabores MLOps", "Italiana")
print(mi_restaurante.restaurant_name)
mi_restaurante.describe_restaurant()
mi_restaurante.open_restaurant()

# Bloque 2: Trabajando con clases e instancias (Ejercicios 9-4 y 9-5) Aqui aprendimos a cambiar los
# valores de los atributos y podemos hacerlo directamente o de una manera mas limpia usando métodos.
# 9-4 Personas servidas: Añadimos un atributo con valor por defecto y métodos para actualizarlo.

# Instancias 
restaurante = Restaurant("Data Burger", "Americana")
restaurante.set_number_served(50)
restaurante.increment_number_served(25)
print(f"Personas servidas: {restaurante.increment_number_served}")