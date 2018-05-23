from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

WINDOW_SIZE_W=1080
WINDOW_SIZE_H=640
OBJECT_X_ANGLE=0
OBJECT_Y_ANGLE=0
OBJECT_Z_ANGLE=0
ROTATE_INCREMENT=3
UPDATE_TIMER=30
CURRENT_DEPTH=1
MAX_DEPTH=5
ZOOM_VALUE=0.75
ZOOM_INCREMENT=0.025
ENABLE_TIMER=True
COLOR_SCHEMA=True
# 	 t, d, l, r, f, b
DRAW_FACES_SEQ = [
	(0, 1, 1, 0, 1, 0), # -x -y -z
	(0, 0, 1, 1, 1, 1), # -x -y oz
	(1, 0, 1, 0, 1, 0), # -x -y +z
	(1, 1, 1, 1, 0, 0), # -x oy -z
	(1, 1, 1, 1, 0, 0), # -x oy +z
	(0, 1, 1, 0, 0, 1), # -x +y -z
	(0, 0, 1, 1, 1, 1), # -x +y oz
	(1, 0, 1, 0, 0, 1), # -x +y +z
	(1, 1, 0, 0, 1, 1), # ox -y -z
	(1, 1, 0, 0, 1, 1), # ox -y +z
	(1, 1, 0, 0, 1, 1), # ox +y -z
	(1, 1, 0, 0, 1, 1), # ox +y +z
	(0, 1, 0, 1, 1, 0), # +x -y -z
	(0, 0, 1, 1, 1, 1), # +x -y oz
	(1, 0, 0, 1, 1, 0), # +x -y +z
	(1, 1, 1, 1, 0, 0), # +x oy -z
	(1, 1, 1, 1, 0, 0), # +x oy +z
	(0, 1, 0, 1, 0, 1), # +x +y -z
	(0, 0, 1, 1, 1, 1), # +x +y oz
	(1, 0, 0, 1, 0, 1), # +x +y +z
]

def setup():
	glutInit()
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
	glutInitWindowSize(WINDOW_SIZE_W, WINDOW_SIZE_H)
	glutCreateWindow('Menger Sponge using OpenGL')
	glEnable(GL_DEPTH_TEST)
	glClearColor(0, 0, 0, 0)

def renderText(deepness):
	text = 'Deepness: (' +\
		str(1+deepness) +\
		'/' + str(1+MAX_DEPTH) + ')' +\
		'\nl: +x_angle' +\
		'\nk: +y_angle' +\
		'\nu: +z_angle' +\
		'\nj: -x_angle' +\
		'\ni: -y_angle' +\
		'\no: -z_angle' +\
		'\n+: +deepness' +\
		'\n-: -deepness' +\
		'\na: +zoom' +\
		'\ns: -zoom' +\
		'\nd: toggle color' +\
		'\nESC: exit'
	glColor3f(0.75, 0.75, 0.1)
	glLoadIdentity()
	
	yPos = -0.30
	yInc = 32.0/WINDOW_SIZE_H
	glRasterPos2f(-0.98, yPos)
	for ch in text:
		if ch != '\n':
			glutBitmapCharacter(GLUT_BITMAP_9_BY_15, ord(ch))
		else:
			yPos -= yInc
			glRasterPos2f(-0.98, yPos)


# top, down, left, right, front, back
def drawCube(edge, draw=(1, 1, 1, 1, 1, 1)):
	he = edge/2
	glBegin(GL_QUADS)

	if draw[1]:
		glVertex3f( he, -he, -he)
		glVertex3f( he,  he, -he)
		glVertex3f(-he,  he, -he)
		glVertex3f(-he, -he, -he)

	if draw[0]:	
		glVertex3f( he,  he,  he)
		glVertex3f( he, -he,  he)
		glVertex3f(-he, -he,  he)
		glVertex3f(-he,  he,  he)

	if draw[2]:	
		glVertex3f(-he, -he, -he)
		glVertex3f(-he, -he,  he)
		glVertex3f(-he,  he,  he)
		glVertex3f(-he,  he, -he)

	if draw[3]:	
		glVertex3f( he, -he, -he)
		glVertex3f( he, -he,  he)
		glVertex3f( he,  he,  he)
		glVertex3f( he,  he, -he)

	if draw[4]:	
		glVertex3f(-he, -he, -he)
		glVertex3f(-he, -he,  he)
		glVertex3f( he, -he,  he)
		glVertex3f( he, -he, -he)

	if draw[5]:	
		glVertex3f(-he,  he, -he)
		glVertex3f(-he,  he,  he)
		glVertex3f( he,  he,  he)
		glVertex3f( he,  he, -he)

	glEnd()

