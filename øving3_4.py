from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from time import sleep
import sys

vertices= ((-1.0,1.0,1.0),(-1.0,-1.0,1.0),(-1.0,-1.0,-1.0),(-1.0,1.0,-1.0),(1.0,-1.0,-1.0),(1.0,-1.0,1.0),(1.0,1.0,-1.0),(1.0,1.0,1.0))
dt = 0.
def init():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(1000,1000)
    glutCreateWindow("test")
    glTranslate(-2.5,2.,-15.) #Centering the entire sett of objects
    glutDisplayFunc(display)
    #glutIdleFunc(myidel)
    glutKeyboardFunc(mykey)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45.0,1.0/1.0,0.1,100)
    glMatrixMode(GL_MODELVIEW)
    gluLookAt(0,0,1,
              0,0,0,
              0,1,0)
    glPushMatrix()
    glutMainLoop()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glClearColor(1.,1.,1.,1.)   #White background
    glColor3f(1.,0.,0.)         #Draw in red
    #glRotatef(1, 3, 1, 1)
    glutWireCube(2.)
    glPushMatrix()
    glPopMatrix()
    glutSwapBuffers()
    return

def myidel():
    sleep(0.1)
    glutPostRedisplay()

def mykey(key,x,y):
    sleep(0.1)
    print(''.join(["key:",str(key)," x:",str(x)," y:",str(y)]))
    if key=='w':
        glRotatef(10, 1, 0, 0)
        print ("w pressed")
    elif key == 's':
        glRotatef(-10, 1, 0, 0)
        print ("s pressed")
    elif key == 'a':
        glRotatef(10, 0, 1, 0)
        print ("a pressed")
    elif key == 'd':
        glRotatef(10, 0, 0, 1)
        print ("d pressed")
    glutPostRedisplay()

def newObject(openglnotation):
    glBegin(openglnotation)
    for i in range(len(vertices)):
        if i != len(vertices)-1:
            glVertex3fv(vertices[i], vertices[i+1])
        else:
            glVertex3fv(vertices[i], vertices[0])
    glEnd()
init()
