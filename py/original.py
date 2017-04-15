from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
import numpy as np
import math as m
#import obj

red=1.0
blue=0.0
green=0.0

name = 'glut'
angulo = 0.0
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
	glutInit(sys.argv)
	glutInitDisplayMode (GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
	glutInitWindowSize (300, 300)
	glutInitWindowPosition (0, 0)
	glutCreateWindow (b"Teapot")

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

	glutDisplayFunc(display) #controla dibujado de pantalla
	glutReshapeFunc(reshape) #controla redimension de pantalla
	glutKeyboardFunc(keyboard) #controla teclado
	#glutTimerFunc(timer_secs, movimiento, 0)
	dona()
	glutMainLoop()

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
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	gluLookAt(eye[0], eye[1], eye[2], camera[0], camera[1], camera[2], 0.0, 1.0, 0.0)
#	glPushMatrix()

	global torus

	

	glTranslatef(-100.0, 0.0, -50.0)

	glCallList(torus)
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
	glTranslatef(100.0, 100.0, -50.0)
	glCallList(torus)
	#drawCircle()
#	drawTriangle()
	glTranslatef(100.0, -100.0, -50.0)
	glCallList(torus)
#	drawCircle()
	glTranslatef(-100.0, -100.0, -50.0)
	glCallList(torus)
#	drawCircle()
#	drawTriangle()
#	glPopMatrix()

#	glTranslatef(100.0, 0.0, -100.0)
#	glRotated(angulo, 0.0, 1.0, 0.0)
#	glColor3f(0.0, 1.0, 0.0)
#	glutSolidTeapot(80.0)


	glFlush()
	glutSwapBuffers()

def keyboard(key, x, y):
	if ord(key) == 27:
		glColor3f(0.0, 0.0, 1.0)
	if ord(key) == 114:
		glColor3f(1.0, 0.0, 0.0)
	if ord(key) == 103:
		glColor3f(0.0, 1.0, 0.0)
	if ord(key) == 98:
		glColor3f(0.0, 0.0, 1.0)
	display()

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
	#drawTriangle()
	glutSolidTorus(20.4, 2.8, 10, 50)
	glEndList()
	glNewList(torus, GL_COMPILE)
	drawTriangle()
	glEndList()

#def movimiento(value):
	#global angulo

	#glutTimerFunc(timer_secs, movimiento, 0)
	#angulo = angulo + (1.0 if angulo < 360.0 else -360.0)
	#glutPostRedisplay()

if __name__ == '__main__': main()

