import OpenGL
from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys
import math


def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(0.0, 1400, 0.0, 1000)


def rumah():
    # ATAP
    glColor3f(1, 0, 1)
    glBegin(GL_TRIANGLES)
    glVertex2i(100, 350)
    glVertex2i(400, 550)
    glVertex2i(700, 350)
    glEnd()
    
    # DINDING
    glColor3f(1, 0, 0)
    glBegin(GL_QUADS)
    glVertex2i(130, 350)
    glVertex2i(130, 100)
    glVertex2i(670, 100)
    glVertex2i(670, 350)
    glEnd()

    # PINTU
    glColor3f(1, 0, 1)
    glBegin(GL_QUADS)
    glVertex2i(150, 250)
    glVertex2i(150, 100)
    glVertex2i(250, 100)
    glVertex2i(250, 250)
    glEnd()

    glColor3f(0, 0, 1)
    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex2i(170, 170)
    glEnd()

    # JENDELA
    glColor3f(0.2, 0.4, 0.3)
    glBegin(GL_QUADS)
    glVertex2i(330, 320)
    glVertex2i(450, 320)
    glVertex2i(450, 230)
    glVertex2i(330, 230)
    glEnd()

    glColor3f(0.1, 0.7, 0.5)
    glLineWidth(3)
    glBegin(GL_LINES)
    glVertex2i(390, 320)
    glVertex2i(390, 230)
    glVertex2i(330, 273)
    glVertex2i(450, 273)
    glEnd()

    glColor3f(0.2, 0.4, 0.3)
    glBegin(GL_QUADS)
    glVertex2i(530, 320)
    glVertex2i(650, 320)
    glVertex2i(650, 230)
    glVertex2i(530, 230)
    glEnd()

    glColor3f(0.1, 0.7, 0.5)
    glLineWidth(3)
    glBegin(GL_LINES)
    glVertex2i(590, 320)
    glVertex2i(590, 230)
    glVertex2i(530, 273)
    glVertex2i(650, 273)
    glEnd()
 

def render():
    glClear(GL_COLOR_BUFFER_BIT)
    rumah()
    glPushMatrix()
    glTranslate(800, 400, 0)
    glRotatef(50, 0, 0, 1)
    glScalef(0.75, 0.75, 0)
    rumah()
    glPopMatrix()
    glFlush()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(10, 10)
    glutCreateWindow("OpenGL Rizki")
    glutDisplayFunc(render)
    init()
    glutMainLoop()


main()
