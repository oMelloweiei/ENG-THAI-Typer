from OpenGL.GL.VERSION import GL_1_0
from OpenGL.raw.GLUT import STRING
try:
	from OpenGL.GLUT import *
	from OpenGL.GL import *
	from OpenGL.GLU import *
except:
	print ('''ERROR: PyOpenGL not installed properly.''')

letter_dict = {
	'ร': [195, 4, 0],
	'ฏ': [175, 4, 0],
	'ใ': [227, 4, 0],
	'D': [45, 5.5, 0],
	't': [116, 2, 0],
	'Y': [89, 5, 0]
}

ASCII = 0
SIZE = 1
CLST = 2

def init_font():
	SaraAi()
	RorRue()
	TorPaTak()
	DLetter()
	TLetter()
	YLetter()

def SaraAi():

	info = letter_dict.get('ใ')
	info[CLST] = glGenLists(info[ASCII])
	glNewList(info[CLST], GL_COMPILE)
	glPushMatrix()
	glTranslatef(2, 2, 0)

	glBegin(GL_POLYGON) # L
	glVertex2f(0.0, 2.0)
	glVertex2f(-0.6, 2.0)
	glVertex2f(-0.6,-1.4)
	glVertex2f(0.0,-2.0)
	glEnd()

	glBegin(GL_POLYGON) # Head
	glVertex2f(-0.0,-1.4)
	glVertex2f(0.6,-1.4)
	glVertex2f(0.6,-2.0)
	glVertex2f(-0.0,-2.0)
	glEnd()	

	glBegin(GL_POLYGON) # Top1
	glVertex2f(0.0, 1.8)
	glVertex2f(-0.6, 2.0)
	glVertex2f(1.0,3.0)
	glVertex2f(1.6,3.0)
	glVertex2f(1.6,2.8)
	glEnd()	

	glBegin(GL_POLYGON) # Top2
	glVertex2f(1.0,3.0)
	glVertex2f(1.6,3.0)
	glVertex2f(1.6,4.0)
	glVertex2f(1.0,4.0)
	glEnd()

	glBegin(GL_POLYGON) # Top3
	glVertex2f(1.6,4.0)
	glVertex2f(1.0,4.6)
	glVertex2f(-1.4,4.6)
	glVertex2f(-2,4.0)
	glEnd()

	glBegin(GL_POLYGON) # Top4
	glVertex2f(-2,4.0)
	glVertex2f(-2,3.0)
	glVertex2f(-1.4,3.0)
	glVertex2f(-1.4,4.0)
	glEnd()

	glPopMatrix()
	glEndList()

def TorPaTak():

	info = letter_dict.get('ฏ')
	info[CLST] = glGenLists(info[ASCII])
	glNewList(info[CLST], GL_COMPILE)
	glPushMatrix()
	glTranslatef(2, 2, 0)

	glBegin(GL_POLYGON)
	glVertex2f(-2.5, -2)
	glVertex2f(-1.6, -2) #
	glVertex2f(-1.4, -1.8) #
	glVertex2f(-1.4, -1.4)
	glVertex2f(-2.5, -1.4)
	glEnd()

	glBegin(GL_POLYGON)
	glVertex2f(-2, -1.4)
	glVertex2f(-1.4, -1.4)
	glVertex2f(-1.4, 0.4)
	glVertex2f(-2, 0.4)
	glEnd()

	glBegin(GL_POLYGON)
	glVertex2f(-2, 0.4)
	glVertex2f(-1.4, 0)
	glVertex2f(-1, 0.4)
	glVertex2f(-1.4, 1)
	glVertex2f(-2, 0.4)
	glEnd()

	glBegin(GL_POLYGON)
	glVertex2f(-2, 0.6)
	glVertex2f(-1.5, 0.6)
	glVertex2f(-1, 0.4)
	glVertex2f(-1, 1)
	glVertex2f(-2, 1)
	glEnd()

	glBegin(GL_POLYGON)
	glVertex2f(-2, 1)
	glVertex2f(-1.4, 1)
	glVertex2f(-1.4, 2)
	glVertex2f(-1.6, 2)
	glVertex2f(-2, 1.6)
	glEnd()

	glBegin(GL_POLYGON)
	glVertex2f(-1.4, 2)
	glVertex2f(-1.4, 1.4)
	glVertex2f(2, 1.4)
	glVertex2f(2, 1.6)
	glVertex2f(1.6, 2)
	glEnd()

	glBegin(GL_POLYGON)
	glVertex2f(1.4, 1.4)
	glVertex2f(2, 1.4)
	glVertex2f(2, -4)
	glVertex2f(1.4, -4)
	glEnd()

	glBegin(GL_POLYGON)
	glVertex2f(1.4, -4)
	glVertex2f(1.4, -3.4)
	glVertex2f(0.5, -2.4)
	glVertex2f(0.2, -2.4)
	glVertex2f(0.2, -3)
	glVertex2f(1.1, -4)
	glEnd()

	glBegin(GL_POLYGON)
	glVertex2f(-0.8, -4)
	glVertex2f(-0.8, -3.4)
	glVertex2f(-1.7, -2.4)
	glVertex2f(-2, -2.4)
	glVertex2f(-2, -3)
	glVertex2f(-1.1, -4)
	glEnd()

	glBegin(GL_POLYGON)
	glVertex2f(-0.8, -4)
	glVertex2f(-0.2, -4)
	glVertex2f(-0.2, -2.4)
	glVertex2f(-0.8, -2.4)
	glEnd()

	glBegin(GL_POLYGON)
	glVertex2f(-0.2, -2.4)
	glVertex2f(-0.2, -3)
	glVertex2f(0.2, -3)
	glVertex2f(0.2, -2.4)
	glEnd()

	glBegin(GL_POLYGON)
	glVertex2f(-2, -3)
	glVertex2f(-2, -2.4)
	glVertex2f(-2.5, -2.4)
	glVertex2f(-2.5, -3)
	glEnd()

	glPopMatrix()
	glEndList()

