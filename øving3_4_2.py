from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from msvcrt import getch
import sys


keyStates = [False for i in range(256)]
vertices= ((-1.0,1.0,1.0),(-1.0,-1.0,1.0),(-1.0,-1.0,-1.0),(-1.0,1.0,-1.0),(1.0,-1.0,-1.0),(1.0,-1.0,1.0),(1.0,1.0,-1.0),(1.0,1.0,1.0))
camera = (0.0, 0.0, 6.0)
running = True

def init():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(1000,1000)
    glutCreateWindow("test")
    glutDisplayFunc(display)
    glClearColor(1.,1.,1.,1.)   #White background
    glColor3f(1.,0.,0.)         #Draw in red
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45.0,1.0/1.0,0.1,100)
    glMatrixMode(GL_MODELVIEW)
    glutKeyboardFunc(keyPressed)
    glutKeyboardUpFunc(keyUp);
    while (running):
        #Handle events
        event =
        '''
        while (window.pollEvent(event)) :
            if (event.type == sf::Event::KeyPressed) :
                if (sf::Keyboard::isKeyPressed(sf::Keyboard::Escape)) :
                    window.close();
                    running = false;
            else if (event.type == sf::Event::MouseMoved) :
                camera.x = 0.01 * -(event.mouseMove.x - static_cast<int>(window.getSize().x) / 2);
                camera.y = 0.01 * (event.mouseMove.y - static_cast<int>(window.getSize().y) / 2);
            else if (event.type == sf::Event::Closed) :
                window.close();
                running = false;
        '''
    gluLookAt(camera.x, camera.y, camera.z, #Camera position in World Space
              camera.x, camera.y, 0.0,      #Camera looks towards this position
              0.0, 1.0, 0.0);               #Up
    glPushMatrix()
    glutMainLoop()

def display():
    i = 0
    glTranslate(-2.5,2.,-15.) #Centering the entire sett of objects
    newObject(GL_LINE_LOOP)
    glTranslate(5.,0.,0.)
    glutWireCube(2.)
    glPushMatrix()
    glPopMatrix()
    glutSwapBuffers()
    return

#3.1
def newObject(openglnotation):
    glBegin(openglnotation)
    for i in range(len(vertices)):
        if i != len(vertices)-1:
            glVertex3fv(vertices[i], vertices[i+1])
        else:
            glVertex3fv(vertices[i], vertices[0])
        print(i)
    glEnd()

def keyPressed (key, x, y):
    keyStates[key] = true; # Set the state of the current key to pressed


def keyUp (key, x, y):
    keyStates[key] = false; # Set the state of the current key to not pressed




init()
