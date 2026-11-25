from pathlib import Path

# Ruta anclada a la ubicacion del script
path = Path(__file__).parent / 'learning_python.txt'

# Nombres explicitos en lugar de "magic strings" repetidas: si cambia
# el lenguaje, se edita una sola línea.
old_lenguage = 'Python' # palabra a buscar(case sensitive)
new_lenguage = 'C'      # palabra remplazo

# Se lee el archivo como string: encoding para portabilidad
contents = path.read_text(encoding='utf-8')

# splitlines() devuelve list[str] sin \n; se itera directo sin temporal
for line in contents.splitlines():
    print(line.replace(old_lenguage, new_lenguage))