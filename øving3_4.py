from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from time import sleep
import sys

vertices= ((-1.0,1.0,1.0),(-1.0,-1.0,1.0),(-1.0,-1.0,-1.0),(-1.0,1.0,-1.0),(1.0,-1.0,-1.0),(1.0,-1.0,1.0),(1.0,1.0,-1.0),(1.0,1.0,1.0))
auto_rotate = False
def init():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(1000,1000)
    glutCreateWindow("test")
    glTranslate(0.,0.,-10.) #Centering the entire sett of objects
    glClearColor(1.,1.,1.,1.)   #White background
    glColor3f(1.,0.,0.)         #Draw in red
    glutDisplayFunc(display)
    glutIdleFunc(myidel)
    glutMouseFunc(mymouse)
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
    glutWireCube(2.)
    glPushMatrix()
    glPopMatrix()
    glutSwapBuffers()
    return

def myidel():
    sleep(0.01)
    #print(auto_rotate)
    if(auto_rotate):
        glRotatef(1, 3, 1, 1)
    glutPostRedisplay()

def mykey(key,x,y):
    #sleep(0.1)
    print(''.join(["key:",str(key)," x:",str(x)," y:",str(y)]))
    if key == 'w':
        glRotatef(10, 1, 0, 0)
    elif key == 's':
        glRotatef(-10, 1, 0, 0)
    elif key == 'a':
        glRotatef(10, 0, 1, 0)
    elif key == 'd':
        glRotatef(10, 0, 0, 1)
    elif key == 'r':
        #not working
        auto_rotate = True
    elif key == 'q':
        print ("Escape pressed..")
        exit(0)
    glutPostRedisplay()

def mymouse(button, state, x, y):
    print(''.join(["button:",str(button)," x:",str(x)," y:",str(y)]))
    if button == 0:
        glRotatef(10, 1, 0, 0)
    elif button == 2:
        glRotatef(-10, 1, 0, 0)

def newObject(openglnotation):
    glBegin(openglnotation)
    for i in range(len(vertices)):
        if i != len(vertices)-1:
            glVertex3fv(vertices[i], vertices[i+1])
        else:
            glVertex3fv(vertices[i], vertices[0])
    glEnd()
init()
