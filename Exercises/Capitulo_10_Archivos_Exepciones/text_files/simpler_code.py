from pathlib import Path

path = Path(__file__).parent / 'pi_digits.txt'

contents = path.read_text(encoding='utf-8')

# ANTES: 
# line = contents.splitlines()
# for line in lines:
# AHORA: la llamada a splitlines() se evalua una sola vex y el for
# se itera sobre la liste que devuelve. Sin variable intermedia.
for line in contents.splitlines():
    print(line)


print(" hola \n".strip())