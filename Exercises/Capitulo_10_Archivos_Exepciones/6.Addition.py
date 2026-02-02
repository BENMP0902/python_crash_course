# 10-7: Manejo de exepciones ValueError al convertir input a números
print("-Calculadora de Suma-\n")

try:
    # Solicitamos dos números
    first_number = input("Ingresa el primer número: ")
    second_number = input("Inbgresa el segundo número: ")

    # Convertir a int y sumar
    result = int(first_number) + int(second_number)

    print(f"\nResultado_ {first_number} + {second_number} = {result}")

except ValueError:
    print("\nError: Por favor, ingresa solo números validos.")

#----------------------------------------------------------
#Mejores prácticas actuales:

# Versión con mensajes de error más específicos:

try:
    first_number = input("Ingresa el primer número: ")
    first = int(first_number)
    
    second_number = input("Ingresa el segundo número: ")
    second = int(second_number)
    
    result = first + second
    print(f"\n✓ Resultado: {first} + {second} = {result}")
    
except ValueError as e:
    print(f"\n✗ Error: '{first_number}' o '{second_number}' no es un número válido.")
    print(f"   Detalles técnicos: {e}")

#---------------------------------------------------------
# Versión con validación individual de cada número:

def get_number1(prompt):
    """Solicita un número y valida la entrada."""
    while True:
        try:
            value = input(prompt)
            return int(value)
        except ValueError:
            print(f"✗ '{value}' no es un número válido. Intenta de nuevo.")

print("=== Calculadora de Suma ===\n")

first = get_number1("Ingresa el primer número: ")
second = get_number1("Ingresa el segundo número: ")

result = first + second
print(f"\n✓ Resultado: {first} + {second} = {result}")

# Versión que maneja números decimales (float):

def get_number2(prompt):
    """Solicita un número (entero o decimal)."""
    while True:
        try:
            value = input(prompt)
            # Intentar convertir a float primero
            num = float(value)
            return num
        except ValueError:
            print(f"✗ '{value}' no es un número válido.")

print("=== Calculadora de Suma ===\n")

first = get_number2("Ingresa el primer número: ")
second = get_number2("Ingresa el segundo número: ")

result = first + second

# Formatear resultado
if result == int(result):
    print(f"\n✓ Resultado: {int(first)} + {int(second)} = {int(result)}")
else:
    print(f"\n✓ Resultado: {first} + {second} = {result:.2f}")

#----------------------------------------------------------------------
# Versión profesional con múltiples validaciones:

def get_validated_number(prompt, allow_negative=True, allow_decimal=True):
    """
    Solicita un número con validaciones personalizadas.
    
    Args:
        prompt: Mensaje para el usuario
        allow_negative: Si se permiten números negativos
        allow_decimal: Si se permiten números decimales
    
    Returns:
        Un número validado (int o float)
    """
    while True:
        try:
            value = input(prompt).strip()
            
            # Validar entrada vacía
            if not value:
                print("✗ No puedes dejar este campo vacío.")
                continue
            
            # Convertir a número
            if allow_decimal:
                num = float(value)
            else:
                num = int(value)
            
            # Validar si es negativo
            if not allow_negative and num < 0:
                print("✗ No se permiten números negativos.")
                continue
            
            return num
            
        except ValueError:
            print(f"✗ '{value}' no es un número válido.")

print("=== Calculadora de Suma ===\n")

first = get_validated_number("Primer número: ")
second = get_validated_number("Segundo número: ")

result = first + second
print(f"\n✓ {first} + {second} = {result}")

#--------------------------------------------------
# Comparación de enfoques de manejo de errores:

# ❌ MALO - Sin manejo de errores
first = int(input("Primer número: "))
second = int(input("Segundo número: "))
print(first + second)
# Crashea si el usuario ingresa texto

# ✅ BUENO - Manejo básico
try:
    first = int(input("Primer número: "))
    second = int(input("Segundo número: "))
    print(first + second)
except ValueError:
    print("Error: Ingresa números válidos")

# ✅ MEJOR - Validación con loop
def get_number3(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Error. Intenta de nuevo.")

first = get_number3("Primer número: ")
second = get_number3("Segundo número: ")
print(f"Resultado: {first + second}")

# ✅ EXCELENTE - Función reutilizable con opciones
def get_number(prompt, num_type=int, min_val=None, max_val=None):
    while True:
        try:
            num = num_type(input(prompt))
            if min_val is not None and num < min_val:
                print(f"Debe ser >= {min_val}")
                continue
            if max_val is not None and num > max_val:
                print(f"Debe ser <= {max_val}")
                continue
            return num
        except ValueError:
            print("Número inválido")   