from pathlib import Path

path = Path(__file__).parent / 'pi_million_digits.txt'
contents = path.read_text(encoding='utf-8')

lines = contents.splitlines()
pi_string = ''

for line in lines:
    pi_string += line.lstrip()

print(f"{pi_string[:52]}...")
print(len(pi_string))