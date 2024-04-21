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
	'ฺ': [218, 1, 0],
	'ฐ': [176, 4, 0],
	'ศ': [200, 4, 0],
	'c': [99, 4, 0],
	'H': [72, 4, 0],
	'x': [120, 4, 0]
}

ASCII = 0
SIZE = 1
CLST = 2

def init_font():
    x_Letter()
    c_letter()
    H_letter()
    Sor_Sara()
    Tor_Than()
    PhinThru()

def PhinThru():
    global move , Phin_thailetter
    
    info = letter_dict.get('ฺ')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE) 
    
    glPushMatrix()
    glTranslatef(3,-1,0)
    glBegin(GL_POLYGON)
    glVertex2f(-0.5, 0.25)
    glVertex2f(-0.25, 0.5)
    glVertex2f(0.25, 0.5)
    glVertex2f(0.5, 0.25)
    glVertex2f(0.5, -0.25)
    glVertex2f(0.25, -0.5)
    glVertex2f(-0.25, -0.5)
    glVertex2f(-0.5, -0.25)
    glEnd()
    glPopMatrix()
    glEndList()
    
def Tor_Than():
    info = letter_dict.get('ฐ')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE) 

    glPushMatrix()
    
    glBegin(GL_POLYGON)
    glVertex2f(2.8, 0.0)
    glVertex2f(2.8, 4.4)
    glVertex2f(3.4, 3.8)
    glVertex2f(3.4, 0.6)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(1.2, 0.0)
    glVertex2f(1.2, 2.6)
    glVertex2f(0.6, 2.6)
    glVertex2f(0.6, 0.6)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(1.2, 0.0)
    glVertex2f(1.2, 0.6)
    glVertex2f(2.8, 0.6)
    glVertex2f(2.8, 0.0)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(0.0, 2.6)
    glVertex2f(0.6, 2.6)
    glVertex2f(0.6, 2.0)
    glVertex2f(0.0, 2.0)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0.4, 4.4)
    glVertex2f(1.0, 5.0)
    glVertex2f(4.0, 5.0)
    glVertex2f(3.4, 4.4)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0.0, 4.0)
    glVertex2f(0.6, 4.0)
    glVertex2f(1.0, 4.4)
    glVertex2f(0.4, 4.4)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(3.4,3.8)
    glVertex2f(2.8,3.8)
    glVertex2f(2.2,4.4)
    glVertex2f(2.8,4.4)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(3.4,0.8)
    glVertex2f(2.8,0.8)
    glVertex2f(2.2,0.2)
    glVertex2f(2.8,0.2)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(0.6,0.8)
    glVertex2f(1.2,0.8)
    glVertex2f(1.8,0.2)
    glVertex2f(1.2,0.2)
    glEnd()
    

    glBegin(GL_POLYGON)
    glVertex2f(4.0,-1.0)
    glVertex2f(4.0,-2.4)
    glVertex2f(3.4,-2.4)
    glVertex2f(3.4,-1.0)
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
    
def Sor_Sara():
    info = letter_dict.get('ศ')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)
    
    glPushMatrix()
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
    
    # glColor3f(0,0,1)
    glBegin(GL_POLYGON)
    glVertex2f(2.8, 3.6)
    glVertex2f(4.0, 6.0)
    glVertex2f(3.4, 6.0)
    glVertex2f(2.2, 3.6)
    glEnd()

    glPopMatrix()

    glEndList()
    

def H_letter():
    info = letter_dict.get('H')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE) 
    
    glPushMatrix()

    glBegin(GL_POLYGON)
    glVertex2f(0.0,8.0)
    glVertex2f(0.6,8.0)
    glVertex2f(0.6,0.0)
    glVertex2f(0.0,0.0)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(4.0,8.0)
    glVertex2f(3.4,8.0)
    glVertex2f(3.4,0.0)
    glVertex2f(4.0,0.0)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(4.0,4.3)
    glVertex2f(0,4.3)
    glVertex2f(0,3.7)
    glVertex2f(4.0,3.7)
    glEnd()

    glPopMatrix()
    
    glEndList()
    
def c_letter():
    info = letter_dict.get('c')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE) 

    glPushMatrix()
    
    glBegin(GL_POLYGON)
    glVertex2f(0.6, 5.0)
    glVertex2f(0.0, 4.4)
    glVertex2f(0.0, 0.6)
    glVertex2f(0.6, 0.0)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(4.0,0.6)
    glVertex2f(3.4,0.0)
    glVertex2f(0.6,0.0)    
    glVertex2f(0.0,0.6)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(4.0,4.4)
    glVertex2f(3.4,5.0)
    glVertex2f(0.6,5.0)    
    glVertex2f(0.0,4.4)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(3.4, 5.0)
    glVertex2f(4.0, 4.4)
    glVertex2f(4.0, 3.8)
    glVertex2f(3.4, 3.8)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(3.4, 0.0)
    glVertex2f(4.0, 0.6)
    glVertex2f(4.0, 1.2)
    glVertex2f(3.4, 1.2)
    glEnd()
 
    # glColor3f(0,0,1)
    glBegin(GL_POLYGON)
    glVertex2f(0.0,0.8)
    glVertex2f(0.6,0.8)
    glVertex2f(1.2,0.2)    
    glVertex2f(0.6,0.2)
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

    glPopMatrix()
    
    glEndList()

def x_Letter():
    info = letter_dict.get('x')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE) 

    glPushMatrix()
    
    glBegin(GL_POLYGON)
    glVertex2f(0.0,5.0)
    glVertex2f(0.6,5.0)
    glVertex2f(0.6,4.0)
    glVertex2f(0.0,4.0)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(4.0,5.0)
    glVertex2f(3.4,5.0)
    glVertex2f(3.4,4.0)
    glVertex2f(4.0,4.0)
    glEnd()
        
    glBegin(GL_POLYGON)
    glVertex2f(0.0,0.0)
    glVertex2f(0.6,0.0)
    glVertex2f(0.6,1.0)
    glVertex2f(0.0,1.0)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(4.0,0.0)
    glVertex2f(3.4,0.0)
    glVertex2f(3.4,1.0)
    glVertex2f(4.0,1.0)
    glEnd()
    
    # glColor3f(0,0,1)
    glBegin(GL_POLYGON)
    glVertex2f(0.0,1.0)
    glVertex2f(0.6,1.0)
    glVertex2f(4.0,4.0)
    glVertex2f(3.4,4.0)
    glEnd()    
    
    glBegin(GL_POLYGON)
    glVertex2f(4.0,1.0)
    glVertex2f(3.4,1.0)
    glVertex2f(0.0,4.0)
    glVertex2f(0.6,4.0)
    glEnd()    

    glPopMatrix()

    glEndList()
