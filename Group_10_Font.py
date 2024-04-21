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

letter_dict = {
	'็': [195, 3.4, 0],
	'ฉ': [175, 4, 0],
	'บ': [227, 4, 0],
	'V': [86, 4, 0],
	'A': [65, 4, 0],
	'q': [113, 4, 0],
}

ASCII = 0
SIZE = 1
CLST = 2

move = 5

def init_font():
    V_letter()
    A_letter()
    q_letter()
    Bor_Baimai()
    Chor_Ching()
    Maitaikhu()

def V_letter():
    
    info = letter_dict.get('V')
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
    glVertex2f(3.4,4.0)
    glVertex2f(3.4,8.0)
    glVertex2f(4.0,8.0)
    glVertex2f(4.0,4.0)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0.0,4.0)
    glVertex2f(0.6,4.0)
    glVertex2f(2.3,0.0)
    glVertex2f(1.7,0.0)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(3.4,4.0)
    glVertex2f(4.0,4.0)
    glVertex2f(2.3,0.0)
    glVertex2f(1.7,0.0)
    glEnd()
    
    glPopMatrix()
    glEndList()
    
def q_letter():
    info = letter_dict.get('q')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)
    glPushMatrix()
    glBegin(GL_POLYGON)
    glVertex2f(0.0,0.6)
    glVertex2f(0.6,0.0)
    glVertex2f(0.6,5.0)
    glVertex2f(0.0,4.4)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(3.4,-3.0)
    glVertex2f(4.0,-3.0)
    glVertex2f(4.0,4.4)
    glVertex2f(3.4,5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0.0,4.4)
    glVertex2f(4.0,4.4)
    glVertex2f(3.4,5.0)
    glVertex2f(0.6,5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0.6,0.0)
    glVertex2f(4.0,0.0)
    glVertex2f(4.0,0.6)
    glVertex2f(0.0,0.6)
    glEnd()

    # glColor3f(1,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(1.2,4.8)
    glVertex2f(0.6,4.8)
    glVertex2f(0.0,4.2)
    glVertex2f(0.6,4.2)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(3.4,4.8)
    glVertex2f(2.8,4.8)
    glVertex2f(3.4,4.2)
    glVertex2f(4.0,4.2)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0.0,0.8)
    glVertex2f(0.6,0.8)
    glVertex2f(1.2,0.2)
    glVertex2f(0.6,0.2)
    glEnd()

    glPopMatrix()
    glEndList()
    
def A_letter():
    info = letter_dict.get('A')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)
    
    glPushMatrix()

    glBegin(GL_POLYGON)
    glVertex2f(0, 7.4)
    glVertex2f(0.6, 8.0)
    glVertex2f(0.6,0.0)
    glVertex2f(0,0.0)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(4.0, 7.4)
    glVertex2f(3.4, 8.0)
    glVertex2f(3.4,0.0)
    glVertex2f(4.0,0.0)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(3.4,4.0)
    glVertex2f(3.4,3.4)
    glVertex2f(0.6,3.4)
    glVertex2f(0.6,4.0)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(3.4,8.0)
    glVertex2f(3.4,7.4)
    glVertex2f(0.6,7.4)
    glVertex2f(0.6,8.0)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0.6,7.8)
    glVertex2f(1.2,7.8)
    glVertex2f(0.6,7.2)
    glVertex2f(0.0,7.2)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(3.4,7.8)
    glVertex2f(2.8,7.8)
    glVertex2f(3.4,7.2)
    glVertex2f(4.0,7.2)
    glEnd()

    glPopMatrix()
    
    glEndList()
    
