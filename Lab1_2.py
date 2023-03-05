from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

# Define the vertices of the object in counter-clockwise order
vertices = np.array([(50, 35), (50, 55), (40, 45), (60, 45), (50, 55)], dtype=np.float32)

def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    
    # Set up the orthogonal projection matrix based on the bounding box of the object
    x_min, y_min = np.min(vertices, axis=0)
    x_max, y_max = np.max(vertices, axis=0)
    aspect = w / h
    if aspect >= 1:
        # Landscape orientation
        scale = 100 / (x_max - x_min)
        x_mid = (x_min + x_max) / 2
        y_mid = (y_min + y_max) / 2
        width = scale * (x_max - x_min)
        height = width / aspect
        bottom = y_mid - height / 2
        top = y_mid + height / 2
        glOrtho(x_mid - width / 2, x_mid + width / 2, bottom, top, -1, 1)
    else:
        # Portrait orientation
        scale = 100 / (y_max - y_min)
        x_mid = (x_min + x_max) / 2
        y_mid = (y_min + y_max) / 2
        height = scale * (y_max - y_min)
        width = height * aspect
        left = x_mid - width / 2
        right = x_mid + width / 2
        glOrtho(left, right, y_mid - height / 2, y_mid + height / 2, -1, 1)
    
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def display():
    glClearColor(1, 1, 1, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0, 0, 0)
    glBegin(GL_LINE_STRIP)
    for vertex in vertices:
        glVertex2f(*vertex)
    glEnd()
    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(800, 600)
    glutInitWindowPosition(100, 150)
    glutCreateWindow("Lab1_2")
    glutReshapeFunc(reshape)
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == '__main__':
    main()
