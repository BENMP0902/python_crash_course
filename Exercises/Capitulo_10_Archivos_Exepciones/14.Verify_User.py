# 10-14: Verificación de usuario y refactorizacion de código.
# El programa User_Dictionary.py(remember_me.py) asume que el usuario que ejecuta el programa
# es el usuario correcto lo cual es un error de seguridad. 
# Refactorizaremos el progroma para que el solicite al usuario su nomnbre y darle autenticación
import json
from pathlib import Path

def get_stored_username():
    """Obtiene el nombre de usuario almacenado si existe."""
    path = Path('username.json')
    
    try:
        contents = path.read_text(encoding='utf-8')
        username = json.loads(contents)
        return username
    except FileNotFoundError:
        return None

def get_new_username():
    """Solicita un nuevo nombre de usuario."""
    username = input("¿Cómo te llamas? ")
    
    path = Path('username.json')
    contents = json.dumps(username)
    path.write_text(contents, encoding='utf-8')
    
    return username

def greet_user():
    """
    Saluda al usuario por su nombre.
    Verifica que el usuario sea correcto.
    """
    username = get_stored_username()
    
    if username:
        # Verificar si es el usuario correcto
        response = input(f"¿Eres {username}? (s/n): ").strip().lower()
        
        if response == 's':
            print(f"¡Bienvenido de nuevo, {username}!")
        else:
            # Usuario diferente
            username = get_new_username()
            print(f"¡Te recordaremos cuando regreses, {username}!")
    else:
        # Nuevo usuario
        username = get_new_username()
        print(f"¡Te recordaremos cuando regreses, {username}!")

# Ejecutar
greet_user()
#-----------------------------------------------------------------------
# Mejores prácticas actuales:
# Version mejorada con validacion robusta:

def get_stored_username1(filepath='username.json'):
    """
    Obtiene el nombre de usuario almacenado.
    
    Args:
        filepath: Ruta del archivo JSON
    
    Returns:
        str: Nombre de usuario o None si no existe
    """
    path = Path(filepath)
    
    try:
        contents = path.read_text(encoding='utf-8')
        username = json.loads(contents)
        return username
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        print("⚠ Archivo corrupto. Se creará uno nuevo.")
        return None

def get_new_username1():
    """
    Solicita y valida un nuevo nombre de usuario.
    
    Returns:
        str: Nombre de usuario válido
    """
    while True:
        username = input("\n¿Cómo te llamas? ").strip()
        
        if not username:
            print("⚠ El nombre no puede estar vacío.")
            continue
        
        if len(username) < 2:
            print("⚠ El nombre debe tener al menos 2 caracteres.")
            continue
        
        # Confirmar el nombre
        confirm = input(f"Tu nombre es '{username}', ¿es correcto? (s/n): ").strip().lower()
        
        if confirm == 's':
            break
        else:
            print("Ok, intentémoslo de nuevo.")
    
    # Guardar en JSON
    path = Path('username.json')
    contents = json.dumps(username, ensure_ascii=False)
    path.write_text(contents, encoding='utf-8')
    
    return username

def verify_user1(stored_username):
    """
    Verifica si el usuario actual es el usuario almacenado.
    
    Args:
        stored_username: Nombre de usuario almacenado
    
    Returns:
        bool: True si es el usuario correcto, False si no
    """
    print(f"\n👤 Usuario encontrado: {stored_username}")
    
    max_attempts = 3
    
    for attempt in range(1, max_attempts + 1):
        response = input(f"¿Eres {stored_username}? (s/n): ").strip().lower()
        
        if response == 's':
            return True
        elif response == 'n':
            return False
        else:
            print(f"⚠ Por favor, responde 's' o 'n'. (Intento {attempt}/{max_attempts})")
    
    # Si no responde correctamente después de 3 intentos
    print("\n⚠ Demasiados intentos. Tratándote como usuario nuevo.")
    return False

