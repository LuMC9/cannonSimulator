"modulo numpy"
import numpy as np
import objeto as g


def hermite(p1_, p4_, r1_, r4_):
    "Curva hermite"
    _dt = 0.1
    _mh = np.matrix('2, -2, 1, 1; -3, 3, -2, -1; 0, 0, 1, 0; 1, 0, 0, 0')
    _gh = np.matrix([[p1_.getX(), p1_.getY(), p1_.getZ()], [p4_.getX(), p4_.getY(), p4_.getZ()],
                     [r1_.getX(), r1_.getY(), r1_.getZ()], [r4_.getX(), r4_.getY(), r4_.getZ()]])
    for __t in np.arange(0.0, 1.0 + _dt, _dt):
        t_matrix = np.matrix([__t**3, __t**2, __t, 1])
        print(t_matrix * _mh * _gh)


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
     #   print (t_matrix * _mb * _gb)
    
    return _arrCoord


def main():
    "main"
    _p1 = g.Vertice(1, 2, 3)
    _p4 = g.Vertice(4, 5, 6)
    _r1 = g.Vertice(5, 3, 6)
    _r4 = g.Vertice(1, 4, 6)

  #  print("HERMITE:")
   # hermite(_p1, _p4, _r1, _r4)
    print("\nBEZIER:")
    bezier(_p1, _p4, _r1, _r4)


if __name__ == "__main__":
    main()
