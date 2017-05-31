from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
#import obj

name = 'glut'
angulo = 0.0
eye = [0.0, 300.0, -700.0]
camera = [0.0, 0.0, 1.0]

light_ambient = [0.0, 0.0, 0.0, 1.0] #controla cuanta luz ambient existe R,G,B,alfa
mat_ambient = [0.0, 0.0, 0.0, 1.0] # cuanta luz refleja los objetos R,G,B

light_diffuse = [1.0, 1.0, 1.0, 1.0] #De q color es el foco RGB,alfa
light_position = [100.0, 0.0, 0.0, 1.0] #donde esta ubicado el foco x,y,z
mat_diffuse = [0.8, 0.8, 0.8, 1.0] #Material, RGB

timer_secs = 10

tetera1 = None
tetera2 = None

light_specular = [1.0, 1.0, 1.0, 1.0]
mat_specular    = [1.0, 1.0, 1.0, 1.0]
high_shininess  = [10.0] 


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    #GLUT_SINGLE-UTILIZA UN SOLO BUFFER
    #GLUT_DOUBLE-uTILIZA DOS BUFFER
    glutInitWindowSize(300, 300)
    glutInitWindowPosition(200, 0)
    glutCreateWindow("Tetera")

    # glShadeModel(GL_FLAT)

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
    # global tetera1
    # tetera1 = glGenLists(1)
    # glNewList(tetera1, GL_COMPILE)
    # glutSolidTeapot(50.0)
    # glEndList()

    # global tetera2
    # tetera2 = glGenLists(1)
    # glNewList(tetera2, GL_COMPILE)
    # glutSolidTeapot(50.0)
    # glEndList()

    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutTimerFunc(timer_secs, movimiento, 0)

    glutMainLoop()


def reshape(w, h):  #Establece la camara
    ar = (w*1.0) / h

    glViewport(0, 0,  w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
#    glOrtho(-w, w, -h, h, 1.0, 150.0)
    glFrustum(-ar, ar, -ar, ar, 1.0, 800.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def display():
    #	reshape(300, 300)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_MODELVIEW) 
    glLoadIdentity()
    gluLookAt(eye[0], eye[1], eye[2], camera[0],
              camera[1], camera[2], 0.0, 1.0, 0.0)
    glPushMatrix()

    glTranslatef(-200.0, 0.0, 0.0)
    glRotated(angulo, 0.0, 1.0, 0.0)
    glColor3f(0.0, 1.0, 0.0)

   # global tetera1
   # glCallList(tetera1)
    glutSolidTeapot(50.0)
#	glBegin(GL_TRIANGLES)
#	glNormal3f(0.0,0.0,1.0)
#	glVertex3f(0.0,0.0,0.0)
#	glVertex3f(100.0,0.0,0.0)
#	glVertex3f(100.0,100.0,0.0)
#	glEnd()

    glPopMatrix()

#    glPushMatrix()

 #   glTranslatef(150.0, 0.0, -500.0)
  #  glRotated(angulo, 0.0, 1.0, 0.0)
  #  glColor3f(1.0, 0.0, 0.0)
  #  global tetera2
  #  glCallList(tetera2)
  #  glutSolidTeapot(50.0)

  #  glPopMatrix()

    glFlush()
    glutSwapBuffers()


def keyboard(key, x, y):
    if ord(key) == 27:
        sys.exit(0)


def movimiento(value):
    global angulo

    glutTimerFunc(timer_secs, movimiento, 0)
    angulo = angulo + (5.0 if angulo < 360.0 else -360.0)
    glutPostRedisplay()

if __name__ == '__main__':
    main()