def greet_user1():
    """Programa principal: verifica y saluda al usuario."""
    print("="*50)
    print("       SISTEMA DE VERIFICACIÓN DE USUARIO")
    print("="*50)
    
    stored_username = get_stored_username1()
    
    if stored_username:
        # Verificar identidad
        if verify_user1(stored_username):
            print(f"\n✓ ¡Bienvenido de nuevo, {stored_username}! 🎉\n")
        else:
            # Usuario diferente
            print(f"\n👋 Hola, usuario nuevo.")
            username = get_new_username1()
            print(f"\n✓ ¡Te recordaremos, {username}! 🎉\n")
    else:
        # Primera vez en el sistema
        print("\n👋 ¡Hola! Parece que es tu primera vez aquí.")
        username = get_new_username1()
        print(f"\n✓ ¡Bienvenido, {username}! Te recordaremos para la próxima vez. 🎉\n")

if __name__ == '__main__':
    greet_user1()
#-----------------------------------------------------------------------------------
# Version vanzada con multiples usuarios:
from datetime import datetime

def get_all_users(filepath='users.json'):
    """
    Obtiene todos los usuarios almacenados.
    
    Returns:
        dict: Diccionario de usuarios o {} si no existe
    """
    path = Path(filepath)
    
    try:
        contents = path.read_text(encoding='utf-8')
        users = json.loads(contents)
        return users
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_all_users(users, filepath='users.json'):
    """
    Guarda todos los usuarios en JSON.
    
    Args:
        users: Diccionario de usuarios
        filepath: Ruta del archivo JSON
    """
    path = Path(filepath)
    contents = json.dumps(users, indent=4, ensure_ascii=False)
    path.write_text(contents, encoding='utf-8')

def get_new_user():
    """
    Crea un nuevo usuario con información completa.
    
    Returns:
        dict: Información del nuevo usuario
    """
    print("\n=== 📝 Registro de Nuevo Usuario ===\n")
    
    while True:
        username = input("Nombre de usuario: ").strip().lower()
        
        if not username:
            print("⚠ El nombre no puede estar vacío.")
            continue
        
        if len(username) < 3:
            print("⚠ El nombre debe tener al menos 3 caracteres.")
            continue
        
        # Verificar si el usuario ya existe
        users = get_all_users()
        if username in users:
            print(f"⚠ El usuario '{username}' ya existe.")
            
            use_existing = input("¿Quieres usar este usuario? (s/n): ").strip().lower()
            if use_existing == 's':
                return username, users[username]
            continue
        
        break
    
    # Solicitar información adicional
    full_name = input("Nombre completo: ").strip()
    email = input("Email (opcional): ").strip() or None
    
    user_data = {
        'username': username,
        'full_name': full_name,
        'email': email,
        'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'last_login': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'login_count': 1
    }
    
    return username, user_data

