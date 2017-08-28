from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from time import sleep
import sys

vertices= ((-1.0,1.0,1.0),(-1.0,-1.0,1.0),(-1.0,-1.0,-1.0),(-1.0,1.0,-1.0),(1.0,-1.0,-1.0),(1.0,-1.0,1.0),(1.0,1.0,-1.0),(1.0,1.0,1.0))

def init():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(1000,1000)
    glutCreateWindow("test")
    glutDisplayFunc(display)
    glutIdleFunc(myidel);
    glClearColor(1.,1.,1.,1.)   #White background
    glColor3f(1.,0.,0.)         #Draw in red
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45.0,1.0/1.0,0.1,100)
    glMatrixMode(GL_MODELVIEW)
    gluLookAt(0,0,1,
              0,0,0,
              0,1,0)
    glPushMatrix()
    glutMainLoop()

def display():
    #glClear()
    i = 0
    glTranslate(-2.5,2.,-15.) #Centering the entire sett of objects
    newObject(GL_LINE_LOOP)
    glTranslate(5.,0.,0.)
    glutWireCube(2.)
    glPushMatrix()
    glPopMatrix()
    glutSwapBuffers()
    return

def myidel():
    variable = 3
    print("kjorer myidle")
    sleep(2)
    glutPostRedisplay();

#3.1
def newObject(openglnotation):
    glBegin(openglnotation)
    for i in range(len(vertices)):
        if i != len(vertices)-1:
            glVertex3fv(vertices[i], vertices[i+1])
        else:
            glVertex3fv(vertices[i], vertices[0])
    glEnd()
init()
