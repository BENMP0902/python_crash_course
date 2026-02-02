# Bloque 2: Escritura de Archivos(10-4 y 10-5)
# 10-4: Descripción: Pedir al usuauario su nombre y almacenarlo en un archivo 'guests.txt'
from pathlib import Path

# Saludo y peticion del nombre al usuario
print("¡Bienvenido a la biblioteca de invitados!")
print("Presiona 'q' para salir.")
name = input("Por favor ingresa tu nombre")

# Almacenamos su nombre
path = Path('guest.txt')
path.write_text(name, encoding='utf-8')

print(f"Gracias {name}! Tú nombre ha sido guardado en {path}.")

# Mejores prácticas actuales:

# Versión con validación de entrada:
def save_guest_name():
    """Solicita y guarda el nombre de un invitado."""
    # Validar que el nombre no esté vacío
    while True:
        name = input("Por favor, ingresa tu nombre: ").strip()
        if name:
            break
        print("El nombre no puede estar vacío. Intenta de nuevo.")
    
    # Guardar en archivo
    path = Path('guest.txt')
    try:
        path.write_text(name, encoding='utf-8')
        print(f"✓ ¡Gracias, {name}! Tu nombre ha sido guardado.")
    except Exception as e:
        print(f"✗ Error al guardar el archivo: {e}")

save_guest_name()


# Con timestamp (marca de tiempo):
from datetime import datetime

name = input("Por favor, ingresa tu nombre: ")
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Guardar nombre con fecha y hora
content = f"{name} - Registrado el {timestamp}"

path = Path('guest.txt')
path.write_text(content, encoding='utf-8')

print(f"¡Gracias, {name}! Tu nombre ha sido guardado.")


# Verificar si el archivo ya existe:
name = input("Por favor, ingresa tu nombre: ")
path = Path('guest.txt')

# Advertir si el archivo ya existe
if path.exists():
    response = input(f"El archivo {path} ya existe. ¿Sobreescribir? (s/n): ")
    if response.lower() != 's':
        print("Operación cancelada.")
        exit()

path.write_text(name, encoding='utf-8')
print(f"✓ ¡Gracias, {name}! Tu nombre ha sido guardado.")