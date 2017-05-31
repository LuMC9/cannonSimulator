import math as m
import sys

import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from random import randint
from random import *

import random as random

import cannonBall as cB
import curvas as cu
import objeto as obj

#cannonBall
pInicialBall = obj.Vertice(-400,0,0) 
vInicialBall = 90
angulo = 45

#displayLists
cannonList = 1
ballList = 2
treeList = 3
cloudList = 4

#archivos
arch = {"models/Naval_cannon.obj" : cannonList, "models/Cannon Ball.obj" : ballList, "models/EU55_1.obj" : treeList}

red=1.0
blue=0.0
green=0.0

name = 'glut'
rX = 0
rY = 0
scale = 2.0

tX = 0.0
tY = 0.0
tZ = 0.0

cX = 0

eye = [0.0, 0.0, 700.0]
camera = [0.0, 0.0,0.0]

light_ambient  = [ 0.0, 0.0, 0.0, 1.0 ]
mat_ambient    = [ 0.8, 0.8, 0.8, 1.0 ]

light_diffuse  = [ 1.0, 1.0, 0.0, 1.0 ]
light_position = [ 1.0, 1.0, 0.0, 1.0 ]
mat_diffuse    = [ 0.8, 0.8, 0.8, 1.0 ]

light_specular = [1.0, 1.0, 1.0, 1.0]
mat_specular    = [1.0, 1.0, 1.0, 1.0]
high_shininess  = [10.0] 

indice = 0 
timerVel = 1 #velocidad timer
#timer_secs = 10
#cup = None

band = 0
angBall = 0

zoomOff = 1300
numArboles = 15

arbolesArr = []
colorArr = []

def main():
	#setup window configuration
	glutInit(sys.argv) # starts up glut for use
	glutInitDisplayMode (GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
	glutInitWindowSize (1200, 700) # window size
	glutInitWindowPosition (0, 0) # initial position of window
	glutCreateWindow (b"Objeto") # Create window
	#end window configuration
	
	
	# glEnable(GL_CULL_FACE)
	# glCullFace(GL_FRONT)

	# glEnable(GL_DEPTH_TEST)

	# glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)#Especifica fuente de luz tipo,color
	# glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)#Especifica a q objetos 

	# glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)#reflexion, color
	# glLightfv(GL_LIGHT0, GL_POSITION, light_position)#especifica la position de la luz
	# glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)

	# glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
	# glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
	# glMaterialfv(GL_FRONT, GL_SHININESS, high_shininess)

	# glEnable(GL_LIGHTING)
	# glEnable(GL_LIGHT0)
	# glEnable(GL_COLOR_MATERIAL)


	setup() #setup initial values
	

	glutDisplayFunc(display) #controla dibujado de pantalla
	glutReshapeFunc(reshape) #controla redimension de pantalla
	glutKeyboardFunc(keyboard) #controla teclado

	generaArboles()
	#traslada(indice)


	glutMainLoop() # take control of program to glut

def display():
#	reshape(300, 300)

	global torus
	global angulo
	global tX, tY, indice, cannon, cannonBall, ballList, cannonList
	global eye, camera, band, arbolesArr, angBall,colorArr
	global scaleBall
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) #------------>



	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	gluLookAt(eye[0], eye[1], eye[2], camera[0], camera[1], camera[2], 0.0, 1.0, 0.0)


	#generaArboles()
	it = 0
	for x in arbolesArr:
		glPushMatrix()
		glColor3f(colorArr[it][0] ,colorArr[it][1],colorArr[it][2])
		glTranslatef(x.getX(), 0, x.getZ())
		glRotated(-90, 1.0, 0.0, 0.0)
		glScalef(100.0, 100.0, 100.0)
		glCallList(treeList)
		glPopMatrix()
		it += 1


	glPushMatrix()
	glColor3f(0.0,1.0,0.0)
	glTranslatef(tX,tY,650.0)

	glScalef(50.0, 50.0, 50.0)
	glRotate(90+angBall,0,1,0)
	glCallList(ballList)
	glPopMatrix()
	
	angBall += 2

	glPushMatrix()
	glColor3f(1.0,0.0,0.0)
	glTranslatef(-400.0,0.0, 0.0)
	glScalef(1.5,1.5,1.5)
	glRotate(90,0,1,0)
	glRotate(-(int(angulo))+20, 1, 0 , 0)

	glCallList(cannonList)
	glPopMatrix()




	glFlush()

	glutSwapBuffers()  #----------------------------->

