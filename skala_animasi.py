import OpenGL
from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys
import math


def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(0.0, 500.0, 0.0, 500.0)


def drawQuads():
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(1.0, 0.75, 0.0)
    glBegin(GL_QUADS)
    glVertex2i(300, 300)
    glVertex2i(100, 300)
    glVertex2i(100, 400)
    glVertex2i(300, 400)
    glEnd()
 

initScale = 0.0
def animScale():
    global initScale
    glPushMatrix()
    glScale(initScale,initScale,0)
    drawQuads()
    initScale+=0.25
    glPopMatrix()
    glFlush()

def Timer():
    glutPostRedisplay()
    glutTimerFunc(10,Timer,5)
    glFlush()


def render():
    glClear(GL_COLOR_BUFFER_BIT)
    animScale()
    glFlush()
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(10, 10)
    glutCreateWindow("OpenGL Rizki")
    glutDisplayFunc(render)
    glutTimerFunc(10,Timer,5)
    init()
    glutMainLoop()


main()