def update_user_login(username, users):
    """
    Actualiza la información de login del usuario.
    
    Args:
        username: Nombre de usuario
        users: Diccionario de usuarios
    """
    if username in users:
        users[username]['last_login'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        users[username]['login_count'] = users[username].get('login_count', 0) + 1
        save_all_users(users)

def list_users(users):
    """
    Muestra todos los usuarios registrados.
    
    Args:
        users: Diccionario de usuarios
    """
    if not users:
        print("\n⚠ No hay usuarios registrados.\n")
        return
    
    print("\n" + "="*60)
    print("           👥 USUARIOS REGISTRADOS")
    print("="*60)
    
    for i, (username, data) in enumerate(users.items(), 1):
        print(f"\n{i}. {username}")
        print(f"   Nombre: {data.get('full_name', 'N/A')}")
        print(f"   Email: {data.get('email', 'N/A')}")
        print(f"   Registrado: {data.get('created_at', 'N/A')}")
        print(f"   Último acceso: {data.get('last_login', 'N/A')}")
        print(f"   Visitas: {data.get('login_count', 0)}")
    
    print("\n" + "="*60 + "\n")

def select_user(users):
    """
    Permite seleccionar un usuario de la lista.
    
    Args:
        users: Diccionario de usuarios
    
    Returns:
        str: Nombre de usuario seleccionado o None
    """
    if not users:
        return None
    
    usernames = list(users.keys())
    
    print("\nUsuarios disponibles:")
    for i, username in enumerate(usernames, 1):
        full_name = users[username].get('full_name', 'N/A')
        print(f"  {i}. {username} ({full_name})")
    
    print(f"  {len(usernames) + 1}. Usuario nuevo")
    
    while True:
        try:
            choice = input("\nSelecciona una opción: ").strip()
            
            if not choice:
                continue
            
            choice = int(choice)
            
            if 1 <= choice <= len(usernames):
                return usernames[choice - 1]
            elif choice == len(usernames) + 1:
                return None  # Usuario nuevo
            else:
                print(f"⚠ Opción inválida. Elige entre 1 y {len(usernames) + 1}.")
        except ValueError:
            print("⚠ Por favor, ingresa un número.")

def verify_user_identity(username, user_data):
    """
    Verifica la identidad del usuario con preguntas de seguridad.
    
    Args:
        username: Nombre de usuario
        user_data: Datos del usuario
    
    Returns:
        bool: True si la identidad es verificada
    """
    print(f"\n🔒 Verificación de identidad para '{username}'")
    
    # Pregunta simple de verificación
    stored_name = user_data.get('full_name', '')
    
    if stored_name:
        entered_name = input(f"Por favor, ingresa tu nombre completo: ").strip()
        
        if entered_name.lower() == stored_name.lower():
            print("✓ Identidad verificada.")
            return True
        else:
            print("✗ Nombre incorrecto.")
            return False
    else:
        # Si no hay nombre almacenado, preguntar directamente
        response = input(f"¿Eres {username}? (s/n): ").strip().lower()
        return response == 's'

def main_menu():
    """Menú principal del sistema."""
    print("\n" + "="*60)
    print("   🔐 SISTEMA DE GESTIÓN DE USUARIOS")
    print("="*60)
    
    users = get_all_users()
    
    if users:
        print(f"\n📊 Usuarios registrados: {len(users)}")
        
        print("\nOpciones:")
        print("  1. Iniciar sesión")
        print("  2. Nuevo usuario")
        print("  3. Listar usuarios")
        print("  4. Salir")
        
        choice = input("\nSelecciona una opción: ").strip()
        
        if choice == '1':
            # Iniciar sesión
            username = select_user(users)
            
            if username:
                # Verificar identidad
                if verify_user_identity(username, users[username]):
                    update_user_login(username, users)
                    
                    user = users[username]
                    print(f"\n{'='*60}")
                    print(f"✓ ¡Bienvenido de nuevo, {user.get('full_name', username)}! 🎉")
                    print(f"{'='*60}")
                    print(f"👤 Usuario: {username}")
                    print(f"📧 Email: {user.get('email', 'N/A')}")
                    print(f"📅 Última visita: {user.get('last_login', 'N/A')}")
                    print(f"🔢 Total de visitas: {user.get('login_count', 0)}")
                    print(f"{'='*60}\n")
                else:
                    print("\n⚠ Verificación fallida. Acceso denegado.\n")
            else:
                # Usuario nuevo desde selección
                username, user_data = get_new_user()
                users[username] = user_data
                save_all_users(users)
                print(f"\n✓ ¡Bienvenido, {user_data['full_name']}! Usuario creado exitosamente. 🎉\n")
        
        elif choice == '2':
            # Nuevo usuario
            username, user_data = get_new_user()
            users[username] = user_data
            save_all_users(users)
            print(f"\n✓ ¡Bienvenido, {user_data['full_name']}! Usuario creado exitosamente. 🎉\n")
        
        elif choice == '3':
            # Listar usuarios
            list_users(users)
        
        elif choice == '4':
            print("\n👋 ¡Hasta luego!\n")
        
        else:
            print("\n⚠ Opción no válida.\n")
    
    else:
        # Sin usuarios registrados
        print("\n👋 No hay usuarios registrados. Vamos a crear el primero.")
        username, user_data = get_new_user()
        users[username] = user_data
        save_all_users(users)
        print(f"\n✓ ¡Bienvenido, {user_data['full_name']}! Primer usuario creado. 🎉\n")

if __name__ == '__main__':
    main_menu()