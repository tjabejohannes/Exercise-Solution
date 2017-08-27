from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys

vertices= ((0.0,2.0,0.0),(1.5,1.5,0.0),(2.0,0.0,0.0),(1.5,-1.5,0.0),(0.0,-2.0,0.0),(-1.5,-1.5,0.0),(-2.0,0.0,0.0),(-1.5,1.5,0.0))

# not included GL_POINTS!
methods = (GL_LINES, GL_LINE_STRIP, GL_LINE_LOOP,GL_TRIANGLES, GL_TRIANGLE_STRIP, GL_TRIANGLE_FAN,GL_QUADS, GL_QUAD_STRIP, GL_POLYGON )

def init():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(800,600)
    glutCreateWindow("test")

    glutDisplayFunc(display)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45.0,4.0/3.0,0.1,100)
    glMatrixMode(GL_MODELVIEW)
    gluLookAt(0,0,1,
              0,0,0,
              0,1,0)
    glPushMatrix()
    glutMainLoop()

def display():
    i = 0
    glTranslate(-10.,5.,-25.)
    for glnotation in methods:
        newObject(glnotation)
        if i==4:
            glTranslate(-15.0,-5.0,0.0)
        else:
            glTranslate(5.0,0.0,0.0)
        i += 1

    glPushMatrix()
    glPopMatrix()
    glutSwapBuffers()
    return

def newObject(openglnotation):
    glBegin(openglnotation)
    for i in range(len(vertices)-1):
        glVertex3fv(vertices[i], vertices[i+1])

    glEnd()

init()
