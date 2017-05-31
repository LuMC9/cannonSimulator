import numpy as np
import objeto as obj

#--------Ejercicio 1----------#
def funcion(p1,p2):
    dt = 0.1

    dx = p2.getX() - p1.getX()
    dy = p2.getY() - p1.getY()

    pc4 = obj.Vertice(p2.getX()+dx, p2.getY() + dy, 0)
    pc1 = obj.Vertice(p1.getX()-dx, p1.getY() - dy, 0 )

    pc2 = obj.Vertice(p1.getX(), (p1.getY() + (dx/4)), 0)

    pc3 = obj.Vertice((p2.getX() - (dx/4)), p2.getY(), 0)

    puntos = bezier(pc1, pc2, pc3, pc4)
	
    i = 0
    for t in np.arange(0.0, 1.0 + dt, dt ):
        print (str(t) + ":")
        print(puntos[i])
        i += 1


def bezier(p1_, p2_, p3_, p4_):
    "Curva bezier"
    _arrCoord = []
    _dt = 0.1
    _mb = np.matrix('-1, 3, -3, 1; 3, -6, 3, 0; -3, 3, 0, 0; 1, 0, 0, 0')
    _gb = np.matrix([[p1_.getX(), p1_.getY(), p1_.getZ()], [p2_.getX(), p2_.getY(), p2_.getZ()],
                     [p3_.getX(), p3_.getY(), p3_.getZ()], [p4_.getX(), p4_.getY(), p4_.getZ()]])
    for __t in np.arange(0.0, 1.0 + _dt, _dt):
        t_matrix = np.matrix([__t**3, __t**2, __t, 1])
        _arrCoord.append(t_matrix * _mb * _gb)
       # print (t_matrix * _mb * _gb)
    
    return _arrCoord

#-----------Ejercicio 2--------------------#
def linea(_p1, _p2, _dt):
    arr = []
    for __t in np.arange(0.0, 1.0 + _dt, _dt):
        if(__t >= 0.5):
            _dt -= 0.1
        print(__t)
        print(_p1.esp() + (__t * (_p2.esp() - _p1.esp())))

#---------------------------------#

def main():
    p1 = obj.Vertice(300, 150, 0)
    p2 = obj.Vertice(400, 350, 0)
    funcion(p1, p2)

   # linea(p1, p2, 0.1)

if __name__ == '__main__': main()

