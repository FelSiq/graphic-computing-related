from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

WINDOW_SIZE_W=1080
WINDOW_SIZE_H=640
OBJECT_ANGLE=0
ROTATE_INCREMENT=1
ROTATE_TIMER=30

# top, down, left, right, front, back
def drawCube(edge, draw=(1, 1, 1, 1, 1, 1)):
	he = edge/2
	glBegin(GL_QUADS)

	if draw[1]:
		glColor3f(0, 1, 1)
		glVertex3f( he, -he, -he)
		glVertex3f( he,  he, -he)
		glVertex3f(-he,  he, -he)
		glVertex3f(-he, -he, -he)

	if draw[0]:	
		glColor3f(1, 0, 1)
		glVertex3f( he,  he,  he)
		glVertex3f( he, -he,  he)
		glVertex3f(-he, -he,  he)
		glVertex3f(-he,  he,  he)

	if draw[2]:	
		glColor3f(1, 1, 0)
		glVertex3f(-he, -he, -he)
		glVertex3f(-he, -he,  he)
		glVertex3f(-he,  he,  he)
		glVertex3f(-he,  he, -he)

	if draw[3]:	
		glColor3f(1, 0, 0)
		glVertex3f( he, -he, -he)
		glVertex3f( he, -he,  he)
		glVertex3f( he,  he,  he)
		glVertex3f( he,  he, -he)

	if draw[4]:	
		glColor3f(0, 0, 1)
		glVertex3f(-he, -he, -he)
		glVertex3f(-he, -he,  he)
		glVertex3f( he, -he,  he)
		glVertex3f( he, -he, -he)

	if draw[5]:	
		glColor3f(1, 1, 1)
		glVertex3f(-he,  he, -he)
		glVertex3f(-he,  he,  he)
		glVertex3f( he,  he,  he)
		glVertex3f( he,  he, -he)

	glEnd()

def setup():
	glutInit()
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
	glutInitWindowSize(WINDOW_SIZE_W, WINDOW_SIZE_H)
	glutCreateWindow('Menger Sponge using OpenGL')
	glEnable(GL_DEPTH_TEST)
	glClearColor(0, 0, 0, 0)

def rotateObject(value):
	global OBJECT_ANGLE
	OBJECT_ANGLE += ROTATE_INCREMENT
	OBJECT_ANGLE %= 360
	display()
	glutTimerFunc(ROTATE_TIMER, rotateObject, value)

def display():
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glLoadIdentity()
	glOrtho(2, -2, 2, -2, 2, -100)
	glRotatef(OBJECT_ANGLE, 1, 1, 1)
	drawCube(1, (1,1,1,1,1,1))
	glutSwapBuffers()

if __name__ == '__main__':
	setup()
	rotateObject(0)
	glutMainLoop()

