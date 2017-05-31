import sys

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

eye = [0.0, 0.0, 800.0]
camera = [0.0, 0.0, 0.0]

timer_secs = 10
moveX = 0.0

light_ambient  = [ 0.0, 0.0, 0.0, 1.0 ]
mat_ambient    = [ 0.8, 0.8, 0.8, 1.0 ]

light_diffuse  = [ 1.0, 1.0, 0.0, 1.0 ]
light_position = [ 1.0, 1.0, 0.0, 1.0 ]
mat_diffuse    = [ 0.8, 0.8, 0.8, 1.0 ]

light_specular = [1.0, 1.0, 1.0, 1.0]
mat_specular    = [1.0, 1.0, 1.0, 1.0]
high_shininess  = [10.0] 

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)

    #Window
    glutInitWindowSize(1200,600)
    glutInitWindowPosition(0,0)
    glutCreateWindow("Let see")

    # glEnable(GL_CULL_FACE)
    # glEnable(GL_LIGHTING) 
    # glEnable(GL_LIGHT0)
    # glColorMaterial(GL_FRONT_AND_BACK, GL_EMISSION)
    # glColorMaterial ( GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE ) 
    # glEnable(GL_COLOR_MATERIAL)

    
    glEnable(GL_CULL_FACE)
    glCullFace(GL_FRONT)

    glEnable(GL_DEPTH_TEST)

    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)#Especifica fuente de luz tipo,color
    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)#Especifica a q objetos 

    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)#reflexion, color
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)#especifica la position de la luz
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)

    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, high_shininess)

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)



    #Events
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)

    global timer_secs, moveX
    glutTimerFunc(timer_secs, movimiento, 0)


    #Loop
    glutMainLoop()

def movimiento(value):   
    global timer_secs, moveX,eye,camera

    glutTimerFunc(timer_secs, movimiento, 0)
    
    if moveX < 4550.0:
        moveX += 50.0
        eye[0] = moveX 
        camera[0] = moveX 

        print(str(eye[0]))


    if moveX == 4550:
        movimiento2(0)
    
    glutPostRedisplay()

def movimiento2(value):
    global timer_secs, moveX,eye,camera

    if eye[2] > 300.0:
        glutTimerFunc(1000, movimiento2, 0)
        eye[2] -= 20
        glutPostRedisplay()
    
  



def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    gluLookAt(eye[0], eye[1], eye[2], camera[0],
              camera[1], camera[2], 0.0, 1.0, 0.0)

    glEnable(GL_DEPTH_TEST)

    glPushMatrix()       
    glTranslatef(moveX, 0.0, 0.0)
   #glRotated(20, 0.0, 1.0, 0.0)
    glColor3f(0.0,1.0,0.0)
    glutSolidTeapot(100.0)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(1500.0, 0.0, -600.0)
   #glRotated(20, 0.0, 1.0, 0.0)
    glColor3f(1.0,0.0,0.0)
    glutSolidTeapot(100.0)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(2500.0, 0.0, -600.0)
   #glRotated(20, 0.0, 1.0, 0.0)
    glColor3f(0.0,0.0,1.0)
    glutSolidTeapot(100.0)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(4000.0, 0.0, -400.0)
   #glRotated(20, 0.0, 1.0, 0.0)
    glColor3f(0.0,0.0,1.0)
    glutSolidTeapot(100.0)
    glPopMatrix()

    # glPushMatrix()
    # glTranslatef(0.0, 0.0, 450.0)
    # glColor3f(1.0,0.0,0.0)
    # glutSolidTeapot(100.0)
    # glPopMatrix()

    glFlush()
    glutSwapBuffers()

def reshape(w,h):
    print(str(w))
    print(str(h))
    ar = (w*1.0) / h
    print(str(ar))
    glViewport(0, 0,  w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    #glOrtho(-w, w, -h, h, 1.0, 150.0)
    glFrustum(-ar, ar, -ar, ar, 1.0, 2000.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()



if __name__ == "__main__":
    main()
