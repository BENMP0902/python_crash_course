from pathlib import Path

path = Path(__file__).parent / 'learning_python.txt'

# Forma de lectura por completo como string
contents = path.read_text(encoding='utf-8')

print("-- Reading the entire file --")
print(contents)

# Forma de lectura guardando las lineas como listas y recorrerla
lines = contents.splitlines()

print("-- Looping over the lines --")

# Recorre la lista con un for; line es cada string individual
for line in lines:
    print(line)