def setup():
	#glClearColor(34.0, 177.0, 76.0, 0.0) # sets the background color for when you call glClear(COLOR_BUFFER_BIT).
	global cannon, cannonBall, ballList, angulo, vInicialBall, tX, tY
	i = 1
	np.seterr(divide='ignore', invalid='ignore')

	cannonBall = cB.CannonBall(pInicialBall, float(vInicialBall), float(angulo))
	cannonBall.calculaPuntosCurva()

	print("Angulo: " + str(angulo))
	print("Vel. inicial:" + str(vInicialBall))
	print("--------------------------")
	print("Alcance: " + str(cannonBall.TiroParabolico.alcance))
	print("Altura Max: " + str(cannonBall.TiroParabolico.alturaMax))	
	print("--------------------------")

	for x in arch:
		carga_objeto(arch[x],  x)



def carga_objeto(id, file):	
	#Lee archivo obj
	objeto = obj.Objeto(1)
	#print (file)
	#print ('Cargando')
	objeto.lee_archivo(file)
	#print ('Juega.!')
	setDisplayList(id, objeto)

def setDisplayList(id, objeto):
	#Carga la geometria del objeto leido en una display list
	global tX, tY, tZ, indice, ballList, cannonList

	faces = objeto.get_faces()

	if id == ballList:

		id = glGenLists(1)
		glNewList(id, GL_COMPILE)
		glPushMatrix()
		#glScalef(100.0,100.0,100.0)
	
	

		for cara in faces:
			glBegin(GL_POLYGON)
			glNormal3f(cara.normalizada.item(0),cara.normalizada.item(1),cara.normalizada.item(2))
			for x in range(0, len(cara.arr)):
				glVertex3f(cara.arr[x].getX(), cara.arr[x].getY(), cara.arr[x].getZ())
			glEnd()
		glPopMatrix()
		glEndList()
	#Termina display list

	if id == cannonList:

		id = glGenLists(1)
		glNewList(id, GL_COMPILE)
		glPushMatrix()
		#glTranslatef(100.0, 0.0, 0.0)
		# glRotate(90, 0, 1 , 0)
		# glRotate(-angulo+20, 1, 0 , 0)
	#	glScalef(1.0,1.0,1.0)
		
		for cara in faces:
			glBegin(GL_POLYGON)
			glNormal3f(cara.normalizada.item(0),cara.normalizada.item(1),cara.normalizada.item(2))
			for x in range(0, len(cara.arr)):
				glVertex3f(cara.arr[x].getX(), cara.arr[x].getY(), cara.arr[x].getZ())
			glEnd()
		glPopMatrix()

		glEndList()
	#Termina display list

	if id == treeList:
		id = glGenLists(1)
		glNewList(id, GL_COMPILE)
		glPushMatrix()
		#glRotated(-90,1,0,0)

		#glScalef(250.0,250.0,250.0)

		for cara in faces:
			glBegin(GL_TRIANGLE_FAN)
			glNormal3f(cara.normalizada.item(0),cara.normalizada.item(1),cara.normalizada.item(2))

			for x in range(0, len(cara.arr)):
				glVertex3f(cara.arr[x].getX(), cara.arr[x].getY(), cara.arr[x].getZ())

			#glVertex3f(cara.arr[0].getX(), cara.arr[0].getY(), cara.arr[0].getZ())
			#glVertex3f(cara.arr[1].getX(), cara.arr[1].getY(), cara.arr[1].getZ())
			#glVertex3f(cara.arr[2].getX(), cara.arr[2].getY(), cara.arr[2].getZ())
			glEnd()
		glPopMatrix()
		glEndList()

	
	if id == cloudList:
		id = glGenLists(1)
		glNewList(id, GL_COMPILE)
		glPushMatrix()
		#glRotated(-90,1,0,0)

		#glScalef(250.0,250.0,250.0)

		for cara in faces:
			glBegin(GL_TRIANGLE_FAN)
		#glNormal3f(0.0,0.0,-1.0)
			for x in range(0, len(cara.arr)):
				glVertex3f(cara.arr[x].getX(), cara.arr[x].getY(), cara.arr[x].getZ())

			#glVertex3f(cara.arr[0].getX(), cara.arr[0].getY(), cara.arr[0].getZ())
			#glVertex3f(cara.arr[1].getX(), cara.arr[1].getY(), cara.arr[1].getZ())
			#glVertex3f(cara.arr[2].getX(), cara.arr[2].getY(), cara.arr[2].getZ())
			glEnd()
		glPopMatrix()
		glEndList()

