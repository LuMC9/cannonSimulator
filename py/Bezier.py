import TiroParabolico as tr
import objeto as obj


class Bezier():
    def __init__(self, pInicial, pFinal, pControl):
        self.pInicial = (obj.Vertice)pInicial
        self.pFinal = pFinal
        self.pControl = 0.0
        self.mb = np.matrix('-1, 3, -3, 1; 3, -6, 3, 0; -3, 3, 0, 0; 1, 0, 0, 0')
        self.dt = 0.1
        self.gb = 0

        setCurva():

    def set_punto_control(self, hMax): 
        x = self.pFinal.getX() - self.pInicial.getX()
        y = hMax
        self.pControl = obj.Vertice(x,y,0)

    def set_gb(self):
        self.gb = np.matrix([[self.pInicial_.getX(), self.pInicial_.getY(), self.pInicial.getZ()], [self.pControl.getX(), self.pControl.getY(), self.pControl.getZ()],
                    [self.pControl_.getX(), self.pControl.getY(), self.pControl.getZ()], [self.pFinal_.getX(), self.pFinal_.getY(), self.pFinal_.getZ()]])

    def setCurva():
        for t in np.arange(0.0, 1.0 + _dt, _dt):
            t_matrix = np.matrix([t**3, t**2, t, 1])
            _arrCoord.append(t_matrix * self.mb * self.gb)
            print (t_matrix * _mb * _gb)
    
        return _arrCoord


