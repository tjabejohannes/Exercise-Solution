from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
import random


def init():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(1000,1000)
    glutCreateWindow("test")
    glTranslate(0.,0.,-25.)             #Centering the entire sett of objects

    #glClearColor(1.,1.,1.,1.)           #Background   - (0.90,0.91,0.98,1.)
    glColor3f(1.,0.,0.)                 #Draw in red

    #init_lighting()

    #Glut event loops:
    glutDisplayFunc(display)
    #glutIdleFunc(myidel)
    #glutMouseFunc(mymouse)
    glutKeyboardFunc(mykey)
    #glutMotionFunc(mymotion)

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
    cube_ring()
    glutSwapBuffers()
    return

def init_lighting():
    #viewpoint = 1                                    #0=infiniteViewpoint, 1=localViewpoint

    #ligthing:
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, model_ambient)     #small white ambient light
    glLightModeli(GL_LIGHT_MODEL_LOCAL_VIEWER, viewpoint)
    #Only outside face because we don't see the inside of the spheres
    glLightModeli(GL_LIGHT_MODEL_TWO_SIDE, 1)
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHTING)
    glEnable(GL_CULL_FACE)

    #Material:
    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, no_mat)
    glMaterialf (GL_FRONT, GL_SHININESS, no_shininess)
    glMaterialfv(GL_FRONT, GL_EMISSION, no_mat)
    return

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

def cube():
    glutSolidCube(2.)

    return

def cube_ring():
    glPushMatrix()
    glClear(GL_COLOR_BUFFER_BIT)
    for i in range(9):
        glColor3f(random.random(),random.random(),random.random())
        if i%2 == 0:
            glRotatef(90, 1, 0, 0)
        cube()
        glTranslate(-5.,0.,0.)
    glPopMatrix()
    return

init()
