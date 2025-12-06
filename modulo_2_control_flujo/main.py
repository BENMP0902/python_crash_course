# ==========================================
# MODULO 2: Control de Flujo (Decisiones y Bucles)
# Archivo: main.py
# ==========================================
import time # Importamos una librería estándar para simular esperas

print("--- EJERCICIO 1: Condicionales (El Portero Digital) ---")
# Objetivo: Validar acceso usando IF, ELIF y ELSE con operadores lógicos (AND/OR).

usuario_admin = "admin"
clave_secreta = "1234"

print("--- SISTEMA DE LOGIN ---")
user_input = input("Usuario: ")
pass_input = input("Contraseña: ")

# Logica: Si usuario coincide Y (and) clave coincide -> Entra.
if user_input == usuario_admin and pass_input == clave_secreta:
    print(">> ACCESO CONCEDIDO: Bienvenido al sistema root.")
    nivel_acceso = 10
elif user_input == usuario_admin and pass_input != clave_secreta:
    print(">> ERROR: Contraseña incorrecta.")
    nivel_acceso = 0
else:
    print(">> ALERTA: Usuario desconocido. Acceso denegado.")
    nivel_acceso = 0

print("-" * 30)


print("\n--- EJERCICIO 2: Bucle FOR (El Escáner) ---")
# Objetivo: Recorrer una lista de elementos uno por uno.
# Imagina que estamos escaneando puertos o direcciones IP.

ips_a_escanear = ["192.168.1.1", "192.168.1.5", "10.0.0.1", "127.0.0.1"]

print(f"Iniciando escaneo de {len(ips_a_escanear)} objetivos...")

# Por cada 'ip' en la lista 'ips_a_escanear':
for ip in ips_a_escanear:
    print(f"[+] Escaneando objetivo: {ip} ...")
    time.sleep(1) # Simula un pequeño retraso (descomentar para probar)

print(">> Escaneo finalizado.")
print("-" * 30)


print("\n--- EJERCICIO 3: Bucle WHILE (Fuerza Bruta Simulada) ---")
# Objetivo: Repetir una acción MIENTRAS una condición sea verdadera.

pin_objetivo = 5  # Imaginemos que este es el PIN correcto (simplificado)
intento_actual = 0
contador = 0

print("Iniciando ataque de fuerza bruta simple (Buscando el número 5)...")

# Mientras el intento NO sea igual al objetivo:
while intento_actual != pin_objetivo:
    contador += 1
    intento_actual += 1 # Probamos el siguiente número
    print(f"Probando PIN: {intento_actual} -> Fallo")
    time.sleep(0.5)

print(f">> ¡ÉXITO! PIN encontrado: {intento_actual} en {contador} intentos.")
print("-" * 30)


print("\n--- EJERCICIO 4: Control de Bucles (Break y Continue) ---")
# Objetivo: Saltar iteraciones o romper el bucle prematuramente.

# Lista de puertos: El 80 es HTTP (seguro), el 23 es Telnet (INSECURO/PELIGROSO)
puertos = [22, 80, 443, 23, 8080]

print("Analizando vulnerabilidades en puertos...")

for puerto in puertos:
    if puerto == 80 or puerto == 443:
        print(f"Puerto {puerto}: Tráfico Web seguro. (Saltando análisis profundo - CONTINUE)")
        continue # 'continue' salta al siguiente ciclo del bucle, ignorando lo de abajo.
    
    if puerto == 23:
        print(f"ALERTA CRÍTICA: Puerto {puerto} (Telnet) detectado. ¡DETENIENDO SISTEMA! (BREAK)")
        break # 'break' mata el bucle inmediatamente.
    
    print(f"Puerto {puerto}: Analizando...")

print("\n=== MÓDULO 2 COMPLETADO ===")