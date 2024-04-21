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
	'ฏ': [175, 4.6, 0],
	'ใ': [227, 2, 0],
	'D': [45, 4, 0],
	't': [116, 3, 0],
	'Y': [89, 4, 0]
}

ASCII = 0
SIZE = 1
CLST = 2

def init_font():
	SaraAi()
	RorRue()
	TorPaTak()
	DLetter()
	tLetter()
	YLetter()

def SaraAi():

	info = letter_dict.get('ใ')
	info[CLST] = glGenLists(info[ASCII])
	glNewList(info[CLST], GL_COMPILE)
	glPushMatrix()
	glBegin(GL_POLYGON)
	glVertex2f(1.6,0.0)
	glVertex2f(1.6,0.6)
	glVertex2f(2.2,0.6)
	glVertex2f(2.2,0.0)
	glEnd()
	
	glBegin(GL_POLYGON)
	glVertex2f(1.6,0.0)
	glVertex2f(1.0,0.0)
	glVertex2f(1.0,6.0)
	glVertex2f(1.6,6.0)
	glEnd()	
	glBegin(GL_POLYGON)
	glVertex2f(1.6,6.0)
	glVertex2f(1.0,6.0)
	glVertex2f(2.4,7.8)
	glVertex2f(3.0,7.8)
	glEnd()	
	glBegin(GL_POLYGON)
	glVertex2f(3.0,7.8)
	glVertex2f(2.4,7.8)
	glVertex2f(2.4,9.0)
	glVertex2f(3.0,8.4)
	glEnd()	
	glBegin(GL_POLYGON)
	glVertex2f(2.4,9.0)
	glVertex2f(3.0,8.4)
	glVertex2f(0.0,8.4)
	glVertex2f(0.6,9.0)
	glEnd()	
	glBegin(GL_POLYGON)
	glVertex2f(0.0,8.4)
	glVertex2f(0.6,9.0)
	glVertex2f(0.6,7.0)
	glVertex2f(0.0,7.6)
	glEnd()	
	glBegin(GL_POLYGON)
	glVertex2f(0.6,7.0)
	glVertex2f(0.0,7.6)    
	glVertex2f(1.0,7.6)    
	glVertex2f(1.0,7.0)    
	glEnd()	
	glBegin(GL_POLYGON)
	glVertex2f(2.4,8.8)
	glVertex2f(3.0,8.2)
	glVertex2f(2.4,8.2)
	glVertex2f(1.8,8.8)
	glEnd()	
	glBegin(GL_POLYGON)
	glVertex2f(0.6,8.8)
	glVertex2f(0.0,8.2)
	glVertex2f(0.6,8.2)
	glVertex2f(1.2,8.8)
	glEnd()	
	glBegin(GL_POLYGON)
	glVertex2f(0.4,7.4)
	glVertex2f(0.0,7.8)
	glVertex2f(0.6,7.8)
	glVertex2f(1.0,7.4)
	glEnd()	
	glPopMatrix()
	glEndList()

