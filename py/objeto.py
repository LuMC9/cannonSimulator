"modulo numpy"
import numpy as np
import math as math

class Vertice():
    "Clase que define un Vertice"

    def __init__(self, x, y, z, w=1):
        self.__x = x
        self.__y = y
        self.__z = z
        self.__w = w

    def homog(self):
        "coordenadas homogeneas"
        return np.matrix([[self.__x], [self.__y], [self.__z], [self.__w]])

    def esp(self):
        "coordenadas espaciales"
        return np.matrix([self.__x / self.__w, self.__y / self.__w, self.__z / self.__w])

    def matriz(self):
        return np.matrix([[self.__x], [self.__y], [self.__z]])

    def getX(self):
        "obtiene coordenada X del vertice"
        return self.__x / self.__w

    def getY(self):
        "obtiene coordenada Y del vertice"
        return self.__y / self.__w

    def getZ(self):
        "obtiene coordenada Z del vertice"
        return self.__z / self.__w

class Cara():
    "Cara"

    def __init__(self, arr):
        self.arr = arr
        self.normal = []
        self.__d = []
        self.normalizada = []
        self.set_normal()
        self.set_d()
        self.normaliza()

    def set_normal(self):
        self.normal = np.cross(
            self.arr[1].esp() - self.arr[0].esp(), self.arr[2].esp() - self.arr[0].esp())

    def normaliza(self):
        a = self.normal.item(0) ** 2
        b = self.normal.item(1) ** 2
        c = self.normal.item(2) ** 2
        res = math.sqrt(a+b+c)

        self.normalizada = np.matrix([np.divide(self.normal.item(0),res), np.divide(self.normal.item(1),res), np.divide(self.normal.item(2),res)])



    def set_d(self):
        self.__d = (self.normal * self.arr[2].matriz())

    def impr_ecuacion(self):
        self.set_normal()
        self.set_d()
      #  print(str(self.normal.item(0)) + "x + " + str(self.normal.item(1)) +
       #       "y + " + str(self.normal.item(2)) + "z - " + str(self.__d.item(0)) + " = 0")


class Objeto():
    "Clase que define un objeto"

    def __init__(self, arrayFaces):
        self.vertices = []
        self.faces = []

    def esta_dentro(self, vertex):
        "Valida si un punto se encuentra dentro de un objeto"
        dentro = "si"
        for face in self.faces:
            face.impr_ecuacion()
            res = face.normal.item(0) * vertex.x + face.normal.item(1) * \
                vertex.y + face.normal.item(2) * vertex.z - face.D
            print(res)
            if res > 0:
                dentro = "no"
                break

        print(dentro)

    def lee_archivo(self, name):
        "lee file"
        obj = open(name, 'r')
        arr = obj.readlines()
        verti = []
        for linea in arr:      
            ln = linea.split()
            if ln:
                if ln[0] == 'v':
                    self.vertices.append(Vertice(float(ln[1]), float(ln[2]), float(ln[3])))
                if ln[0] == 'f':
                    for x in range (1, len(ln)):
                        v =  self.vertices[int(ln[x].split('/')[0]) - 1]
                        verti.append(v)
                    self.faces.append(Cara(verti))
                    verti = []

   
    def imprime_faces(self):
        for cara in self.faces:
            cara.impr_ecuacion()
            print(cara.normal)
            print("----------")
            print("[" + str(cara.arr[0].getX()) + " " + str(cara.arr[0].getY()) + " " + str(cara.arr[0].getZ()) + "]"
            + " [" + str(cara.arr[1].getX()) + " " + str(cara.arr[1].getY()) + " " + str(cara.arr[1].getZ()) + "]" 
            + " [" + str(cara.arr[2].getX()) + " " + str(cara.arr[2].getY()) + " " + str(cara.arr[2].getZ()) + "]")
           
    def get_faces(self):
        return self.faces
    # def imprimeVertex(self):
    #     for vert in self.vertices:
    #         print(vert.getX())

def linea(_p1, _p2, _dt):
    "doc"
    for __t in np.arange(0.0, 1.0 + _dt, _dt):
        print(_p1.esp() + (__t * (_p2.esp() - _p1.esp())))

def main():
    "main"
   # _va = Vertice(-1, 3, 7)
   # _vb = Vertice(6, 5, 8)
   # _vc = Vertice(4, 9, -1)
   # _vd = Vertice(2, 2, 2)

   # linea(_va, _vb, 0.1)
    _obj = Objeto(1)
    _obj.lee_archivo("models/cloud.obj")
 #   _obj.imprimeVertex()
    _obj.imprime_faces()
 #   face1 = Cara([_va, _vb, _vc])
    # obj.estaDentro(vd);
    #bj.linea(_va, _vb, .1)


if __name__ == '__main__':
    main()