def reshape(w, h): #2 parametros, alto y ancho
	ar = (w*1.0) / h


	

	glViewport(0, 0,  w, h)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()

	#glOrtho(-w, w, -h, h, 1.0, 150.0)


	glFrustum(-ar, ar, -ar, ar, 1.0, 5000.0)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()

def traslada(value):
	global tX, tY, indice, cannonBall
	global eye, camera, zoomOff

	vertex = cannonBall.puntos[value]

	tX = vertex.item(0)
	tY = vertex.item(1)	

	eye[0] = tX 
	eye[1] = tY
	camera[0] = tX
	camera[1] = tY

	value += 1
	if value < len(cannonBall.puntos):
		glutTimerFunc(timerVel, traslada,value)	
	
	if value == len(cannonBall.puntos):
		tX += 10
		tY -= 15.0
		aleja(zoomOff)

	glutPostRedisplay()

def aleja(value):
	global eye, scaleBall, zoomOff
	if eye[2] < value:
		eye[2] += 50
		glutTimerFunc(1, aleja, zoomOff)

	glutPostRedisplay()



def keyboard(key, x, y):
	global angulo
	global rX
	global rY
	global scale
	global vInicialBall
	global cannonBall

	if ord(key) == 97: #a->izquierda
		angulo = angulo - 20
		rX = 1
		rY = 0
	if ord(key) == 100: #d->derecha
		rX = 1
		rY = 0
		angulo = angulo + 20
	
	if ord(key) == 119: #w->arriba
		angulo = input("Angulo: ")
		vInicialBall = input("Vel. inicial: ")

		cannonBall = cB.CannonBall(pInicialBall, float(vInicialBall), float(angulo))
		cannonBall.calculaPuntosCurva()
		print("Alcance: " + str(cannonBall.TiroParabolico.alcance))
		print("Altura Max: " + str(cannonBall.TiroParabolico.alturaMax))
		print("--------------------------")

		reiniciar()

	if ord(key) == 115: #s->abajo
		reiniciar()

	if ord(key) == 122:
		scale = scale + 5
	if ord(key) == 120:
		scale = scale - 5
	

	glutPostRedisplay()

def generaArboles():
	xpos = 500.0
	global arbolesArr
	global colorArr, numArboles
	colorRGB = []
	for x in range(0, numArboles):
		r = random.uniform(0,1)
		g = random.uniform(0,1)
		b = random.uniform(0,1)
		arbolesArr.append(obj.Vertice(xpos,0,randint(-400,800)))
		colorRGB = [r,g,b]
		colorArr.append(colorRGB)
		xpos += 300


def reiniciar():
	global indice,eye,camera,angBall
	eye[0] = 0
	camera[0] = 0
	eye = [0.0,0.0,700.0]
	camera = [0.0,0.0,0.0]
	angBall = 0
	traslada(indice)

def linea(_p1, _p2, _dt):
	arr = []
	for __t in np.arange(0.0, 1.0 + _dt, _dt):
		print(_p1.esp() + (__t * (_p2.esp() - _p1.esp())))
		arr.append(_p1.esp() + (__t * (_p2.esp() - _p1.esp())))

	return arr

if __name__ == '__main__': main()
