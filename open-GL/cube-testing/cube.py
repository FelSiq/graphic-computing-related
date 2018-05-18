from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

angle=0
inc=1

def timer(val):
	global angle
	angle += inc
	display()
	glutTimerFunc(30, timer, 0)

def init():
	glClearColor(0, 0, 0, 0)

def display():
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glViewport(0, 0, 640, 480)

	glColor3f(1, 1, 1)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	glOrtho(-2, 2, -2, 2, -2, 100)
	
	glMatrixMode(GL_MODELVIEW)

	gluLookAt(0, 0, 1, 0, 0, 0, 0, 1, 0)
	glRotatef(angle, 1, 1, 1)
	glutSolidCube(1.5)

	glFlush()

if __name__ == '__main__':
	glutInit()
	glutInitWindowSize(640, 480)
	glutCreateWindow('')
	
	init()

	glutDisplayFunc(display)
	timer(0)
	
	glutMainLoop()
