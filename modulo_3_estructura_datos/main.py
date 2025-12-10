# ==========================================
# MODULO 3: Estructuras de Datos (Listas y Diccionarios)
# Archivo: main.py
# ==========================================

print("--- EJERCICIO 1: Listas (El Inventario de Herramientas) ---")
# Objetivo: Crear, agregar, eliminar y acceder a elementos de una lista.
# Las listas usan corchetes [] y son ORDENADAS (tienen posicion 0,1,2,3,...)

# 1. Creacion
herramientas = ["nmap", "wireshark", "burpsuite", "metasploit"]
print(f"Inventario inicial: {herramientas}")

# 2. Acceso (Indexing)
print(f"Herramienta principal (indice 0): {herramientas[0]}")
print(f"Ultima herramienta (indice -1) {herramientas[-1]}")

# 3. Modificacion (Mutable)
herramientas[1] = "tshark" # Cambiamos wireshark por tshark
print(f"Inventario modificado: {herramientas}")

# 4. Métodos (Append y Remove)
herramientas.append("sqlmap") # Se agrega al final
herramientas.remove("burpsuite") # Eliminacion por valor
print(f"Inventario final: {herramientas}")
print("-" * 30)

print("\n--- EJERCICIO 2: Slicing (Análisis de Tráfico) ---")
# Objetivo: Cortar listas para obtener sub-conjuntos de datos.
# Sintaxis: lista[inicio : fin : pasos])

paquetes_red = ["packet_1","packet_2","packet_3","packet_4","packet_5","packet_6"]

print(f"Total de paquetes capturados: {len(paquetes_red)}")

# Tomaar los primero 3 
primeros_tres = paquetes_red[:3]
print(f"Cabecera (Primeros 3): {primeros_tres}")

# Tomar las ultimas 2
ultimos_dos = paquetes_red[-2:]
print(f"Cola (Últimos 2): {ultimos_dos}")

# Invertir la lista
invertidos = paquetes_red[::-1]
print(f"Invertidos: {invertidos}")
print("-" * 30)

print("\n--- EJERCICIO 3: Diccionarios (Configuración del Servidor) ---")
# Objetivo: Manejar datos clave-valor. Es la base de JSON y bases de datos NoSQL.
# Los diccionarios usan llaves {} y NO tienen orden garantizado (antes de Python 3.7).

servidor = {
    "ip": "192.168.1.10",
    "puerto": 22,
    "estado": "activo",
    "usuarios_conectados": 3
}

# 1. Acceder por Clave (Key)
print(f"Conectando a IP: {servidor['ip']} en puerto {servidor['puerto']}...")

# 2. Modificar valor
servidor["estado"] = "mantenimiento"

# 3. Agregar nueva clave
servidor["os"] = "Kali_Linux"

print("configuracion actualizada del servidor:")
print(servidor) # Muestra todo el objeto
print("-" * 30)

print("\n--- EJERCICIO 4: Estructuras Anidadas (Simulando una API JSON) ---")
# Objetivo: Listas que contienen Diccionarios. 
# Así es como se ven los datos reales en MLOps.

base_de_datos_vulnerabilidades = [
    {
        "id": "CVE-2025-001",
        "tipo": "SQL Injection",
        "severidad": "Alta"
    },
    {
        "id": "CVE-2025-002",
        "tipo": "XSS",
        "severidad": "Media"
    },
    {
        "id": "CVE-2025-003",
        "tipo": "DDoS",
        "severidad": "Critica"
    }
]

print("Reporte de Vulnerabilidades:")

# Recorremos la lista, y cada 'vuln' es un diccionario
for vuln in base_de_datos_vulnerabilidades:
    if vuln["severidad"] == "Alta" or vuln["severidad"] == "Critica":
        print(f"[ALERTA] {vuln['id']}: {vuln['tipo']} (Revisar Inmediatamente)")
    else:
        print(f"[INFO] {vuln['id']}: {vuln['tipo']} (Monitorear)")

print("\n=== MÓDULO 3 COMPLETADO ===")
