import math as math
import numpy as np

class TiroParabolico():

    def __init__(self, vo, angulo):
        self.vo = vo
        self.angulo = angulo
        self.alcance = 0.0
        self.alturaMax = 0.0
        self.gravedad = 9.81

    def set_alcance(self):
        "Establece el alcance maximo del objeto"
        self.alcance = (self.vo**2 * math.sin(math.radians(2 * self.angulo))) / self.gravedad
        return self.alcance

    def set_altura(self):
        "Establece la altura maxima del objeto"
        self.alturaMax = ((self.vo * math.sin(math.radians(self.angulo)))**2) / (2 * self.gravedad)
        return self.alturaMax
