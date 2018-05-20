import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

WINDOW_SIZE_W=1080
WINDOW_SIZE_H=640
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

def renderText(deepness):
	text = 'Deepness:' + str(deepness)
	glColor3f(0.75, 0.75, 0.1)
	glLoadIdentity()
	glRasterPos2f(-0.95, -0.95)
	for ch in text:
		glutBitmapCharacter(GLUT_BITMAP_9_BY_15, ord(ch))

def drawObject(edgeSize, recCallsNum, ti=0, tj=0, tk=0):
	"""
	The "object" is a collection of 20 cubes.
	"""
	tMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
	shiftCoords = [-edgeSize, 0, edgeSize]
	for i in shiftCoords:
		for j in shiftCoords:
			for k in shiftCoords:
				if abs(i) + abs(j) + abs(k) >= 2.0*edgeSize:
					glColor3f(
						abs(i + ti),
						abs(j + tj), 
						abs(k + tk))
					glLoadMatrixf(tMatrix)
					if recCallsNum:
						drawObject(edgeSize/3, 
							recCallsNum-1, 
							ti+i, tj+j, tk+k)
					else:
						glRotatef(OBJECT_ANGLE, 1, 1, 1)
						glTranslatef(ti+i, tj+j, tk+k)
						glutSolidCube(edgeSize)
	

def rotateObject(value):
	global OBJECT_ANGLE
	OBJECT_ANGLE += ROTATE_INCREMENT
	OBJECT_ANGLE %= 360
	display(value)
	glutTimerFunc(ROTATE_TIMER, rotateObject, value)

def display(recCallsNum=0):
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glLoadIdentity()
	glOrtho(2, -2, 2, -2, 2, -100)
	drawObject(0.75, recCallsNum)
	renderText(recCallsNum)
	glFlush()

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print('usage:', sys.argv[0], '<depth between 0 and 10>')
		exit(1)
	try:
		deepness = int(sys.argv[1])
		if not (0 <= deepness <= 10):
			raise Exception()
	except:
		print('Depth parameter must be a integer between 0 and 10.')
		exit(2)

	print('Started rendering process. This may take a while...')
	setup()

	if deepness > 2:
		print('Warning: disabling rotation to improve performance.')
		OBJECT_ANGLE=30
		display(deepness)
	else:
		rotateObject(deepness)

	glutMainLoop()