def TorPaTak():

	info = letter_dict.get('ฏ')
	info[CLST] = glGenLists(info[ASCII])
	glNewList(info[CLST], GL_COMPILE)
	glPushMatrix()	
	glTranslatef(0.6,0,0)
	glBegin(GL_POLYGON)
	glVertex2f(-0.6, 0)
	glVertex2f(0, 0)
	glVertex2f(0, 0.6)
	glVertex2f(-0.6, 0.6)
	glEnd()
    
	glBegin(GL_POLYGON)
	glVertex2f(0.0, 0)
	glVertex2f(0.6, 0)
	glVertex2f(0.6,2.4)
	glVertex2f(0.0,2.4)
	glEnd()

	glBegin(GL_POLYGON)
	glVertex2f(0.0, 2.4)
	glVertex2f(0.6, 2.4)
	glVertex2f(1.4,3.2)
	glVertex2f(0.8,3.2)
	glEnd()

	glBegin(GL_POLYGON)
	glVertex2f(0.0,3.6)
	glVertex2f(0.0, 3.2)
	glVertex2f(1.4,3.2)
	glVertex2f(1.4,3.6)
	glEnd()

	glBegin(GL_POLYGON)
	glVertex2f(0.6,3.4)
	glVertex2f(0.0, 3.4)
	glVertex2f(0.0,4.4)
	glVertex2f(0.6,5)
	glEnd()

	glBegin(GL_POLYGON)
	glVertex2f(4,4.4)
	glVertex2f(3.4, 5)
	glVertex2f(0.6,5)
	glVertex2f(0.0,4.4)
	glEnd()

	glBegin(GL_POLYGON)
	glVertex2f(3.4,5)
	glVertex2f(4, 4.4)
	glVertex2f(4,0)
	glVertex2f(3.4,0)
	glEnd()

	glBegin(GL_POLYGON)
	glVertex2f(0.6,4.8)
	glVertex2f(1.2,4.8)
	glVertex2f(0.6,4.2)
	glVertex2f(0.0,4.2)
	glEnd()	
	glBegin(GL_POLYGON)
	glVertex2f(3.4,4.2)
	glVertex2f(4.0,4.2)
	glVertex2f(3.4,4.8)
	glVertex2f(2.8,4.8)
	glEnd()	
	glBegin(GL_POLYGON)
	glVertex2f(4.0,-0.0)
	glVertex2f(4.0,-2.4)
	glVertex2f(3.4,-2.4)
	glVertex2f(3.4,-0.0)
	glEnd()	
	glBegin(GL_POLYGON)
	glVertex2f(4.0,-2.4)
	glVertex2f(3.4,-2.4)
	glVertex2f(2.2,-1.0)
	glVertex2f(2.8,-1.0)
	glEnd()	
	glBegin(GL_POLYGON)
	glVertex2f(2.8,-1.0)
	glVertex2f(2.8,-1.6)
	glVertex2f(2.0,-1.6)
	glVertex2f(2.0,-1.0)
	glEnd()	
	glBegin(GL_POLYGON)
	glVertex2f(2.0,-1.0)
	glVertex2f(2.0,-2.4)
	glVertex2f(2.6,-2.4)
	glVertex2f(2.6,-1.0)
	glEnd()	
	glBegin(GL_POLYGON)
	glVertex2f(2.6,-2.4)
	glVertex2f(2.0,-2.4)
	glVertex2f(0.6,-1.0)
	glVertex2f(1.2,-1.0)
	glEnd()	
	glBegin(GL_POLYGON)
	glVertex2f(1.2,-1.0)
	glVertex2f(1.2,-1.6)
	glVertex2f(0.0,-1.6)
	glVertex2f(0.0,-1.0)
	glEnd()	
	glPopMatrix()
	glEndList()

def DLetter():

	info = letter_dict.get('D')
	info[CLST] = glGenLists(info[ASCII])
	glNewList(info[CLST], GL_COMPILE)

	glPushMatrix()
	glTranslatef(0, 0, 0)	

	glBegin(GL_POLYGON)
	glVertex2f(0, 8.0)
	glVertex2f(0.6, 8.0)
	glVertex2f(0.6,0.0)
	glVertex2f(0,0.0)
	glEnd()	

	glBegin(GL_POLYGON)
	glVertex2f(2.8,8.0)
	glVertex2f(3.4,7.4)
	glVertex2f(0.6,7.4)
	glVertex2f(0.6,8.0)
	glEnd()

	glBegin(GL_POLYGON)
	glVertex2f(3.4,0.6)
	glVertex2f(2.8,0.0)
	glVertex2f(0.6,0.0)
	glVertex2f(0.6,0.6)
	glEnd()

	glBegin(GL_POLYGON)
	glVertex2f(2.4,0.0)
	glVertex2f(3.0,0.0)
	glVertex2f(4.0,1.0)
	glVertex2f(3.4,1.0)
	glEnd()

	glBegin(GL_POLYGON)
	glVertex2f(2.4,8.0)
	glVertex2f(3.0,8.0)
	glVertex2f(4.0,7.0)
	glVertex2f(3.4,7.0)
	glEnd()


	glBegin(GL_POLYGON)
	glVertex2f(4.0,7.0)
	glVertex2f(3.4,7.0)
	glVertex2f(3.4,1.0)
	glVertex2f(4.0,1.0)
	glEnd()	

	glPopMatrix()
	glEndList()
		
