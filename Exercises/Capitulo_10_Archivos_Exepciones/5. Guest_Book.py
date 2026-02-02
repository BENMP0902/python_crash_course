# Escritua en multiples líneas en archivos usando loops
# Uso de ciclo while que solicite a los usuarios su nombre, los recopile y 
# los escriba en un archivo llamado 'guest_book.txt'
from pathlib import Path

print("-Libro de Invitados-")
print("Escribe 'q' para terminar. \n")

# Lista que almacenará los nombres
guests = []

# Loop para recopilar nombres
while True:
    name = input("Por favor, ingresa tu nombre: ")

    if name.lower() == 'q':
        break
    
    guests.append(name)
    print(f"¡Gracias por registrarte, {name}!")

# Guardamos los nombres en el archivo
if guests:
    path = Path('guests_book.txt')
    # Unir nombres con saltos de línea
    content = '\n'.join(guests)
    path.write_text(content, encoding='utf-8')

    print(f"\n ✓ {len(guests)} nomnbre(s) guardado(s) en {path}.")
else:
    print("\nNo se registraron invitados.")


#omparación de métodos de escritura:

guests = ['Alice', 'Bob', 'Charlie']
path = Path('guest_book.txt')

# Método 1: Usando '\n'.join() (RECOMENDADO)
content = '\n'.join(guests)
path.write_text(content, encoding='utf-8')

# Método 2: Construyendo string manualmente
content = ''
for guest in guests:
    content += guest + '\n'
path.write_text(content, encoding='utf-8')

# Método 3: Usando list comprehension
content = '\n'.join([guest for guest in guests])
path.write_text(content, encoding='utf-8')

# Método 4: Con formato adicional
content = '\n'.join(f"{i+1}. {guest}" for i, guest in enumerate(guests))
path.write_text(content, encoding='utf-8')
# ```
#     Ejemplo de salida del archivo `guest_book.txt`:
#     Alice
#     Bob
#     Charlie
#     Diana
#     Edward
#     ```

#     **O con formato mejorado:**
#     ```
#     === LIBRO DE INVITADOS ===
#     Generado: 2025-02-02 14:30:00
#     Total de invitados: 5
#     ========================================

#     1. Alice - 2025-02-02 14:25
#     2. Bob - 2025-02-02 14:26
#     3. Charlie - 2025-02-02 14:27
#     4. Diana - 2025-02-02 14:28
#     5. Edward - 2025-02-02 14:29
# ```