# 10-7 Uso de while loops para permitir multiples entradas con manejo de exepciones
from pathlib import Path


print("-Calculadora de Suma-")
print("Escribe 'q' para salir")

while True:
    # Solicitar primer número
    first_number = input("Primer número: ")
    if first_number == 'q':
        break
    second_number = input("Segundo número: ")
    if second_number == 'q':
        break

    # Intentar realizar la suma y conversion de numero a entero
    try:
        first = int(first_number)
        second = int(second_number)
        result = first + second
        print(f"Resultado de {first} + {second} = {result}")
    except ValueError:
        print("x Error: Uno o ambos valores no son números validos.\n")

print("\n¡Gracias por usar la calculadora!")

#----------------------------------------------------------------------------------
# Mejores practicas actuales
# Version con función helper reutilizable:
def get_number_or_quit(prompt):
       """
       Solicita un número o permite salir.
       
       Returns:
           El número ingresado, o None si el usuario quiere salir
       """
       while True:
           value = input(prompt).strip()
           
           if value.lower() == 'q':
               return None
           
           try:
               return int(value)
           except ValueError:
               print(f"✗ '{value}' no es válido. Intenta de nuevo o escribe 'q'.")
   
print("=== Calculadora de Suma ===")
print("Escribe 'q' en cualquier momento para salir.\n")

while True:
    first = get_number_or_quit("Primer número: ")
    if first is None:
        break
    
    second = get_number_or_quit("Segundo número: ")
    if second is None:
        break
    
    result = first + second
    print(f"✓ Resultado: {first} + {second} = {result}\n")
   
print("\n¡Gracias por usar la calculadora!")

#---------------------------------------------------------------------------------
# Versión con multiples operaciones
def get_number_or_quit2(prompt):
       """Solicita un número o permite salir."""
       while True:
           value = input(prompt).strip()
           if value.lower() == 'q':
               return None
           try:
               return float(value)
           except ValueError:
               print(f"✗ '{value}' no es válido.")
   
def calculate(num1, num2, operation):
    """Realiza la operación matemática."""
    operations = {
        '+': num1 + num2,
        '-': num1 - num2,
        '*': num1 * num2,
        '/': num1 / num2 if num2 != 0 else "Error: División por cero"
    }
    return operations.get(operation, "Operación no válida")

print("=== Calculadora ===")
print("Operaciones: +, -, *, /")
print("Escribe 'q' para salir.\n")

while True:
    first = get_number_or_quit2("Primer número: ")
    if first is None:
        break
    
    operation = input("Operación (+, -, *, /): ").strip()
    if operation.lower() == 'q':
        break
    
    second = get_number_or_quit2("Segundo número: ")
    if second is None:
        break
    
    try:
        result = calculate(first, second, operation)
        print(f"✓ {first} {operation} {second} = {result}\n")
    except ZeroDivisionError:
        print("✗ Error: No se puede dividir entre cero.\n")
   
print("\n¡Gracias por usar la calculadora!")

#--------------------------------------------------------------------------------
# Version historial de aplicaciones
from datetime import datetime
   
def get_number_or_quit3(prompt):
    """Solicita un número o permite salir."""
    while True:
        value = input(prompt).strip()
        if value.lower() == 'q':
            return None
        try:
            return float(value)
        except ValueError:
            print(f"✗ '{value}' no es válido.")

print("=== Calculadora con Historial ===")
print("Escribe 'q' para salir.\n")

history = []

while True:
    first = get_number_or_quit3("Primer número: ")
    if first is None:
        break
    
    second = get_number_or_quit3("Segundo número: ")
    if second is None:
        break
    
    result = first + second
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Guardar en historial
    entry = f"{timestamp} | {first} + {second} = {result}"
    history.append(entry)
    
    print(f"✓ Resultado: {result}\n")

# Guardar historial en archivo
if history:
    path = Path('calculator_history.txt')
    content = '\n'.join(history)
    path.write_text(content, encoding='utf-8')
    
    print(f"\n📊 Se realizaron {len(history)} operación(es).")
    print(f"📁 Historial guardado en {path}")

print("¡Gracias por usar la calculadora!")