def RorRue():

	info = letter_dict.get('ร')
	info[CLST] = glGenLists(info[ASCII])
	glNewList(info[CLST], GL_COMPILE)
	glPushMatrix()

	glBegin(GL_POLYGON)
	glVertex2f(3.4, 3.0)
	glVertex2f(2.8, 3.6)
	glVertex2f(2.8, 0.0)
	glVertex2f(3.4, 0.6)
	glEnd()
	
	glBegin(GL_POLYGON)
	glVertex2f(0.0, 3.6)
	glVertex2f(0.6, 3.0)
	glVertex2f(0.6, 5.0)
	glVertex2f(0.0, 4.4)
	glEnd()	
	glBegin(GL_POLYGON)
	glVertex2f(0.6,5.0)
	glVertex2f(0.0,4.4)
	glVertex2f(4.0,4.4)
	glVertex2f(4.0,5.0)
	glEnd()
	
	glBegin(GL_POLYGON)
	glVertex2f(0.6,3.0)
	glVertex2f(0.0,3.6)
	glVertex2f(2.8,3.6)
	glVertex2f(3.4,3.0)
	glEnd()
	
	glBegin(GL_POLYGON)
	glVertex2f(1.6,0.0)
	glVertex2f(1.6,0.6)
	glVertex2f(3.4,0.6)
	glVertex2f(2.8,0.0)
	glEnd()
	
	# glColor3f(1,0,0)
	glBegin(GL_POLYGON)
	glVertex2f(3.4,2.8)
	glVertex2f(2.8,3.4)
	glVertex2f(2.2,3.4)
	glVertex2f(2.8,2.8)
	glEnd()
	
	glBegin(GL_POLYGON)
	glVertex2f(2.8,0.8)
	glVertex2f(3.4,0.8)
	glVertex2f(2.8,0.2)
	glVertex2f(2.2,0.2)
	glEnd()
	
	glBegin(GL_POLYGON)
	glVertex2f(0.0,3.8)
	glVertex2f(0.6,3.8)
	glVertex2f(1.2,3.2)
	glVertex2f(0.6,3.2)
	glEnd()
	
	glBegin(GL_POLYGON)
	glVertex2f(0.0,4.2)
	glVertex2f(0.6,4.2)
	glVertex2f(1.2,4.8)
	glVertex2f(0.6,4.8)
	glEnd()	
	glPopMatrix()
	glEndList()

def tLetter():
	info = letter_dict.get('t')
	info[CLST] = glGenLists(info[ASCII])
	glNewList(info[CLST], GL_COMPILE)
	glPushMatrix()
	glTranslatef(-0.5,0,0)
	glBegin(GL_POLYGON)
	glVertex2f(1.7,8.0)
	glVertex2f(2.3,8.0)
	glVertex2f(2.3,0.0)
	glVertex2f(1.7,0.0)
	glEnd()	

	glBegin(GL_POLYGON)
	glVertex2f(0.5,5.0)
	glVertex2f(3.5,5.0)
	glVertex2f(3.5,4.4)
	glVertex2f(0.5,4.4)
	glEnd()	
	glPopMatrix()
	glEndList()

def YLetter():

	info = letter_dict.get('Y')
	info[CLST] = glGenLists(info[ASCII])
	glNewList(info[CLST], GL_COMPILE)
	glPushMatrix()
	glTranslatef(-0.2,0,0)
	glBegin(GL_POLYGON)
	glVertex2f(0.0,8.0)
	glVertex2f(0.6,8.0)
	glVertex2f(2.3,4.4)
	glVertex2f(1.7,4.4)
	glEnd()	

	glBegin(GL_POLYGON)
	glVertex2f(3.4,8.0)
	glVertex2f(4.0,8.0)
	glVertex2f(2.3,4.4)
	glVertex2f(1.7,4.4)
	glEnd()	

	glBegin(GL_POLYGON)
	glVertex2f(1.7,4.4)
	glVertex2f(2.3,4.4)
	glVertex2f(2.3,0.0)
	glVertex2f(1.7,0.0)
	glEnd()	

	glPopMatrix()
	glEndList()