def DLetter():

	info = letter_dict.get('D')
	info[CLST] = glGenLists(info[ASCII])
	glNewList(info[CLST], GL_COMPILE)
	glPushMatrix()
	glTranslatef(2.5, 3, 0)
		
	glBegin(GL_POLYGON)
	glVertex2f(-2.4,3.0)
	glVertex2f(-1.8,3.0)
	glVertex2f(-1.8,-3.0)
	glVertex2f(-2.4,-3.0)
	glEnd()
		
	glBegin(GL_POLYGON)
	glVertex2f(3.0,2.0)
	glVertex2f(2.4,2.6)
	glVertex2f(2.4,-2.6)
	glVertex2f(3.0,-2.0)
	glEnd()
		
	glBegin(GL_POLYGON)
	glVertex2f(2.0, 3.0)
	glVertex2f(2.6, 2.4)
	glVertex2f(-2.4, 2.4)
	glVertex2f(-2.4, 3.0)
	glEnd()
		
	glBegin(GL_POLYGON)
	glVertex2f(2.0, -3.0)
	glVertex2f(2.6, -2.4)
	glVertex2f(-2.4, -2.4)
	glVertex2f(-2.4, -3.0)
	glEnd()
		
	glBegin(GL_POLYGON)
	glVertex2f(3.0,1.8)
	glVertex2f(2.4,1.8)
	glVertex2f(1.2,3.0)
	glVertex2f(1.8,3.0)
	glEnd()
		
	glBegin(GL_POLYGON)
	glVertex2f(3.0,-1.8)
	glVertex2f(2.4,-1.8)
	glVertex2f(1.2,-3.0)
	glVertex2f(1.8,-3.0)
	glEnd()

	glPopMatrix()
	glEndList()
		
