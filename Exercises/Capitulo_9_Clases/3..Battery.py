# Bloque 4: Clases como Atributos(Composicion)
# Mejora la bateria: En lugar de poner toda la clase Car vista en la leccion
# creamos una clase Battery
# 9-9 Battery Upgrade
class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100

""" Consejo Pro: Convenciones de Nombres
En Python, seguimos la guía PEP 8:

Clases: Usan CapWords (o PascalCase). Ejemplo: ElectricCar.

Funciones y Variables: Usan snake_case. Ejemplo: set_number_served.

Esto ayuda a diferenciar de un vistazo si estás llamando a una clase o a una función. """