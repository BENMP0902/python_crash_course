# 10-8: Manejo de FileNotFoundError
from pathlib import Path

# Lista de archivos a leer
filenames = ['cats.txt', 'dogs.txt', 'birds.txt']

for filename in filenames:
    path = Path(filename)

    try:
        contents = path.read_text(encoding='utf-8')
        print(f"-Contenido en {filename}-")
        print(contents)
    except FileNotFoundError:
        print(f"\nx Lo siendo, no se pudo encontrar el archivo '{filename}'.")

#----------------------------------------------------------------------------------
# Mejores practicas actuLles
# Crear archivos de ejemplo si no existen
def create_sample_files():
    """Crea archivos de ejemplo con nombres de mascotas."""
    cats_data = "Whiskers\nMittens\nLuna\nShadow\nSimba"
    dogs_data = "Buddy\nMax\nBella\nCharlie\nDaisy"
    
    Path('cats.txt').write_text(cats_data, encoding='utf-8')
    Path('dogs.txt').write_text(dogs_data, encoding='utf-8')
    print("✓ Archivos de ejemplo creados.\n")

# Crear archivos (comentar después de la primera ejecución)
create_sample_files()

# Leer archivos con manejo de errores
filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    path = Path(filename)
    
    try:
        contents = path.read_text(encoding='utf-8')
        
        print(f"=== {filename.upper()} ===")
        # Imprimir cada línea con viñeta
        for line in contents.splitlines():
            print(f"  • {line}")
        print()
        
    except FileNotFoundError:
        print(f"✗ Error: El archivo '{filename}' no existe.")
        print(f"  Ubicación esperada: {path.absolute()}\n")


#----------------------------------------------------------------------------------
# Version con validacion adicional y estadísticas

def read_pet_file(filename):
    """
    Lee un archivo de mascotas y retorna información.
    
    Returns:
        dict con 'success', 'names', 'count', 'error'
    """
    path = Path(filename)
    
    try:
        contents = path.read_text(encoding='utf-8')
        names = [name.strip() for name in contents.splitlines() if name.strip()]
        
        return {
            'success': True,
            'names': names,
            'count': len(names),
            'error': None
        }
        
    except FileNotFoundError:
        return {
            'success': False,
            'names': [],
            'count': 0,
            'error': f"Archivo '{filename}' no encontrado"
        }
    except UnicodeDecodeError:
        return {
            'success': False,
            'names': [],
            'count': 0,
            'error': f"Error al leer '{filename}': problema de codificación"
        }

# Procesar archivos
files = {
    'cats.txt': '🐱 Gatos',
    'dogs.txt': '🐶 Perros'
}

total_pets = 0

for filename, label in files.items():
    result = read_pet_file(filename)
    
    if result['success']:
        print(f"\n{label} ({result['count']} encontrado(s)):")
        for i, name in enumerate(result['names'], 1):
            print(f"  {i}. {name}")
        total_pets += result['count']
    else:
        print(f"\n✗ {label}: {result['error']}")

if total_pets > 0:
    print(f"\n📊 Total de mascotas registradas: {total_pets}")

#----------------------------------------------------------------------------------



#----------------------------------------------------------------------------------


#----------------------------------------------------------------------------------