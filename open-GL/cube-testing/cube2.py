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
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
	glutInitWindowSize(640, 480)
	glutInitWindowPosition(100, -500)
	glutCreateWindow('Cube with lights')
	glEnable(GL_DEPTH_TEST)
	glClearColor(0, 0, 0, 0)
	gluLookAt(0, 0, 2, 0, 0, 0, 0, 1, 0)

def initLighting():
	glEnable(GL_LIGHTING)
	glEnable(GL_LIGHT0)
	glEnable(GL_COLOR_MATERIAL)

def display():
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	glOrtho(-2, 2, -2, 2, -2, 100)
	
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	glLightfv(GL_LIGHT0, GL_POSITION, [0.0, 10.0, 10.0, 0.0])
	glMaterialfv(GL_FRONT, GL_AMBIENT, [0.7, 0.7, 0.7, 1.0])
	glMaterialfv(GL_FRONT, GL_SPECULAR, [0.2, 0.2, 0.2, 0.2])
	glMaterialfv(GL_FRONT, GL_DIFFUSE, [0.1, 0.5, 0.8, 1.0])

	glColor3f(1, 1, 1)
	glViewport(0, 0, 640, 480)
	gluLookAt(0, 0, 1, 0, 0, 0, 0, 1, 0)
	glRotatef(angle, 1, 1, 1)
	glutSolidCube(1.2)

	glFlush()

if __name__ == '__main__':
	glutInit()
	init()
	initLighting()

	glutDisplayFunc(display)
	timer(0)
	
	glutMainLoop()
