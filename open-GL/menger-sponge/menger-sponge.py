from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

WINDOW_SIZE_W=1080
WINDOW_SIZE_H=640
VIEW_SIZE_W=int(WINDOW_SIZE_W/1.1)
VIEW_SIZE_H=int(WINDOW_SIZE_H/1.1)
VIEW_SHIFT_X=(WINDOW_SIZE_W - VIEW_SIZE_W)//2
VIEW_SHIFT_Y=(WINDOW_SIZE_H - VIEW_SIZE_H)//2
OBJECT_ANGLE=0
ROTATE_INCREMENT=1
ROTATE_TIMER=30

def setup():
	glutInit()
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
	glutInitWindowSize(WINDOW_SIZE_W, WINDOW_SIZE_H)
	glutCreateWindow('Menger Sponge using OpenGL')
	glEnable(GL_DEPTH_TEST)
	glClearColor(0, 0, 0, 0)

def drawObject(edgeSize, recCallsNum):
	"""
	The "object" is a collection of 20 cubes.
	"""
	tMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
	shiftCoords = [-edgeSize, 0, edgeSize]
	for i in shiftCoords:
		for j in shiftCoords:
			for k in shiftCoords:
				if abs(i) + abs(j) + abs(k) >= 2.0*edgeSize:
					glColor3f(abs(j/1.5-i), abs(k/1.5-j), abs(i/1.5-k))
					glLoadMatrixf(tMatrix)
					glOrtho(2, -2, 2, -2, 2, -100)
					glRotatef(OBJECT_ANGLE, 1, 1, 1)
					glTranslatef(i, j, k)
					glutSolidCube(edgeSize)
	

def rotateObject(value):
	global OBJECT_ANGLE
	OBJECT_ANGLE += ROTATE_INCREMENT
	display(value)
	glutTimerFunc(ROTATE_TIMER, rotateObject, value)

def display(recCallsNum=5):
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glViewport(
		VIEW_SHIFT_X, 
		VIEW_SHIFT_Y, 
		VIEW_SIZE_W, 
		VIEW_SIZE_H)
	glColor3f(1, 1, 1)
	glLoadIdentity()
	drawObject(0.5, recCallsNum)
	glFlush()

if __name__ == '__main__':
	setup()
	glutDisplayFunc(display)
	rotateObject(5)
	glutMainLoop()

