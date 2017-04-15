import math as m
import sys

import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import objeto as obj

red=1.0
blue=0.0
green=0.0

name = 'glut'
angulo = 0
rX = 0
rY = 0
scale = 0.0
eye = [0.0, 0.0, 300.0]
camera = [0.0, 0.0, 0.0]

light_ambient  = [ 0.0, 0.0, 0.0, 1.0 ]
mat_ambient    = [ 0.8, 0.8, 0.8, 1.0 ]

light_diffuse  = [ 1.0, 1.0, 0.0, 1.0 ]
light_position = [ 1.0, 1.0, 0.0, 1.0 ]
mat_diffuse    = [ 0.8, 0.8, 0.8, 1.0 ]

torus = None

#timer_secs = 10
#cup = None

def main():
	#setup window configuration
	glutInit(sys.argv) # starts up glut for use
	glutInitDisplayMode (GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
	glutInitWindowSize (1200, 700) # window size
	glutInitWindowPosition (0, 0) # initial position of window
	glutCreateWindow (b"Objeto") # Create window
	#end window configuration
	
	setup() #setup initial values
#	glutDisplayFunc(display) # starts the initial drawing

#	glutMainLoop() # glut takes control of program by waiting for new events

	#glShadeModel(GL_FLAT)

	#glEnable(GL_CULL_FACE)
	#glCullFace(GL_FRONT)

	#glEnable(GL_DEPTH_TEST)

	#glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
	#glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)

	#glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
	#glLightfv(GL_LIGHT0, GL_POSITION, light_position)
	#glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)

	#glEnable(GL_LIGHTING)
	#glEnable(GL_LIGHT0)
	#glEnable(GL_COLOR_MATERIAL)
	
	#dona()
	glutDisplayFunc(display) #controla dibujado de pantalla
	glutReshapeFunc(reshape) #controla redimension de pantalla
	glutKeyboardFunc(keyboard) #controla teclado
	#glutTimerFunc(timer_secs, movimiento, 0)	
#	_obj = obj.Objeto(1)
#	_obj.lee_archivo("cube.txt")
#	_obj.imprime_faces()





	glutMainLoop() # take control of program to glut

def setup():
#	glClearColor(1.0, 1.0, 1.0, 1.0) # sets the background color for when you call glClear(COLOR_BUFFER_BIT).
	objeto = obj.Objeto(1)
	objeto.lee_archivo("Naval_cannon.obj")
	global torus
	torus = glGenLists(1)
	glNewList(torus, GL_COMPILE)
	faces = objeto.get_faces()
	for cara in faces:
		glBegin(GL_TRIANGLES)
	#glNormal3f(0.0,0.0,-1.0)
		#glVertex3f( -284.171655,-999.999960, -290.331321)
		#glVertex3f(316.854193, -999.999960,-290.331321)
		#glVertex3f( 316.854193,-31.265704,-290.331321)

	#glVertex3f(0.0,1.0,1.0)
	#glVertex3f(1.0,0.0,0.0)
	#glVertex3f(1.0,0.0,1.0)

	#glVertex3f(1.0,1.0,0.0)
	#glVertex3f(1.0,1.0,1.0)
#	glNormal3f(0.0,0.0,-1.0)
		glVertex3f(cara.arr[0].getX(), cara.arr[0].getY(), cara.arr[0].getZ())
		glVertex3f(cara.arr[1].getX(), cara.arr[1].getY(), cara.arr[1].getZ())
		glVertex3f(cara.arr[2].getX(), cara.arr[2].getY(), cara.arr[2].getZ())
		glEnd()
#	for cara in faces:
#	glBegin(GL_TRIANGLES)
		#glNormal3f()

#	glEnd()
	glEndList()


def reshape(w, h): #2 parametros, alto y ancho
#	ar = (w*1.0) / h

	glViewport(0, 0,  w, h)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	glOrtho(-w, w, -h, h, 1.0, 1000.0)
#	glFrustum(-ar, ar, -ar, ar, 1.0, 1000.0)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()

def display():
#	reshape(300, 300)
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) #------------>

	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	gluLookAt(eye[0], eye[1], eye[2], camera[0], camera[1], camera[2], 0.0, 1.0, 0.0)
#	glPushMatrix()

	global torus
	global angulo
	global rX
	global rY
	global scale

	#glTranslatef(-100.0, 0.0, -50.0)
	glScalef(scale,scale,scale)
	glRotate(angulo, rY, rX , 0)
	glCallList(torus)
	
#	glColor3f (1.0, 1.0, 1.0)
#	glutSolidTeapot(100.0)

#	glTranslate(100.0, 0.0, 50.0)
#	glColor3f(0.0, 1.0, 0.0) 
#	glutSolidTeapot(50.0)
#	global cup
#	glCallList(cup)
#	glColor3f(1.0,0.0,0.0)
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
#	glPopMatrix()

#	glTranslatef(100.0, 0.0, -100.0)
#	glRotated(angulo, 0.0, 1.0, 0.0)
#	glColor3f(0.0, 1.0, 0.0)
#	glutSolidTeapot(80.0)



	#glCallList(torus)
	glFlush()
	glutSwapBuffers()  #----------------------------->

def keyboard(key, x, y):
	global angulo
	global rX
	global rY
	global scale

	if ord(key) == 97: #a->izquierda
		angulo = angulo - 20
		rX = 1
		rY = 0
	if ord(key) == 100: #d->derecha
		rX = 1
		rY = 0
		angulo = angulo + 20
	
	if ord(key) == 119: #w->arriba
		angulo = angulo + 20
		rX = 0
		rY = 1
	if ord(key) == 115: #s->abajo
		angulo = angulo - 20
		rX = 0
		ry = 1

	if ord(key) == 122:
		scale = scale + 5
	if ord(key) == 120:
		scale = scale - 5
	

	glutPostRedisplay()

def drawCircle():
	posX = 0
	posY = 0
	sides = 32
	radius = 50
	glBegin(GL_LINE_LOOP)
	for i in range(100):
		cosine= radius * m.cos(i*2*m.pi/sides) + 50
		sine  = radius * m.sin(i*2*m.pi/sides) + 50
		glVertex2f(cosine,sine)
	glEnd()

def drawTriangle():
	glBegin(GL_TRIANGLES)
	glNormal3f(0.0,0.0,-1.0)
	glVertex3i(50,50,0)
	glVertex3i(70,50,0)
	glVertex3i(60,100,0)
	glEnd()

def dona():
	global torus
	torus = glGenLists(1)
	glNewList(torus, GL_COMPILE)
	drawTriangle()
	#glutSolidTorus(20.4, 2.8, 10, 50)
	glEndList()
	#glNewList(torus, GL_COMPILE)
	#drawTriangle()
	#glEndList()

#def movimiento(value):
	#global angulo

	#glutTimerFunc(timer_secs, movimiento, 0)
	#angulo = angulo + (1.0 if angulo < 360.0 else -360.0)
	#glutPostRedisplay()

if __name__ == '__main__': main()
