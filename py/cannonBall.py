import curvas as bezier
import TiroParabolico as tp
import objeto as obj

class CannonBall():

    def __init__(self, pInicial, vInicial, angulo):
        self.puntos = []
        self.pInicial = pInicial
        self.pFinal = 0.0
        self.pControl = 0.0
        self.pActual = 0.0
        self.TiroParabolico = tp.TiroParabolico(vInicial, angulo)

    def set_pInicial(self,puntoInicial):
        self.pInicial = puntoInicial

    def set_pFinal(self):
        alcance = self.TiroParabolico.set_alcance() + self.pInicial.getX()
        self.pFinal = obj.Vertice(alcance, self.pInicial.getY(), self.pInicial.getZ())
     #   print (alcance)

    def set_pControl(self):
        x = (self.pFinal.getX() + self.pInicial.getX()) / 2 
        y =  self.TiroParabolico.set_altura() + self.pInicial.getY()
       # print (y)
        self.pControl = obj.Vertice(x,y,0)

    def calculaPuntosCurva(self):
        self.set_pFinal()
        self.set_pControl()
        self.puntos = bezier.bezier(self.pInicial, self.pControl, self.pControl, self.pFinal)
