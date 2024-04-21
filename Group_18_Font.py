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

letter_dict = {
	'i': [105, 1, 0],
	'N': [78, 4, 0],
	'ช': [170, 3, 0],
	'ญ': [173, 6.6, 0],
	'ุ': [216, 0.6, 0],
}

ASCII = 0
SIZE = 1
CLST = 2

def init_font():
    Chang()
    YorYing()
    N()
    Au()
    i()
    
def Chang():
    info = letter_dict.get('ช')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE) 
    glPushMatrix()
    glBegin(GL_POLYGON)
    glVertex2f(0,5)
    glVertex2f(0,4.4)
    glVertex2f(1.4,4.4)
    glVertex2f(1.4,5)
    glEnd()

    #2
    glBegin(GL_POLYGON)
    glVertex2f(1.4,5)
    glVertex2f(1.4,4.2)
    glVertex2f(0.8,4.2)
    glVertex2f(0.8,5)
    glEnd()

    #3
    glBegin(GL_POLYGON)
    glVertex2f(1.4,4.2)
    glVertex2f(0.8,4.2)
    glVertex2f(0, 3.3)
    glVertex2f(0.6, 3.3)
    glEnd()
    
    #4
    glBegin(GL_POLYGON)
    glVertex2f(0, 3.3)
    glVertex2f(0.6, 3.3)
    glVertex2f(0.6,0)
    glVertex2f(0,0.6)
    glEnd()

    #5
    glBegin(GL_POLYGON)
    glVertex2f(0.6,0)
    glVertex2f(0,0.6)
    glVertex2f(3,0.6)
    glVertex2f(2.4,0)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(4.0,5.4)
    glVertex2f(3.4,5.4)
    glVertex2f(3.4,6.0)
    glVertex2f(4.0,6.0)
    glEnd()
    
    #6
    glBegin(GL_POLYGON)
    glVertex2f(2.4, 4.2)
    glVertex2f(3, 3.6)
    glVertex2f(3,0.6)
    glVertex2f(2.4,0)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(3.0,3.6)
    glVertex2f(2.4,3.6)
    glVertex2f(1.8,4.2)
    glVertex2f(2.4,4.2)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(1.8,4.2)
    glVertex2f(2.4,4.2)
    glVertex2f(4.0,5.4)
    glVertex2f(3.4,5.4)
    glEnd()
    
    # ขวาล่างตัด   
    glBegin(GL_POLYGON)
    glVertex2f(3,0.6)
    glVertex2f(2.4,0)
    glVertex2f(2.2,0.6)
    glVertex2f(2.4,0.8)
    glEnd()

    # ซ้ายล่างตัด   
    glBegin(GL_POLYGON)
    glVertex2f(0.6,0)
    glVertex2f(0,0.6)
    glVertex2f(0.6,0.8)
    glVertex2f(0.8,0.6)
    glEnd()
    glPopMatrix()
    glEndList()
    
    
def YorYing():
    info = letter_dict.get('ญ')
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
    glVertex2f(6.6,0.6)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(6.0,0.6)
    glVertex2f(6.0,0.0)
    glVertex2f(4.0,0.0)
    glVertex2f(4.0,0.6)
    glEnd()

    # glColor3f(1,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(3.4,0.8)
    glVertex2f(4.0,0.8)
    glVertex2f(4.6,0.2)
    glVertex2f(4.0,0.2)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(6.0,0.8)
    glVertex2f(6.6,0.8)
    glVertex2f(6.0,0.2)
    glVertex2f(5.4,0.2)
    glEnd()

    glPushMatrix()
    glTranslatef(3.5,-2,0)
    glBegin(GL_POLYGON)
    glVertex2f(0, 1.0)
    glVertex2f(0.6, 1.0)
    glVertex2f(0.6, 0)
    glVertex2f(0, 0.6)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0.6, 0.6)
    glVertex2f(0.6, 0.0)
    glVertex2f(1.8, 0.0)
    glVertex2f(2.4, 0.6)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(1.2, 0.0)
    glVertex2f(2.4, 1.2)
    glVertex2f(3.0, 1.2)
    glVertex2f(1.8, 0.0)
    glEnd()

    glPopMatrix()

    glPopMatrix()
    glEndList()
    
    
def Au():
    info = letter_dict.get('ุ')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE) 
    glPushMatrix()

    glTranslatef(0,-1,0)
    glBegin(GL_POLYGON)
    glVertex2f(4.0,-0.6)
    glVertex2f(2.8,-0.6)
    glVertex2f(2.8,0.0)
    glVertex2f(4.0,0.0)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(4.0,0.0)
    glVertex2f(3.4,0.0)
    glVertex2f(3.4,-1.6)
    glVertex2f(4.0,-1.6)
    glEnd()
                  
    glPopMatrix()
    glEndList()
    
def i():
    info = letter_dict.get('i')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE) 
    glPushMatrix()
    glTranslatef(0.2,0,0)
    glBegin(GL_POLYGON) #เส้นตรง
    glVertex2f(0.6, 5.0)
    glVertex2f(0.0, 5.0)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.6, 0.0)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(0.6, 8.0)
    glVertex2f(0.0, 8.0)
    glVertex2f(0.0,6.6)
    glVertex2f(0.6,6.6)
    glEnd()
    
    glPopMatrix()
    glEndList()
    
def N():
    info = letter_dict.get('N')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE) 
    glPushMatrix()
    glBegin(GL_POLYGON)
    glVertex2f(0, 8.0)
    glVertex2f(0.5, 8.0)
    glVertex2f(0.5, 0)
    glVertex2f(0, 0)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(3.7, 8.0)
    glVertex2f(4.2, 8.0)
    glVertex2f(4.2, 0)
    glVertex2f(3.7, 0)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0, 7.7)
    glVertex2f(0.5, 8.0)
    glVertex2f(4.2, 0.2)
    glVertex2f(3.7, 0)
    glEnd()
    glPopMatrix()
    glEndList()
   