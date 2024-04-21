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

mini_height = 5
mini_width = 4
big_height = 8

ex_height_b = -3
#สระเสียงสูง 2.5 กว้าง 

letter_dict = {
	'o': [111, 4, 0],
	'T': [84, 4, 0],
	'ณ': [179, 6.6, 0],
	'๋': [235, 1.8, 0],
	'ส': [202, 4, 0],
	'ฦ': [198, 4, 0]
}

ASCII = 0
SIZE = 1
CLST = 2

def init_font():
    o_letter()
    T_letter()
    No_nen()
    Lu()
    So_sua()
    CHATTAWA()

    
def CHATTAWA():
    info = letter_dict.get('๋')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE) 
    glPushMatrix()  
    glTranslatef(0.6,move,0)
    glBegin(GL_QUADS)
    glVertex2f(2.2,2.3)
    glVertex2f(2.2,1.7)
    glVertex2f(4.0,1.7)
    glVertex2f(4.0,2.3)
    glEnd()
    
    glBegin(GL_QUADS)
    glVertex2f(3.4,1.2)
    glVertex2f(3.4,2.8)
    glVertex2f(2.8,2.8)
    glVertex2f(2.8,1.2)
    glEnd()
    glPopMatrix() 
    glEndList() 
   
    
def So_sua():
    info = letter_dict.get('ส')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE) 
    
    glBegin(GL_POLYGON)
    glVertex2f(0.0,3.8)
    glVertex2f(0.0,4.4)
    glVertex2f(0.6,5.0)
    glVertex2f(0.6,3.8)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(0.0,0.6)
    glVertex2f(0.0,2.0)
    glVertex2f(0.6,2.6)
    glVertex2f(0.6,0.6)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(0.6,2.6)
    glVertex2f(0.0,2.0)
    glVertex2f(4.0,2.0)
    glVertex2f(3.4,2.6)
    glEnd()

    
    glBegin(GL_POLYGON)
    glVertex2f(0.6,0.0)
    glVertex2f(0.0,0.6)
    glVertex2f(1.6,0.6)
    glVertex2f(1.6,0.0)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(0.6,5.0)
    glVertex2f(0.0,4.4)
    glVertex2f(4.0,4.4)
    glVertex2f(3.4,5.0)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(3.4,0.0)
    glVertex2f(3.4,5.0)
    glVertex2f(4.0,4.4)
    glVertex2f(4.0,0.0)
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
    
    glBegin(GL_POLYGON)
    glVertex2f(0.0,0.8)
    glVertex2f(0.6,0.8)
    glVertex2f(1.2,0.2)
    glVertex2f(0.6,0.2)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(0.0,1.8)
    glVertex2f(0.6,1.8)
    glVertex2f(1.0,2.2)
    glVertex2f(0.4,2.2)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(2.8, 3.6)
    glVertex2f(4.0, 6.0)
    glVertex2f(3.4, 6.0)
    glVertex2f(2.2, 3.6)
    glEnd()
          
    glEndList()
    
def Lu():
    info = letter_dict.get('ฦ')
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

    glPopMatrix()
    
    glEndList()
    
def No_nen():
    info = letter_dict.get('ณ')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE) 
    glPushMatrix()
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
    glVertex2f(4,0)
    glVertex2f(3.4,0.6)
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
    glVertex2f(6.0,0.0)
    glVertex2f(6.0,5.0)
    glVertex2f(6.6,5.0)
    glVertex2f(6.6,0.0)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(5.8,0.6)
    glVertex2f(5.2,0.0)
    glVertex2f(4.0,0.0)
    glVertex2f(4.0,0.6)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(5.8,0.6)
    glVertex2f(5.2,0.6)
    glVertex2f(6.0,1.4)
    glVertex2f(6.6,1.4)
    glEnd()

    # glColor3f(1,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(3.4,0.8)
    glVertex2f(4.0,0.8)
    glVertex2f(4.6,0.2)
    glVertex2f(4.0,0.2)
    glEnd()
    
    glPopMatrix()
    glEndList()
    
def T_letter():
    info = letter_dict.get('T')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE) 
    
    glPushMatrix()
    glBegin(GL_POLYGON)
    glVertex2f(0.0,8.0)
    glVertex2f(0.0,7.4)
    glVertex2f(4.0,7.4)
    glVertex2f(4.0,8.0)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex(1.7,8.0)
    glVertex(1.7,0.0)
    glVertex(2.3,0.0)
    glVertex(2.3,8.0)
    glEnd()
    glPopMatrix()
    glEndList()
def o_letter():
    info = letter_dict.get('o')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE) 
    
    glBegin(GL_POLYGON)
    glVertex2f(0.0, 4.4)
    glVertex2f(0.6, 5.0)
    glVertex2f(0.6, 0.0)
    glVertex2f(0.0, 0.6)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(0.6,5.0)
    glVertex2f(0.0,4.4)
    glVertex2f(4.0,4.4)
    glVertex2f(3.4,5.0)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(0.6,0.0)
    glVertex2f(0.0,0.6)
    glVertex2f(4.0,0.6)
    glVertex2f(3.4,0.0)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(3.4,5.0)
    glVertex2f(4.0,4.4)
    glVertex2f(4.0,0.6)
    glVertex2f(3.4,0.0)
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
    
    glBegin(GL_POLYGON)
    glVertex2f(4.0,0.8)
    glVertex2f(3.4,0.8)
    glVertex2f(2.8,0.2)
    glVertex2f(3.4,0.2)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(1.2,0.2)
    glVertex2f(0.6,0.2)
    glVertex2f(0.0,0.8)
    glVertex2f(0.6,0.8)
    glEnd()
    
    glEndList()
