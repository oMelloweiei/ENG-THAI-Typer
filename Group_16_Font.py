import sys
from OpenGL.GL.VERSION import GL_1_0
from OpenGL.raw.GLUT import STRING
try:
  from OpenGL.GLUT import *
  from OpenGL.GL import *
  from OpenGL.GLU import *
except:
    print ('''ERROR: PyOpenGL not installed properly.''')
    
letter_dict = {
	'ฅ': [165, 4, 0],
	'ฟ': [191, 4, 0],
	'k': [107, 4, 0],
	'P': [80, 4, 0],
	'ี': [213, 3, 0],
}

#position in letter dictionary
ASCII = 0
SIZE = 1
CLST = 2

def init_font():
    saraE()
    forfun()
    korkon()
    k()
    P()

def saraE():
    info = letter_dict.get('ี')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)

    glPushMatrix()
    glTranslatef(1,6,0)
    glBegin(GL_POLYGON)
    glVertex2f(0,0.6)
    glVertex2f(3,0.6)
    glVertex2f(3,0)
    glVertex2f(0,0)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(2.4,0)
    glVertex2f(3,0)
    glVertex2f(3,1.2)
    glVertex2f(2.4,1.2)
    glEnd()
    glPopMatrix()
    glEndList()
   
   
def korkon():
    info = letter_dict.get('ฅ')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)
    glBegin(GL_POLYGON)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.6, 0.0)
    glVertex2f(0.6, 5.0)
    glVertex2f(0.0, 4.4)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(4.0, 0.0)
    glVertex2f(3.4, 0.0)
    glVertex2f(3.4, 5.0)
    glVertex2f(4.0, 4.4)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(0, 4.4)
    glVertex2f(0.6, 5.0)
    glVertex2f(1.4, 5.0)
    glVertex2f(2.0, 4.4)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(2.0 + 0.3, 4.2)
    glVertex2f(1.2 + 0.3, 5.0)
    glVertex2f(0.6 + 0.3, 5.0)
    glVertex2f(1.4 + 0.3, 4.2)
    glEnd()

    #เส้นเฉือนดิ่ง(ขวา)
    glBegin(GL_POLYGON)
    glVertex2f(2.4 + 0.1, 5.0)
    glVertex2f(3.0 + 0.1, 5.0)
    glVertex2f(2.2 + 0.1, 4.2)
    glVertex2f(1.6 + 0.1, 4.2)
    glEnd()

    # เส้นดิ่ง
    glBegin(GL_POLYGON)
    glVertex2f(2.3, 4.4)
    glVertex2f(1.7, 4.4)
    glVertex2f(1.7, 3.4)
    glVertex2f(2.3, 3.4)
    glEnd()
    
    #เส้นบน(ขวา)
    glBegin(GL_POLYGON)
    glVertex2f(2, 4.4)
    glVertex2f(2.6, 5.0)
    glVertex2f(3.4, 5.0)
    glVertex2f(4.0, 4.4)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(1.7, 2.6)
    glVertex2f(1.7, 2.0)
    glVertex2f(2.3, 2.0)
    glVertex2f(2.3, 2.6)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(2.3, 2.6)
    glVertex2f(0.6, 1.0)
    glVertex2f(0.0, 1.0)
    glVertex2f(1.7, 2.6)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(0.6, 4.8)
    glVertex2f(1.2, 4.8)
    glVertex2f(0.6, 4.2)
    glVertex2f(0.0, 4.2)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(3.4, 4.8)
    glVertex2f(2.8, 4.8)
    glVertex2f(3.4, 4.2)
    glVertex2f(4.0, 4.2)
    glEnd()
    glEndList()

