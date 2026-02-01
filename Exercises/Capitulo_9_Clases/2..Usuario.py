# 9-3 Users: Modelaremos personas/usuarios
class User:
    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        # Atributo agregado en 9-5
        self.login_attempts = 0

    def describe_user(self):
        print(f"Nombre: {self.first_name} {self.last_name}")
        print(f"Edad: {self.age}")
        print(f"Ciudad: {self.city}")

    def greet_user(self):
        print(f"Hola, {self.first_name}. ¡Bienvenido!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def restar_login_attempts(self):
        self.login_attempts = 0

# Uso 9-3
user1 = User("Ben", "Gómez", 20, "CDMX")
user2 = User("Ana", "López", 22, "Monterrey")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

# Login Attempts 9-5
user = user1
user.increment_login_attempts()
user.increment_login_attempts()
print(user.login_attempts)

user.restar_login_attempts()
print(user.login_attempts)

# 9-7 Admin
class Admin(User):
    def __init__(self, first_name, last_name, age, city):
        super().__init__(first_name, last_name, age, city)
        self.privileges = Privileges()

# 9-8 Privilegios
class Privileges:
    def __init__(self):
        self.privileges = [
            "can add post",
            "can delete post",
            "can be user"
        ]

    def show_privileges(self):
        print("Privilegios:")
        for privilege in self.privileges:
            print(f"- {privilege}")

# Creamos el objeto admin
admin = Admin("Ben", "Gómez", 20, "CDMX")

admin.describe_user()
admin.greet_user()
admin.increment_login_attempts()
admin.increment_login_attempts()
print(f"El usuario lleva {admin.login_attempts} intentos de login")
admin.restar_login_attempts()


# Accedemos al objeto Privileges
admin.privileges.show_privileges()
        