from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from time import sleep
import sys
import random

vertices= ((-1.0,1.0,1.0),(-1.0,-1.0,1.0),(-1.0,-1.0,-1.0),(-1.0,1.0,-1.0),(1.0,-1.0,-1.0),(1.0,-1.0,1.0),(1.0,1.0,-1.0),(1.0,1.0,1.0))
auto_rotate = False
mat_ambient = (0.7, 0.7, 0.7, 1.0)
model_ambient = (0.4, 0.4, 0.4, 1.0)
no_mat = (0.0, 0.0, 0.0, 1.0)
mat_ambient = (0.7, 0.7, 0.7, 1.0)
mat_ambient_color = (0.8, 0.8, 0.2, 1.0)
mat_diffuse = (0.1, 0.5, 0.8, 1.0)
mat_specular = (1.0, 1.0, 1.0, 1.0)
no_shininess = 0.0
low_shininess = 5.0
high_shininess = 100.0
mat_emission = (0.3, 0.2, 0.2, 0.0)

def init():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(1000,1000)
    glutCreateWindow("test")
    glTranslate(0.,0.,-5.)             #Centering the entire sett of objects

    glClearColor(1.,1.,1.,1.)           #Background   - (0.90,0.91,0.98,1.)
    glColor3f(1.,0.,0.)                 #Draw in red

    viewpoint = 1                                    #0=infiniteViewpoint, 1=localViewpoint

    #ligthing:
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, model_ambient)     #small white ambient light
    glLightModeli(GL_LIGHT_MODEL_LOCAL_VIEWER, viewpoint)
    #Only outside face because we don't see the inside of the spheres
    glLightModeli(GL_LIGHT_MODEL_TWO_SIDE, 1)
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHTING)
    glEnable(GL_CULL_FACE);

    #Material:
    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, no_mat)
    glMaterialf (GL_FRONT, GL_SHININESS, no_shininess)
    glMaterialfv(GL_FRONT, GL_EMISSION, no_mat)

    #Glut event loops:
    glutDisplayFunc(display)
    glutIdleFunc(myidel)
    #glutMouseFunc(mymouse)
    glutKeyboardFunc(mykey)
    glutMotionFunc(mymotion)

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
    glutSolidCube(2.)
    glPushMatrix()
    glPopMatrix()
    glutSwapBuffers()
    return

def myidel():
    #print(auto_rotate)
    if(auto_rotate):
        glRotatef(1, 3, 1, 1)
    glutPostRedisplay()

def mykey(key,x,y):
    #sleep(0.1)
    #print(''.join(["key:",str(key)," x:",str(x)," y:",str(y)]))
    if key == 'w':
        glRotatef(10, 1, 0, 0)
    elif key == 's':
        glRotatef(10, -1, 0, 0)
    elif key == 'a':
        glRotatef(10, 0, 0, -1)
    elif key == 'd':
        glRotatef(10, 0, 0, 1)
    elif key == 'c':
        glColor3f(random.random(),random.random(),random.random())
    elif key == 'q':
        print ("Q pressed, quiting...")
        exit(0)
    glutPostRedisplay()

def mymouse(button, state, x, y):
    #print(''.join(["button:",str(button)," state:",str(state)," x:",str(x)," y:",str(y)]))
    if button == 0:
        glRotatef(10, 1, 0, 0)
    elif button == 2:
        glRotatef(-10, 1, 0, 0)

def mymotion(x,y):
    #print(''.join(["    x:",str(x)," y:",str(y)]))
    if x<500 and y<500:
        glRotatef(10, -1, -1, 0)
    elif x>500 and y<500:
        glRotatef(10, -1, 1, 0)
    elif x<500 and y>500:
        glRotatef(10, 1, -1, 0)
    elif x>500 and y>500:
        glRotatef(10, 1, 1, 0)
    glutPostRedisplay()

init()
