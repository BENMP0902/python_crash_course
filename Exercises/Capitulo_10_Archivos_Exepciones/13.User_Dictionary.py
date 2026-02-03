# 10-13: Almacenamiento de estructuras de datos complejas con JSON
# Le pediremos al usuario que nos diga su nombre, edad y ciudad, las cuales almacenaremos
# en el archivo remember_me.txt en formato JSON.
import json
from pathlib import Path

def get_stored_user():
    """Obtiene información del usuario si existe."""
    path = Path('user_data.json')
    
    try:
        contents = path.read_text(encoding='utf-8')
        return json.loads(contents)
    except FileNotFoundError:
        return None

def get_new_user():
    """Solicita información del usuario y la guarda."""
    print("=== Registro de Usuario ===\n")
    
    username = input("Nombre de usuario: ").strip()
    age = input("Edad: ").strip()
    location = input("Ciudad: ").strip()
    
    user_data = {
        'username': username,
        'age': age,
        'location': location
    }
    
    path = Path('user_data.json')
    contents = json.dumps(user_data, indent=4)
    path.write_text(contents, encoding='utf-8')
    
    return user_data

def greet_user():
    """Saluda al usuario con su información almacenada."""
    user = get_stored_user()
    
    if user:
        print(f"\n¡Bienvenido de nuevo, {user['username']}!")
        print(f"Edad: {user['age']}")
        print(f"Ciudad: {user['location']}")
    else:
        user = get_new_user()
        print(f"\n✓ ¡Te recordaremos, {user['username']}!")

# Ejecutar
greet_user()
#-----------------------------------------------------------------------------------
# Mejores practicas actuales:
# Version con validacion y campos
import json
from pathlib import Path
from datetime import datetime

def get_stored_user1(filepath='user_data.json'):
    """
    Obtiene datos del usuario desde JSON.
    
    Returns:
        dict: Datos del usuario o None
    """
    path = Path(filepath)
    
    try:
        contents = path.read_text(encoding='utf-8')
        return json.loads(contents)
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        print("⚠ Archivo de usuario corrupto.")
        return None

def get_valid_age1():
    """Solicita una edad válida."""
    while True:
        age_input = input("Edad: ").strip()
        
        try:
            age = int(age_input)
            if 1 <= age <= 120:
                return age
            else:
                print("⚠ Edad debe estar entre 1 y 120.")
        except ValueError:
            print("⚠ Por favor, ingresa un número válido.")

def get_new_user1():
    """Solicita y guarda información completa del usuario."""
    print("=== 📝 Registro de Nuevo Usuario ===\n")
    
    # Solicitar información
    username = input("Nombre de usuario: ").strip()
    
    while not username:
        print("⚠ El nombre no puede estar vacío.")
        username = input("Nombre de usuario: ").strip()
    
    age = get_valid_age1()
    location = input("Ciudad: ").strip()
    email = input("Email (opcional): ").strip()
    favorite_color = input("Color favorito: ").strip()
    
    # Crear diccionario de usuario
    user_data = {
        'username': username,
        'age': age,
        'location': location,
        'email': email if email else None,
        'favorite_color': favorite_color,
        'registration_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'login_count': 1
    }
    
    # Guardar en JSON
    path = Path('user_data.json')
    contents = json.dumps(user_data, indent=4, ensure_ascii=False)
    path.write_text(contents, encoding='utf-8')
    
    return user_data

def update_login_count1(user_data):
    """Incrementa el contador de logins."""
    user_data['login_count'] = user_data.get('login_count', 0) + 1
    user_data['last_login'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    path = Path('user_data.json')
    contents = json.dumps(user_data, indent=4, ensure_ascii=False)
    path.write_text(contents, encoding='utf-8')

def greet_user1():
    """Saluda al usuario y muestra su información."""
    user = get_stored_user1()
    
    if user:
        # Usuario existente
        update_login_count1(user)
        
        print(f"\n{'='*50}")
        print(f"¡Bienvenido de nuevo, {user['username']}! 👋")
        print(f"{'='*50}")
        print(f"📍 Ciudad: {user['location']}")
        print(f"🎂 Edad: {user['age']}")
        print(f"🎨 Color favorito: {user.get('favorite_color', 'No especificado')}")
        print(f"📅 Registrado: {user.get('registration_date', 'Desconocido')}")
        print(f"🔢 Visitas: {user.get('login_count', 1)}")
        
        if user.get('last_login'):
            print(f"⏰ Último acceso: {user['last_login']}")
        
        print(f"{'='*50}\n")
    else:
        # Nuevo usuario
        print("\n👋 ¡Hola! Parece que eres nuevo aquí.\n")
        user = get_new_user1()
        
        print(f"\n{'='*50}")
        print(f"✓ ¡Bienvenido, {user['username']}!")
        print(f"✓ Tu información ha sido guardada exitosamente.")
        print(f"{'='*50}\n")

if __name__ == '__main__':
    greet_user1()