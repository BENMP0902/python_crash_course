# Bloque 1: Creando y usando una Clase(Ejercicios 9-1 a 9-3)
# Aqui aprendimos el "plano" básico: el método (__init__) el constructor
# y cómo crear instancias (onjetos reales).

# 9-1 Restaurante: El parárametro self es la clave: la forma en que el objeto se refiere a sí mismo.
class Restaurant:
    """Un modelo simple de un restaurante""" # Cadena de documentacion con la descripcion  de lo 
                                             # realizaran nuestras clases y/o métodos

    def __init__(self, restaurant_name, cuisine_type): # Contructor 
        """Atributos que describen el estado del objeto."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        # atributo agregado ejercicio 9-4
        self.number_served = 0 # Valor por defecto

    def describe_restaurant(self):
        """Muestra la descripcion del restaurante."""
        print(f"El restaurante {self.restaurant_name} sirve comida {self.cuisine_type}.")

    def open_restaurant(self):
        """Indica que el restaurant esta abierto y su tipo de comida."""
        print(f"El restaurant {self.restaurant_name} esta abierto y sirve comida estilo {self.cuisine_type}.")

    # Funciones extra del ejercicio 9-4 
    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, increment):
        self.number_served += increment

# Crear la instancia que obtendra los argumentos para luego imprimir sus valores
mi_restaurante = Restaurant("Sabores MLOps", "Italiana")
print(mi_restaurante.restaurant_name)
mi_restaurante.describe_restaurant()
mi_restaurante.open_restaurant()

# Ejercicio resuelto(
restaurant1 = Restaurant("Sushi House", "japonesa")
restaurant2 = Restaurant("El Taco Feliz", "mexicana")
restaurant3 = Restaurant("Burger Town", "americana")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()


# Bloque 2: Trabajando con clases e instancias (Ejercicios 9-4 y 9-5) Aqui aprendimos a cambiar los
# valores de los atributos y podemos hacerlo directamente o de una manera mas limpia usando métodos.
# 9-4 Personas servidas: Añadimos un atributo con valor por defecto y métodos para actualizarlo.

# Instancias 
restaurant = Restaurant("Data Burger", "Americana")
restaurant.set_number_served(10)
print(f"Personas atendidas al momento: {restaurant.number_served}")
restaurant.increment_number_served(5)
print(f"Total de personas atendidas: {restaurant.number_served}")

# Bloque 3:Herencia(Ekjercicios 9-6 a 9-9) La herencia permite crear una clase especializada
# a partir de una general. La clase hija herada todos los  atributos y métodos del padre.
# 9-6 Puesto de Helados: IceCreamStand es un típo de Restaurant

class IceCreamStand(Restaurant):
    """Respresenta un típo especifico de restaurante y definimos tipo predeterminada."""
    def __init__(self, restaurant_name, cuisine_type='helados'):
        """Inicializamos atributos de la clase padre."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vainilla', 'chocolate', 'fresa']

    def display_flavors(self):
        """Método que muestra los sabores disponibles."""
        print("Sabores disponibles: ")
        for flavor in self.flavors:
            print(f"- {flavor}")

# Creamos Instancia 
mi_puesto = IceCreamStand("Michoacanita :)")
mi_puesto.display_flavors()

