# Bloque 1: Definicion y Argumentos (8-1 a 8-5)
# Parametros vs Argumentos
#       Parametros: La variable que se define en la funcion (ej. titulo en def libro(titulo)):).
#       Argumentos: El valor real que envias (ej. "Alice" en libro("Alice")).

#8-1. Mensaje y 8-2. Libro Favorito:
# Definicion simple
def display_message():
    """Muestra una oracion simple sobre lo que estoy aprendiendo."""
    print("En este capítulo estoy aprendiendo sobre funciones en Python.")

# Pasando informacion (un parámetro)
def favorite_book(title):
    """Muestro un mensaje sobre uno de mis libros favoritos."""
    print(f"Uno de mis libros favoritos es {title}.")

# Llamadas a funciones
display_message()
favorite_book("python crash course")

# 8-3 Camisetas(Argumentos Posicionales vs Keyword):
def make_shirt(size, message):
    """Resumen de la talla y el mensaje de la camiseta."""
    print(f"\nVoy a hacer una camíseta talla {size}.")
    print(f"Llevará estampado el mensaje: '{message}.")

# 1. Argumentos Posicionales (El orden importa: primera talla, luego mensaje)
make_shirt('L','I Love Python')

# 2. Argumenso de Palabra Clave (El orden No importa)
make_shirt(message='Code Is Life', size='S')