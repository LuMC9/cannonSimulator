from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import objeto as obj

import curvas as cu

p1 = obj.Vertice(0,0,0)
p2 = obj.Vertice(0,0,0)
pc1 = obj.Vertice(0,0,0)
pc4 = obj.Vertice(0,0,0)
pc2 = obj.Vertice(0,0,0)
pc3 = obj.Vertice(0,0,0)
puntos = []

def main():
    #setup window configuration
    glutInit(sys.argv) # starts up glut for use
    glutInitDisplayMode (GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize (1366, 700) # window size
    glutInitWindowPosition (0, 0) # initial position of window
    glutCreateWindow (b"Objeto") # Create window
    #end window configuration
    setup()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMainLoop()

def setup():
 #   glClearColor(1.0, 1.0, 1.0, 1.0
    global p1, p2, pc1, pc4, pc2, pc3
    p1 = obj.Vertice(300, 150, 0)
    p2 = obj.Vertice(400, 350, 0)

    funcion(p1, p2)

def reshape(w, h): #2 parametros, alto y ancho
#	ar = (w*1.0) / h

	glViewport(0, 0,  w, h)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	glOrtho(0, w, -h, h, 1.0, 1000.0)
#	glFrustum(-ar, ar, -ar, ar, 1.0, 1000.0)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()

def display():
#	reshape(300, 300)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    #	gluLookAt(eye[0], eye[1], eye[2], camera[0], camera[1], camera[2], 0.0, 1.0, 0.0)
    #	glPushMatrix()

    global torus, p1,p2,pc1,pc4, pc2, pc3



    glTranslatef(100.0, 0.0, -50.0)

    #	glCallList(torus)
    #	glRotated(angulo, 0.0, 1.0, 0.0)
    #	glColor3f(0.0, 0.0, 1.0)
    #	glutSolidTeapot(100.0)

    #	glTranslate(100.0, 0.0, 50.0)
    #	glColor3f(0.0, 1.0, 0.0) 
    #	glutSolidTeapot(50.0)
    #	global cup
    #	glCallList(cup)
    #	glColor3f(red,green,blue)
    #	drawTriangle()
    #	drawCircle()
    #	glTranslatef(100.0, 100.0, -50.0)
    #	glCallList(torus)
    #drawCircle()
    #	drawTriangle()
    #	glTranslatef(100.0, -100.0, -50.0)
    #	glCallList(torus)
    #	drawCircle()
    #	glTranslatef(-100.0, -100.0, -50.0)
    #	glCallList(torus)
    #	drawCircle()
    #	drawTriangle()
    #glPopMatrix()
    glPointSize(10.0)
    # glBegin(GL_POINTS)
    # #glNormal3f(0.0,0.0,-1.0)
    # glVertex3f(p1.getX(),p1.getY(),0.0)
    # glVertex3f(p2.getX(),p2.getY(),0.0)
    # glVertex3f(pc4.getX(),pc4.getY(),0.0)
    # glVertex3f(pc1.getX(),pc1.getY(),0.0)

    # glVertex3f(pc2.getX(),pc2.getY(),0.0)
    # glVertex3f(pc3.getX(),pc3.getY(),0.0)

    # glEnd()


    for vertex in puntos:
        glBegin(GL_POINTS)
        glVertex3f(vertex.item(0), vertex.item(1), 0)
        glEnd()
    #	glTranslatef(100.0, 0.0, -100.0)
    #	glRotated(angulo, 0.0, 1.0, 0.0)
    #	glColor3f(0.0, 1.0, 0.0)
    #	glutSolidTeapot(80.0)


    glFlush()
    glutSwapBuffers()

def funcion(p1,p2):
    global pc1, pc4, pc2, pc3, puntos
    dx = p2.getX() - p1.getX()
    dy = p2.getY() - p1.getY()

    pc4 = obj.Vertice(p2.getX()+dx, p2.getY() + dy, 0)
    pc1 = obj.Vertice(p1.getX()-dx, p1.getY() - dy, 0 )

    pc2 = obj.Vertice(p1.getX(), (p1.getY() + (dx/4)), 0)

    pc3 = obj.Vertice((p2.getX() - (dx/4)), p2.getY(), 0)

    puntos = cu.bezier(pc1, pc2, pc3, pc4 )

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
        print (t_matrix * _mb * _gb)
    
    return _arrCoord





if __name__ == '__main__': main()
