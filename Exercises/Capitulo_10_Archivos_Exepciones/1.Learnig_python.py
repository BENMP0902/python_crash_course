# Bloque 1: Lectura de archivos(10-1 a 10-3)
# Objetivo: Leer un archivo e imprimirlo de tres formas: leyendo todo el archivo,
# iterando sobre el objeto archivado y almacenando las lineas en una lista.
from pathlib import Path

# Definimos la ruta al archivo
path = Path('learning_python.txt')

# Leemos el documento de forma segura
if path.exists():
    contents = path.read_text()

    # 1. lectura completa
    print("--- Contenido Completado ---")
    print(contents)

    # 2. Lectura línea por línea usando splitlines()
    print("\n--- Línea por línea ---")
    lines = contents.splitlines()
    for line in lines:
        # 10-2: Reemplazar una palabra (ej. Python por C)
        print(line.replace('Python', 'C'))
else:
    print("El archivo no existe.")