def drawObject(edgeSize, recCallsNum, ti=0, tj=0, tk=0):
	"""
	The "object" is a collection of 20 cubes.
	"""
	global DRAW_FACES_SEQ
	counter=0
	tMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
	shiftCoords = [-edgeSize, 0, edgeSize]

	for i in shiftCoords:
		for j in shiftCoords:
			for k in shiftCoords:
				if abs(i) + abs(j) + abs(k) >= 2.0*edgeSize:
					if COLOR_SCHEMA:
						glColor3f(
							abs(i + ti),
							abs(j + tj), 
							abs(k + tk))
					else:
						glColor3f(
							1.0-abs(i + ti),
							1.0-abs(j + tj), 
							1.0-abs(k + tk))

					glLoadMatrixf(tMatrix)
					if recCallsNum:
						drawObject(edgeSize/3, 
							recCallsNum-1, 
							ti+i, tj+j, tk+k)
					else:
						glRotatef(OBJECT_X_ANGLE, 1, 0, 0)
						glRotatef(OBJECT_Y_ANGLE, 0, 1, 0)
						glRotatef(OBJECT_Z_ANGLE, 0, 0, 1)
						glTranslatef(ti+i, tj+j, tk+k)
						drawCube(edgeSize, DRAW_FACES_SEQ[counter])
						counter += 1

def display(value):
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glLoadIdentity()
	glOrtho(2, -2, 2, -2, 2, -100)
	drawObject(ZOOM_VALUE, CURRENT_DEPTH)
	renderText(CURRENT_DEPTH)
	glutSwapBuffers()

	global ENABLE_TIMER
	ENABLE_TIMER=True

def keyPressEvent(key, x, y):
	global OBJECT_X_ANGLE
	global OBJECT_Y_ANGLE
	global OBJECT_Z_ANGLE
	global ROTATE_INCREMENT
	global CURRENT_DEPTH
	global ZOOM_VALUE
	global ZOOM_INCREMENT
	global ENABLE_TIMER
	global COLOR_SCHEMA

	if key == b'l':
		OBJECT_X_ANGLE += ROTATE_INCREMENT
	elif key == b'j':
		OBJECT_X_ANGLE -= ROTATE_INCREMENT
	elif key == b'k':
		OBJECT_Y_ANGLE += ROTATE_INCREMENT
	elif key == b'i':
		OBJECT_Y_ANGLE -= ROTATE_INCREMENT
	elif key == b'u':
		OBJECT_Z_ANGLE += ROTATE_INCREMENT
	elif key == b'o':
		OBJECT_Z_ANGLE -= ROTATE_INCREMENT
	elif key == b'+':
		CURRENT_DEPTH = min(CURRENT_DEPTH+1, MAX_DEPTH)
	elif key == b'-':
		CURRENT_DEPTH = max(CURRENT_DEPTH-1, 0)
	elif key == b'\x1b':
		print('Program terminated successfully.')
		exit(0)
	elif key == b'a':
		ZOOM_VALUE = min(1.0, 
			ZOOM_VALUE + ZOOM_INCREMENT)
	elif key == b's':
		ZOOM_VALUE = max(2.0*ZOOM_INCREMENT, 
			ZOOM_VALUE - ZOOM_INCREMENT)
	elif key == b'd':
		COLOR_SCHEMA = not COLOR_SCHEMA

	if ENABLE_TIMER:
		ENABLE_TIMER=False
		glutTimerFunc(UPDATE_TIMER, display, 0)

if __name__ == '__main__':
	setup()

	OBJECT_X_ANGLE=30
	OBJECT_Y_ANGLE=30
	OBJECT_Z_ANGLE=30
	glutKeyboardFunc(keyPressEvent)
	display(0)

	glutMainLoop()

