from pathlib import Path

# Leemos el archivo y reemplazamos "Python" por "C"
path = Path('learning_python.txt')

try:
    contents = path.read_text(encoding='utf-8')

    # Método 1: Reemplazar en todo el contenido de una sola vez
    print("-Reemplazando 'Python' por 'C'-")
    modified_contents = contents.replace('Python', 'C')
    print(modified_contents)

    # Método 2: Linea por linea
    print("-Línea por línea-")
    for line in contents.splitlines():
        modified_line = line.replace('Python', 'C') 
        print(modified_line)

except FileNotFoundError:
    print(f"El archivo {path} no existe :)") 