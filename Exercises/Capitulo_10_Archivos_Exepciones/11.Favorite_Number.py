# 10-11: Almacenamiento de datos con JSON usando 'json.dumps()'
# Solicitaremos al usuario su número favorito y lo almacenaremos usando json.dump().
# Leeremos el valor dado y lo mostraremos en consola
import json
from pathlib import Path

# Programa 1: Guardar número favorito
def save_favorite_number():
    """Solicita y guarda el número favorito del usuario"""
    number = input("¿Cuál es tu número favorito?")
    
    path = Path('favorite_number.json') # Indicamos extension con el formato en el que se almacenará
    contents = json.dumps(number)
    path.write_text(contents, encoding='utf-8')

    print(f"¡Recordaré que tu número favorito es {number}!")

# Programa 2: Leer número favorito
def read_favorite_number():
    """Lee y muestra el número guardado"""
    path = Path('favorite_number.json')

    try:
        contents = path.read_text(encoding='utf-8')
        number = json.loads(contents)
        print(f"¡Sé cuál es tu número favorito! Es el {number}")
    except FileNotFoundError:
        print("No tengo tu número favorito todavía")

# Ejecutar
if __name__ == '__main__':
    # Primera ejecucion: guardar
    save_favorite_number()

    # Segunda ejecucion: leer
    print()
    read_favorite_number()

#----------------------------------------------------------------------------------------
# Mejores prácticas actuales:
# Version con validacion de entrada numerica:
def save_favorite_number2():
    """Solicita y guarda el número favorito del usuario."""
    while True:
        number_input = input("¿Cuál es tu número favorito? ").strip()
        
        try:
            # Intentar convertir a número
            number = int(number_input)
            break
        except ValueError:
            try:
                # Si no es entero, intentar float
                number = float(number_input)
                break
            except ValueError:
                print("⚠ Por favor, ingresa un número válido.")
    
    path = Path('favorite_number.json')
    contents = json.dumps(number)
    path.write_text(contents, encoding='utf-8')
    
    print(f"✓ ¡Guardado! Tu número favorito es {number}.")
   
def read_favorite_number2():
    """Lee y muestra el número favorito guardado."""
    path = Path('favorite_number.json')
    
    try:
        contents = path.read_text(encoding='utf-8')
        number = json.loads(contents)
        print(f"\n¡Sé cuál es tu número favorito! Es el {number}. 🎯")
    except FileNotFoundError:
        print("\n⚠ No hay número favorito guardado.")
    except json.JSONDecodeError:
        print("\n⚠ Error al leer el archivo JSON.")

if __name__ == '__main__':
    save_favorite_number2()
    read_favorite_number2()

#----------------------------------------------------------------------------------------
# Version con uso de json.dump() y json.load()
def save_favorite_number3():
    """Guarda el número favorito usando json.dump()."""
    number = input("¿Cuál es tu número favorito? ")
    
    path = Path('favorite_number.json')
    
    # Método directo con file handle
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(number, f)
    
    print(f"✓ Número {number} guardado exitosamente.")
   
def read_favorite_number3():
    """Lee el número favorito usando json.load()."""
    path = Path('favorite_number.json')
    
    try:
        with open(path, 'r', encoding='utf-8') as f:
            number = json.load(f)
        print(f"\n¡Conozco tu número favorito! Es el {number}.")
    except FileNotFoundError:
        print("\n⚠ Archivo no encontrado.")

if __name__ == '__main__':
    save_favorite_number3()
    read_favorite_number3()

#----------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------