def Maitaikhu():
    info = letter_dict.get('็')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)
    glPushMatrix()
    glTranslatef(1,move+1,0)
    
    glBegin(GL_POLYGON)
    glVertex2f(0, 1.9)
    glVertex2f(0.6, 2.5)
    glVertex2f(0.6, 0)
    glVertex2f(0, 0)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(1.2,0.6)
    glVertex2f(1.2,0.0)
    glVertex2f(2.4,0.0)
    glVertex2f(3.0,0.6)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(2.4,0.2)
    glVertex2f(3.0,0.8)
    glVertex2f(2.4,0.8)
    glVertex2f(1.8,0.2)
    glEnd()

    glColor3f(1,1,1)
    glBegin(GL_POLYGON)
    glVertex2f(0.6,2.5)
    glVertex2f(0.0,1.9)
    glVertex2f(2.8,1.9)
    glVertex2f(3.4,2.5)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(2.4,1.4)
    glVertex2f(2.4,0.6)
    glVertex2f(3.0,0.6)
    glVertex2f(3.0,1.4)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(1.8,1.4)
    glVertex2f(1.8,0.8)
    glVertex2f(3.0,0.8)
    glVertex2f(3.0,1.4)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0.6,1.2)
    glVertex2f(1.8,0.0)
    glVertex2f(1.2,0.0)
    glVertex2f(0.0,1.2)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(2.8,2.5)
    glVertex2f(3.4,2.5)
    glVertex2f(3.4,3.0)
    glVertex2f(2.8,3.0)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0.0,1.7)
    glVertex2f(0.6,1.7)
    glVertex2f(1.2,2.3)
    glVertex2f(0.6,2.3)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(2.2,2.1)
    glVertex2f(2.8,2.1)
    glVertex2f(3.4,2.7)
    glVertex2f(2.8,2.7)
    glEnd()
    glPopMatrix()
    glEndList()
    
    
def Bor_Baimai():
    info = letter_dict.get('บ')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)
    
    glBegin(GL_POLYGON)
    glVertex2f(3.4, 5)
    glVertex2f(4.0, 5)
    glVertex2f(4.0, 0.6)
    glVertex2f(3.4,0.0)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0.6, 5)
    glVertex2f(0.0, 5)
    glVertex2f(0.0, 0.6)
    glVertex2f(0.6,0.0)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(0.6,0.6)
    glVertex2f(0.6,0)
    glVertex2f(3.4,0)
    glVertex2f(4,0.6)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(0.0,0.8)
    glVertex2f(0.6,0.2)
    glVertex2f(1.2,0.2)
    glVertex2f(0.6,0.8)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(2.8,0.2)
    glVertex2f(3.4,0.2)
    glVertex2f(4.0,0.8)
    glVertex2f(3.4,0.8)
    glEnd()
    glEndList()

def Chor_Ching():
    info = letter_dict.get('ฉ')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)
    
    glBegin(GL_POLYGON)
    glVertex2f(0.6, 2.4)
    glVertex2f(0, 2.4)
    glVertex2f(0,0.6)
    glVertex2f(0.6,0)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(0,0.6)
    glVertex2f(3.4,0.6)
    glVertex2f(2.8,0)
    glVertex2f(0.6,0)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(4.0,0.0)
    glVertex2f(3.4,0.0)
    glVertex2f(3.4,5)
    glVertex2f(4.0,4.4)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(3.4,5) 
    glVertex2f(4.0,4.4) 
    glVertex2f(0.0,4.4) 
    glVertex2f(0.6,5) 
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(0.0,4.4)
    glVertex2f(0.6,5.0)
    glVertex2f(0.6,3.2)
    glVertex2f(0.0,3.2)
    glEnd()
               
    glBegin(GL_POLYGON)
    glVertex2f(3.4,1.2)
    glVertex2f(4.0,1.2)
    glVertex2f(3.0 ,0.0)
    glVertex2f(2.4 ,0.0)
    glEnd() 

    glBegin(GL_POLYGON)
    glVertex2f(0.6,4.8)
    glVertex2f(1.2,4.8)
    glVertex2f(0.6 ,4.2)
    glVertex2f(0.0 ,4.2)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(3.4, 4.2)
    glVertex2f(4.0, 4.2)
    glVertex2f(3.4, 4.8)
    glVertex2f(2.8, 4.8)
    glEnd() 

    glBegin(GL_POLYGON)
    glVertex2f(0.6, 0.8)
    glVertex2f(0.0, 0.8)
    glVertex2f(0.6, 0.2)
    glVertex2f(1.2, 0.2)
    glEnd() 

    glEndList()
   
