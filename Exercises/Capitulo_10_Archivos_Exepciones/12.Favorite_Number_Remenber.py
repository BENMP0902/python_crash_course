# 10-12: Refactorizacion para recordar datos existentes
# Combina los programas 11 y 12, si el número ya esta almacenado lo muestra,
# de lo contratio lo solicita y lo guarda.
import json
from pathlib import Path

def get_stored_number():
    """Obtiene el número favorito si existe."""
    path = Path('favorite_number.json')
    
    try:
        contents = path.read_text(encoding='utf-8')
        return json.loads(contents)
    except FileNotFoundError:
        return None

def save_new_number():
    """Solicita y guarda un nuevo número favorito."""
    number = input("¿Cuál es tu número favorito? ")
    
    path = Path('favorite_number.json')
    contents = json.dumps(number)
    path.write_text(contents, encoding='utf-8')
    
    return number

def favorite_number():
    """Muestra el número favorito o solicita uno nuevo."""
    number = get_stored_number()
    
    if number:
        print(f"¡Sé cuál es tu número favorito! Es el {number}.")
    else:
        number = save_new_number()
        print(f"✓ Recordaré que tu número favorito es {number}.")

# Ejecutar
save_new_number()
get_stored_number()
favorite_number()
#----------------------------------------------------------------------------------
# Mejores practicas:
# Version con validación mejorada:
def get_stored_number1(filepath='favorite_number.json'):
    """
    Obtiene el número favorito almacenado.
    
    Args:
        filepath: Ruta del archivo JSON
    
    Returns:
        El número almacenado o None si no existe
    """
    path = Path(filepath)
    
    try:
        contents = path.read_text(encoding='utf-8')
        return json.loads(contents)
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        print("⚠ Archivo JSON corrupto. Se creará uno nuevo.")
        return None

def get_valid_number1():
    """Solicita un número válido al usuario."""
    while True:
        number_str = input("¿Cuál es tu número favorito? ").strip()
        
        try:
            # Intentar convertir a int primero
            return int(number_str)
        except ValueError:
            try:
                # Si falla, intentar float
                return float(number_str)
            except ValueError:
                print("⚠ Por favor, ingresa un número válido.")

def save_number1(number, filepath='favorite_number.json'):
    """
    Guarda el número en un archivo JSON.
    
    Args:
        number: El número a guardar
        filepath: Ruta del archivo JSON
    """
    path = Path(filepath)
    contents = json.dumps(number, indent=4)
    path.write_text(contents, encoding='utf-8')

def favorite_number1():
    """Programa principal: recordar o solicitar número favorito."""
    number = get_stored_number1()
    
    if number is not None:
        print(f"\n🎯 ¡Sé cuál es tu número favorito! Es el {number}.")
    else:
        print("\n👋 ¡Hola! Parece que es tu primera vez aquí.")
        number = get_valid_number1()
        save_number1(number)
        print(f"✓ Perfecto. Recordaré que tu número favorito es {number}.")

if __name__ == '__main__':
    favorite_number1()

#---------------------------------------------------------------------------------
# Versión con opción de actualizar
def get_stored_number2():
    """Obtiene el número almacenado."""
    path = Path('favorite_number.json')
    
    try:
        contents = path.read_text(encoding='utf-8')
        return json.loads(contents)
    except (FileNotFoundError, json.JSONDecodeError):
        return None

def save_number2(number):
    """Guarda el número en JSON."""
    path = Path('favorite_number.json')
    path.write_text(json.dumps(number), encoding='utf-8')

def favorite_number2():
    """Muestra o solicita número favorito con opción de cambiar."""
    number = get_stored_number2()
    
    if number is not None:
        print(f"🎯 Tu número favorito guardado es: {number}")
        
        change = input("¿Quieres cambiarlo? (s/n): ").strip().lower()
        
        if change == 's':
            new_number = input("Ingresa tu nuevo número favorito: ")
            save_number2(new_number)
            print(f"✓ Actualizado a {new_number}.")
        else:
            print("✓ Mantenemos tu número favorito actual.")
    else:
        print("👋 No tengo ningún número favorito guardado.")
        number = input("¿Cuál es tu número favorito? ")
        save_number2(number)
        print(f"✓ Guardado: {number}")

if __name__ == '__main__':
    favorite_number2()
