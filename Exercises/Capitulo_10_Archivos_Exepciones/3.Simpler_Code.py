# Simplificacion de código eliminando variables temporales
# Uso de ciclo for en lugar de variable temporal
# Código ANTES con variable temporal
# from pathlib import Path

# path = Path('pi_digits.txt')
# contents = path.read_text()
# lines = contents.splitlines()  # ← Variable temporal

# for line in lines:
#     print(line)

#Códiogo con cíclo for
from pathlib import Path

path  = Path('pi_digits.txt')
contents = path.read_text()

# LOOP directo sobre splitlines()
for line in contents.splitlines():
    print(line)

# Mejores prácticas actuales y comparacion de los niveles de concisión
# Nivel 1: Muy explícito (principiantes)
contents = path.read_text()
lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

# Nivel 2: Sin variable 'lines'
contents = path.read_text()
pi_string = ''
for line in contents.splitlines():
    pi_string += line.lstrip()

# Nivel 3: Sin variable 'contents'
pi_string = ''
for line in path.read_text().splitlines():
    pi_string += line.lstrip()

# Nivel 4: Usando generator expression (Pythonic)
pi_string = ''.join(line.lstrip() for line in path.read_text().splitlines())

# Nivel 5: Ultra conciso (pero menos legible)
pi_string = path.read_text().replace('\n', '').replace(' ', '')