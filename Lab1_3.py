import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def draw_initials():
    # M
    glBegin(GL_LINES)
    glVertex3f(-0.7, -0.5, 0.0)
    glVertex3f(-0.7, 0.5, 0.0)
    glVertex3f(-0.7, 0.5, 0.0)
    glVertex3f(-0.4, 0.0, 0.0)
    glVertex3f(-0.4, 0.0, 0.0)
    glVertex3f(-0.1, 0.5, 0.0)
    glVertex3f(-0.1, 0.5, 0.0)
    glVertex3f(-0.1, -0.5, 0.0)
    glEnd()

    # S
    glBegin(GL_LINE_STRIP)
    glVertex3f(0.6, 0.5, 0.0)
    glVertex3f(0.3, 0.5, 0.0)
    glVertex3f(0.3, 0.0, 0.0)
    glVertex3f(0.6, 0.0, 0.0)
    glVertex3f(0.6, -0.5, 0.0)
    glVertex3f(0.3, -0.5, 0.0)
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0,0.0,-2.5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        draw_initials()
        pygame.display.flip()
        pygame.time.wait(10)

main()
