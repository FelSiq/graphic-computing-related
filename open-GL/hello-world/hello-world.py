import OpenGL.GL as gl
import OpenGL.GLU as glu
import OpenGL.GLUT as glut
import OpenGL as ogl

def trianglesAreMyFavoriteShape():
	gl.glViewport(0,0,200,200)
	gl.glBegin(gl.GL_TRIANGLES)
	gl.glColor3f(0,1,0.4)	
	gl.glVertex3f(0,0,0)
	gl.glVertex3f(1,0,0)
	gl.glVertex3f(0,1,0)
	gl.glEnd()

	#gl.glViewport(25,25, 200,200)
	gl.glBegin(gl.GL_TRIANGLES)
	gl.glColor3f(0,0,0.8)	
	gl.glVertex3f(1,1,0)
	gl.glColor3f(0,1,0.4)	
	gl.glVertex3f(1,0.2,0)
	gl.glColor3f(0,1,0.4)	
	gl.glVertex3f(0.2,1,0)
	gl.glEnd()

	gl.glFlush()

if __name__ == '__main__':
	glut.glutInit()
	glut.glutInitWindowSize(640, 480)
	glut.glutCreateWindow('Hello world!')

	gl.glClearColor(0,0,1,0)

	glut.glutDisplayFunc(trianglesAreMyFavoriteShape)

	glut.glutMainLoop()
	
