import OpenGL
from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys
import math


def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(-320, 320, -240, 240)

initScale = 0.0
def kotak():
    glColor3f(1.0, 0.75, 0.0)
    glBegin(GL_QUADS)
    glVertex2d(0, 60)
    glVertex2d(50, 60)
    glVertex2d(50, 20)
    glVertex2d(0, 20)
    glEnd()

def kotak2(h):
    glColor3f(1, 0, 0)
    glBegin(GL_QUADS)
    glVertex2d(0, h/2)
    glVertex2d(h/2, 0)
    glVertex2d(0, -h/2)
    glVertex2d(-h/2, 0)
    glEnd()

kx=0;ky=0;speed=10
px=0;py=0
def tampil():
    glClear(GL_COLOR_BUFFER_BIT)
    glPushMatrix()
    glTranslatef(kx,ky,0)
    glColor3f(1,0,0)    
    kotak()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(px,py,0)
    glColor3f(1,0,0)    
    kotak2(100)
    glPopMatrix()

    glFlush()

def keyboard(key,x,y):
    global kx,ky
    if key == b'a':
        kx-=speed
    if key == b'd':
        kx+=speed
    if key == b's':
        ky-=speed
    if key == b'w':
        ky+=speed
def keySpecialFunc(key,x,y):
    global px,py
    if key == GLUT_KEY_LEFT:
        px -= 5
    if key == GLUT_KEY_RIGHT:
        px += 5
    if key == GLUT_KEY_UP:
        py += 5
    if key == GLUT_KEY_DOWN:
        py -= 5
def idle():
    glutPostRedisplay()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(10, 10)
    glutCreateWindow("OpenGL Rizki")
    init()
    glutDisplayFunc(tampil)
    glutKeyboardFunc(keyboard)
    glutSpecialFunc(keySpecialFunc)
    glutIdleFunc(idle)
    glutMainLoop()


main()