def RorRue():

	info = letter_dict.get('ร')
	info[CLST] = glGenLists(info[ASCII])
	glNewList(info[CLST], GL_COMPILE)
	glPushMatrix()
	glTranslatef(2, 2, 0)

	glBegin(GL_POLYGON)
	glVertex2f(-2.0, 1.4)
	glVertex2f(-1.4, 2.0)
	glVertex2f(-1.4, -0.1)
	glVertex2f(-2.0, 0.5)
	glEnd()
		
	glBegin(GL_POLYGON)
	glVertex2f(2.0, -1.4)
	glVertex2f(1.4, -2.0)
	glVertex2f(1.4, 0.5)
	glVertex2f(2.0, -0.1)
	glEnd()
		
	glBegin(GL_POLYGON)
	glVertex2f(2.0, 1.4)
	glVertex2f(1.4, 2.0)
	glVertex2f(1.4, 1.1)
	glVertex2f(2.0, 1.1)
	glEnd()
		
	glBegin(GL_POLYGON)
	glVertex2f(-2.0, -1.4)
	glVertex2f(-1.4, -2.0)
	glVertex2f(-1.4, -1.0)
	glVertex2f(-2.0, -1.0)
	glEnd()
		
	glBegin(GL_POLYGON)
	glVertex2f(-1.4, -0.1)
	glVertex2f(-2.0, 0.5)
	glVertex2f(1.4, 0.5)	
	glVertex2f(2.0, -0.1)
	glEnd()
		
	glBegin(GL_POLYGON)
	glVertex2f(-1.4, 2.0)
	glVertex2f(-2.0, 1.4)
	glVertex2f(2.0, 1.4)
	glVertex2f(1.4, 2.0)
	glEnd()
		
	glBegin(GL_POLYGON)
	glVertex2f(-1.4, -2.0)
	glVertex2f(-2.0, -1.4)
	glVertex2f(2.0, -1.4)
	glVertex2f(1.4, -2.0)
	glEnd()
		
	glBegin(GL_POLYGON)
	glVertex2f(1.6,1.6)
	glVertex2f(1.0,1.6)
	glVertex2f(1.4,1.2)
	glVertex2f(2.0,1.2)
	glEnd()
		
	glBegin(GL_POLYGON)
	glVertex2f(1.6, 0.2)
	glVertex2f(1.0, 0.2)
	glVertex2f(1.4, -0.2)
	glVertex2f(2.0, -0.2)
	glEnd()
		
	glBegin(GL_POLYGON)
	glVertex2f(-1.6,-1.7)
	glVertex2f(-1.0,-1.7)
	glVertex2f(-1.4,-1.3)
	glVertex2f(-2.0,-1.3)
	glEnd()
		
	glBegin(GL_POLYGON)
	glVertex2f(-1.6, 0.3)
	glVertex2f(-1.0, 0.3)
	glVertex2f(-1.4, 0.7)
	glVertex2f(-2.0, 0.7)
	glEnd()
		
	glBegin(GL_POLYGON)
	glVertex2f(1.6,-1.6)
	glVertex2f(1.0,-1.6)
	glVertex2f(1.4,-1.2)
	glVertex2f(2.0,-1.2)
	glEnd()
		
	glBegin(GL_POLYGON)
	glVertex2f(-1.6,1.6)
	glVertex2f(-1.0,1.6)
	glVertex2f(-1.4,1.2)
	glVertex2f(-2.0,1.2)
	glEnd()

	glPopMatrix()
	glEndList()

def TLetter():

	info = letter_dict.get('t')
	info[CLST] = glGenLists(info[ASCII])
	glNewList(info[CLST], GL_COMPILE)
	glPushMatrix()
	glTranslatef(1, 3, 0)

	glBegin(GL_POLYGON)
	glVertex2f(-0.3,2.0)
	glVertex2f(0.3,2.0)
	glVertex2f(0.3,-3.0)
	glVertex2f(-0.3,-3.0)
	glEnd()

	glBegin(GL_POLYGON)
	glVertex2f(1, 1)
	glVertex2f(1, 0.4)
	glVertex2f(-1, 0.4)
	glVertex2f(-1, 1)
	glEnd()

	glPopMatrix()
	glEndList()

def YLetter():

	info = letter_dict.get('Y')
	info[CLST] = glGenLists(info[ASCII])
	glNewList(info[CLST], GL_COMPILE)
	glPushMatrix()
	glTranslatef(2.4, 3, 0)

	glBegin(GL_POLYGON)
	glVertex2f(-0.3,0.0)
	glVertex2f(0.3,0.0)
	glVertex2f(0.3,-3.0)
	glVertex2f(-0.3,-3.0)
	glEnd()

	glBegin(GL_POLYGON)
	glVertex2f(1.8, 3.0)
	glVertex2f(2.4, 3.0)
	glVertex2f(0.3, 0.0)
	glVertex2f(-0.3, 0.0)
	glEnd()

	glBegin(GL_POLYGON)
	glVertex2f(-2.4, 3.0)
	glVertex2f(-1.8, 3.0)
	glVertex2f(0.3, 0.0)
	glVertex2f(-0.3, 0.0)
	glEnd()

	glPopMatrix()
	glEndList()