def forfun():
    info = letter_dict.get('ฟ')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)
    glBegin(GL_POLYGON)
    glVertex2f(0.6, 5.0)
    glVertex2f(0.6, 0.0)
    glVertex2f(0.0, 0.6)
    glVertex2f(0.0, 5.0)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(3.4, 8.0)
    glVertex2f(3.4, 0.0)
    glVertex2f(4.0, 0.6)
    glVertex2f(4.0, 8.0)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(2.3,5.0)
    glVertex2f(1.7,5.0)
    glVertex2f(1.7,0.6)
    glVertex2f(2.3,0.6)
    glEnd()
    
    # # glColor3f(0,0,1)
    glBegin(GL_POLYGON)
    glVertex2f(2.3,0.6)
    glVertex2f(0.0,0.6)
    glVertex2f(0.6,0.0)
    glVertex2f(1.8,0.0)
    glEnd() 
       
    glBegin(GL_POLYGON)
    glVertex2f(4.0,0.6)
    glVertex2f(1.7,0.6)
    glVertex2f(2.3,0.0)
    glVertex2f(3.4,0.0)
    glEnd()    

    glBegin(GL_POLYGON)
    glVertex2f(0.0,0.8)
    glVertex2f(0.6,0.8)
    glVertex2f(1.2,0.2)
    glVertex2f(0.6,0.2)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0.0,0.8)
    glVertex2f(0.6,0.8)
    glVertex2f(1.2,0.2)
    glVertex2f(0.6,0.2)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(1.7,0.8)
    glVertex2f(2.3,0.8)
    glVertex2f(2.9,0.2)
    glVertex2f(2.3,0.2)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(1.1,0.2)
    glVertex2f(1.7,0.2)
    glVertex2f(2.3,0.8)
    glVertex2f(1.7,0.8)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(2.8,0.2)
    glVertex2f(3.4,0.2)
    glVertex2f(4.0,0.8)
    glVertex2f(3.4,0.8)
    glEnd()
    glEndList()
   


def k():
    info = letter_dict.get('k')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)
    glBegin(GL_POLYGON)
    glVertex2f(0,8)
    glVertex2f(0.6,8)
    glVertex2f(0.6,0)
    glVertex2f(0,0)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0.6,2.2)
    glVertex2f(2.8,2.2)
    glVertex2f(3.4,2.8)
    glVertex2f(0.6,2.8)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0.6,2.2)
    glVertex2f(3.4,2.2)
    glVertex2f(2.8,2.8)
    glVertex2f(0.6,2.8)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(2.8,2.8)
    glVertex2f(2.2,2.8)
    glVertex2f(3.4,1.6)
    glVertex2f(4.0,1.6)
    glEnd()
    
    
    glBegin(GL_POLYGON)
    glVertex2f(2.8,2.2)
    glVertex2f(2.2,2.2)
    glVertex2f(3.4,3.4)
    glVertex2f(4.0,3.4)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(4.0,5.0)
    glVertex2f(3.4,5.0)
    glVertex2f(3.4,3.4)
    glVertex2f(4.0,3.4)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(4.0,1.6)
    glVertex2f(3.4,1.6)
    glVertex2f(3.4,0.0)
    glVertex2f(4.0,0.0)
    glEnd()
    glEndList()
   
def P():
    info = letter_dict.get('P')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)
    glBegin(GL_POLYGON)
    glVertex2f(0.6,8)
    glVertex2f(0,8)
    glVertex2f(0,0)
    glVertex2f(0.6,0)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0,8)
    glVertex2f(3.4,8)
    glVertex2f(4,7.4)
    glVertex2f(0,7.4)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0,4.6)
    glVertex2f(4,4.6)
    glVertex2f(3.4,4)
    glVertex2f(0,4)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(3.4,8)
    glVertex2f(4,7.4)
    glVertex2f(4,4.6)
    glVertex2f(3.4,4)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(4,5.6)
    glVertex2f(4,4.6)
    glVertex2f(3.4,4)
    glVertex2f(2.4,4)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(2.4,8)
    glVertex2f(3.4,8)
    glVertex2f(4,7.4)
    glVertex2f(4,6.4)
    glEnd()
    glEndList()
   
