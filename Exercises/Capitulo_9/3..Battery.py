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