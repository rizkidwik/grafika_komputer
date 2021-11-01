from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

l=1;

def titik():
    glColor3f(1,1,0)
    glPointSize(l)
    glBegin(GL_POINTS)
    glVertex2i(500,240)
    glEnd()

def tampil():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    titik()
    glutSwapBuffers()
    

def mouse(button,state,x,y):
    global l
    if button==GLUT_LEFT_BUTTON and state==GLUT_DOWN:
        l += 1
    if button==GLUT_RIGHT_BUTTON and state==GLUT_DOWN:
        l -= 1
    

def idle():
    glutPostRedisplay()

def init():
    glClearColor(0.3,0.3,0.3,0)
    gluOrtho2D(0,1024,512,0)    

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(1024, 512)
    window = glutCreateWindow("OpenGL Rizki - Mouse")
    init()
    glutDisplayFunc(tampil)
    glutMouseFunc(mouse)
    glutIdleFunc(idle)
    glutMainLoop()


main()