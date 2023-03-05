import math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def f(x):
    return 0.25*x + 3*math.cos(100*x)*math.sin(x)

def draw_axes():
    glColor3f(1, 0, 0)  # Red color for X axis
    glBegin(GL_LINES)
    glVertex2f(-100, 0)
    glVertex2f(100, 0)
    glEnd()
    glColor3f(0, 1, 0)  # Green color for Y axis
    glBegin(GL_LINES)
    glVertex2f(0, -10)
    glVertex2f(0, 10)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0, 0, 1)  # Blue color for function graph
    glBegin(GL_LINE_STRIP)
    for x in range(-200, 201, 1):
        y = f(x/2)
        glVertex2f(x/2, y)
    glEnd()
    draw_axes()
    glFlush()

def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    aspect_ratio = w/h
    glOrtho(-100*aspect_ratio, 100*aspect_ratio, -10, 10, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(800, 600)
glutInitWindowPosition(100, 150)
glutCreateWindow("Lab1_1")
glClearColor(1, 1, 1, 0)
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutMainLoop()
