# Bloque 2: Escritura de Archivos(10-4 y 10-5)
# Pedir un nombre y guardarlo en un archivo.
from pathlib import Path

path = Path('guest.txt')

name = input("Por favor, introduce tu nombre: ")

# Escribimos texto en el archivo (sobreescribe si el archivo ya existe)
path.write_text(name)
print(f"Hola {name}, hemos guardado tu nombre en el registro.")