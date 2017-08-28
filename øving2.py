from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
import random as rand

def myinit():
    glClearColor(1.,1.,1.,1.)   #White background
    glColor3f(1.,0.,0.)         #Draw in red
    glMatrixMode(GL_PROJECTION)
    #glLoadIdentity()
    gluPerspective(45.0,1.0/1.0,0.1,100)
    glMatrixMode(GL_MODELVIEW)
    gluLookAt(0,0,1,
              0,0,0,
              0,1,0)


def display():
    vertices =((0.,0.),(25.,50),(50.,0.))
    p = list([7.5,5.0])
    glClear(GL_COLOR_BUFFER_BIT)
    glTranslate(-25.,-25.,-90.)

    # drawing the edge of the triangle
    #glBegin(GL_POLYGON)
    #glVertex2fv((0.,0.),(0.,50.))
    #glVertex2fv((0.,50.),(50.,50.))
    #glVertex2fv((50.,50.),(50.,0.))
    #glVertex2fv((50.,0.),(0.,0.))
    #glEnd()

    glBegin(GL_POINTS)
    for k in range(100000):
        j = rand.choice([0,1,2])

        p[0] = (p[0]+vertices[j][0])/2.0
        p[1] = (p[1]+vertices[j][1])/2.0
        glVertex2fv(p)

    glEnd()
    glPushMatrix()
    glPopMatrix()
    glutSwapBuffers()
    return



glutInit(sys.argv)
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(1000,1000)
glutInitWindowPosition(0,0)
glutCreateWindow("Sierpinski Gasket")
glutDisplayFunc(display)
myinit()
glutMainLoop()
