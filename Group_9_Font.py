#!/usr/bin/python

import sys

from OpenGL.GL.VERSION import GL_1_0
from OpenGL.raw.GLUT import STRING
try:
  from OpenGL.GLUT import *
  from OpenGL.GL import *
  from OpenGL.GLU import *
except:
  print ('''ERROR: PyOpenGL not installed properly.''')
  
move = 5

letter_dict = {
	'r': [114, 4, 0],
	'W': [87, 6, 0],
	'B': [66, 4, 0],
	'ค': [164, 4, 0],
	'ฬ': [204, 4, 0],
	'ฤ': [196, 4, 0]
}

ASCII = 0
SIZE = 1
CLST = 2

def init_font():
    r_Letter()
    W_letter()
    B_letter()
    Kor_kwai()
    Ror_jura()
    Ror_ri()
    
def Ror_ri():
    info = letter_dict.get('ฤ')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)
    
    glBegin(GL_POLYGON)
    glVertex2f(0, 0)
    glVertex2f(1.2, 0)
    glVertex2f(1.2, 0.6)
    glVertex2f(0, 0.6)
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
    glVertex2f(4,-3.0)
    glVertex2f(3.4,-3.0)
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
    glEndList()
    
    
def Ror_jura():
    info = letter_dict.get('ฬ')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)
    
    glBegin(GL_POLYGON)
    glVertex2f(0.6, 5.0)
    glVertex2f(0.6, 0.0)
    glVertex2f(0.0, 0.6)
    glVertex2f(0.0, 5.0)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(3.4, 5.0)
    glVertex2f(3.4, 0.0)
    glVertex2f(4.0, 0.6)
    glVertex2f(4.0, 5.0)
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
    glVertex2f(4.0,8.0)
    glVertex2f(3.4,8.0)
    glVertex2f(3.4,6.8)
    glVertex2f(4.0,7.4)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(4.0,5.0)
    glVertex2f(3.4,5.0)
    glVertex2f(3.4,6.2)
    glVertex2f(4.0,5.6)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(4.0,5.6)
    glVertex2f(3.4,5.6)
    glVertex2f(2.6,6.4)
    glVertex2f(3.2,6.4)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(4.0,7.4)
    glVertex2f(3.4,7.4)
    glVertex2f(2.6,6.4)
    glVertex2f(3.2,6.4)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(2.0,6.1)
    glVertex2f(2.9,6.1)
    glVertex2f(2.9,6.7)
    glVertex2f(2.0,6.7)
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
    
    
def Kor_kwai():
    info = letter_dict.get('ค')
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
    glVertex2f(0.6, 5.0)
    glVertex2f(0.0, 4.4)
    glVertex2f(4.0, 4.4)
    glVertex2f(3.4, 5.0)
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
    
def B_letter():
    info = letter_dict.get('B')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)
    
    glPushMatrix()

    glBegin(GL_POLYGON)
    glVertex2f(0, 8.0)
    glVertex2f(0.6, 8.0)
    glVertex2f(0.6,0.0)
    glVertex2f(0,0.0)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(3.0,4.3)
    glVertex2f(3.0,3.7)
    glVertex2f(0.6,3.7)
    glVertex2f(0.6,4.3)
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
    glVertex2f(2.4,4.0)
    glVertex2f(3.0,4.0)
    glVertex2f(4.0,5.0)
    glVertex2f(3.4,5.0)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(2.4,4.0)
    glVertex2f(3.0,4.0)
    glVertex2f(4.0,3.0)
    glVertex2f(3.4,3.0)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(4.0,7.0)
    glVertex2f(3.4,7.0)
    glVertex2f(3.4,5.0)
    glVertex2f(4.0,5.0)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(4.0,3.0)
    glVertex2f(3.4,3.0)
    glVertex2f(3.4,1.0)
    glVertex2f(4.0,1.0)
    glEnd()
    
    glPopMatrix()
    
    glEndList()
    
def W_letter():
    info = letter_dict.get('W')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)
    glPushMatrix()
    
    glBegin(GL_POLYGON)
    glVertex2f(0.0,4.0)
    glVertex2f(0.0,8.0)
    glVertex2f(0.6,8.0)
    glVertex2f(0.6,4.0)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(5.4,4.0)
    glVertex2f(5.4,8.0)
    glVertex2f(6.0,8.0)
    glVertex2f(6.0,4.0)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(2.7,4.0)
    glVertex2f(2.7,8.0)
    glVertex2f(3.3,8.0)
    glVertex2f(3.3,4.0)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0.0,4.0)
    glVertex2f(0.6,4.0)
    glVertex2f(1.8,0.0)
    glVertex2f(1.2,0.0)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(2.7,4.0)
    glVertex2f(3.3,4.0)
    glVertex2f(4.8,0.0)
    glVertex2f(4.2,0.0)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(5.4,4.0)
    glVertex2f(6.0,4.0)
    glVertex2f(4.8,0.0)
    glVertex2f(4.2,0.0)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(2.7,4.0)
    glVertex2f(3.3,4.0)
    glVertex2f(1.8,0.0)
    glVertex2f(1.2,0.0)
    glEnd()
    
    glPopMatrix()

    glEndList()
    
def r_Letter():
    info = letter_dict.get('r')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)
    
    
    glBegin(GL_POLYGON)
    glVertex2f(0.0, 4.4)
    glVertex2f(0.6, 5.0)
    glVertex2f(0.6, 0.0)
    glVertex2f(0.0, 0.0)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(0.6,5.0)
    glVertex2f(0.0,4.4)
    glVertex2f(4.0,4.4)
    glVertex2f(3.4,5.0)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(3.4,5.0)
    glVertex2f(4.0,4.4)
    glVertex2f(4.0,3.4)
    glVertex2f(3.4,3.4)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(0.0,4.2)
    glVertex2f(0.6,4.2)
    glVertex2f(1.2,4.8)
    glVertex2f(0.6,4.8)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(4.0,4.2)
    glVertex2f(3.4,4.2)
    glVertex2f(2.8,4.8)
    glVertex2f(3.4,4.8)
    glEnd()
    
    glEndList()
   