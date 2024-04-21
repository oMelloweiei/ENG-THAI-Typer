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

mini_height = 5
mini_width = 4
big_height = 8

ex_height_b = -3

move = 5

letter_dict = {
	'a': [97, 4, 0],
	'F': [70, 4, 0],
	'v': [118, 4, 0],
	'ง': [167, 3, 0],
	'น': [185, 4, 0],
	'ิ': [212, 3, 0]
}

ASCII = 0
SIZE = 1
CLST = 2

def init_font():
    asmall()
    SNAKE()
    vsmall()
    fbig()
    SARAEI()
    Nor_Nu()

def SNAKE():
    info = letter_dict.get('ง')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)
    
    #เส้นซ้ายสุด
    glBegin(GL_POLYGON)
    glVertex2f(0.6, 4)
    glVertex2f(0, 4)
    glVertex2f(0,0.6)
    glVertex2f(0.6,0)
    glEnd()
    
    #เล้นนอนล่าง
    glBegin(GL_POLYGON)
    glVertex2f(0,0.6)
    glVertex2f(2.4,0.6)
    glVertex2f(2.4,0)
    glVertex2f(0.6,0)
    glEnd()
    
    #เส้นขวาสุด
    glBegin(GL_POLYGON)
    glVertex2f(3.0,0.6)
    glVertex2f(2.4,0)
    glVertex2f(2.4,mini_height)
    glVertex2f(3.0,5.0)
    glEnd()
    
    #เส้นบนสุด
    glBegin(GL_POLYGON)
    glVertex2f(3,mini_height) 
    glVertex2f(3,4.4) 
    glVertex2f(1.6,4.4) 
    glVertex2f(1.6,mini_height) 
    glEnd()

    #ทะแยงล่างขวา           
    glBegin(GL_POLYGON)
    glVertex2f(2.4,0.8)
    glVertex2f(3.0,0.8)
    glVertex2f(1.6,0.0)
    glVertex2f(2.4 ,0.0)
    glEnd() 

    #ทะแยงล่างซ้าย
    glBegin(GL_POLYGON)
    glVertex2f(0.6, 0.8)
    glVertex2f(0.0, 0.8)
    glVertex2f(0.6, 0.2)
    glVertex2f(1.2, 0.2)
    glEnd() 

    glEndList()
    
def Nor_Nu():
    info = letter_dict.get('น')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)
    
    #เส้นซ้ายสุด
    glBegin(GL_POLYGON)
    glVertex2f(0.6, 5)
    glVertex2f(0, 5)
    glVertex2f(0,0.6)
    glVertex2f(0.6,0)
    glEnd()
    
    #เล้นนอนล่าง
    glBegin(GL_POLYGON)
    glVertex2f(0,0.6)
    glVertex2f(3.4,0.6)
    glVertex2f(2.8,0)
    glVertex2f(0.6,0)
    glEnd()
    
    #เส้นขวาสุด
    glBegin(GL_POLYGON)
    glVertex2f(4.0,0.0)
    glVertex2f(3.4,0.0)
    glVertex2f(3.4,mini_height)
    glVertex2f(4.0,5.0)
    glEnd()

    #ทะแยงล่างขวา           
    glBegin(GL_POLYGON)
    glVertex2f(3.4,1.2)
    glVertex2f(4.0,1.2)
    glVertex2f(3.0 ,0.0)
    glVertex2f(2.4 ,0.0)
    glEnd() 

    #ทะแยงล่างซ้าย
    glBegin(GL_POLYGON)
    glVertex2f(0.6, 0.8)
    glVertex2f(0.0, 0.8)
    glVertex2f(0.6, 0.2)
    glVertex2f(1.2, 0.2)
    glEnd() 

    glEndList()
    
def SARAEI():
    info = letter_dict.get('ิ')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)
    glPushMatrix()
    glTranslatef(1,6,0)
    
    #เส้นล่างสุด
    glBegin(GL_POLYGON)
    glVertex2f(0,0.6)
    glVertex2f(0,0.0)
    glVertex2f(3,0)
    glVertex2f(3,0.6)
    glEnd()

    glPopMatrix()
    glEndList()
    
def vsmall():
    info = letter_dict.get('v')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)
    
    glBegin(GL_POLYGON)
    glVertex2f(0.6 , 5)
    glVertex2f(0, 5)
    glVertex2f(0, 3.2)
    glVertex2f(0.6, 3.2)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0.0,3.2)
    glVertex2f(0.6,3.2)
    glVertex2f(2.2,0.0)
    glVertex2f(1.6,0.0)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(3.4,3.2)
    glVertex2f(4.0,3.2)
    glVertex2f(2.2,0.0)
    glVertex2f(1.6,0.0)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(4 , 5)
    glVertex2f(3.4, 5)
    glVertex2f(3.4 , 3.2)
    glVertex2f(4 , 3.2)
    glEnd()

    glEndList()

def fbig():
    info = letter_dict.get('F')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)
    
    glBegin(GL_POLYGON) #1
    glVertex2f(0.6 , 8)
    glVertex2f(0, 8)
    glVertex2f(0, 0)
    glVertex2f(0.6, 0)
    glEnd()

    glBegin(GL_POLYGON) #2
    glVertex2f(4 , 8)
    glVertex2f(0, 8)
    glVertex2f(0, 7.4)
    glVertex2f(4, 7.4)
    glEnd()

    glBegin(GL_POLYGON) #2
    glVertex2f(3 , 4.4)
    glVertex2f(0, 4.4)
    glVertex2f(0, 3.8)
    glVertex2f(3, 3.8)
    glEnd()

    glEndList()
    
def asmall():
    info = letter_dict.get('a')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)
    
    glBegin(GL_POLYGON) #1
    glVertex2f(0.6 , 4.4)
    glVertex2f(0, 4.4)
    glVertex2f(0, 3.8)
    glVertex2f(0.6, 3.8)
    glEnd()

    glBegin(GL_POLYGON) #2
    glVertex2f(0.6 , 5)
    glVertex2f(0.6, 5)
    glVertex2f(0, 4.4)
    glVertex2f(0.6, 4.4)
    glEnd() 
     
    glBegin(GL_POLYGON) #3
    glVertex2f(3.4 , 5)
    glVertex2f(0.6, 5)
    glVertex2f(0.6, 4.4)
    glVertex2f(3.4, 4.4)
    glEnd()

    glBegin(GL_POLYGON) #4
    glVertex2f(3.4, 5)
    glVertex2f(3.4, 5)
    glVertex2f(3.4, 4.4)
    glVertex2f(4, 4.4)
    glEnd()

    glBegin(GL_POLYGON) #5
    glVertex2f(4 , 4.4)
    glVertex2f(3.4, 4.4)
    glVertex2f(3.4, 0.6)
    glVertex2f(4, 0.6)
    glEnd()

    glBegin(GL_POLYGON) #6
    glVertex2f(4 , 0.6)
    glVertex2f(3.4, 0.6)
    glVertex2f(3.4, 0)
    glVertex2f(3.4, 0)
    glEnd()

    glBegin(GL_POLYGON) #7
    glVertex2f(3.4 , 0.6)
    glVertex2f(0.6, 0.6)
    glVertex2f(0.6, 0)
    glVertex2f(3.4, 0)
    glEnd()

    glBegin(GL_POLYGON) #8
    glVertex2f(0.6 , 0.6)
    glVertex2f(0, 0.6)
    glVertex2f(0.6, 0)
    glVertex2f(0.6, 0)
    glEnd()

    glBegin(GL_POLYGON) #9
    glVertex2f(0.6 , 2.4)
    glVertex2f(0, 2.4)
    glVertex2f(0, 0.6)
    glVertex2f(0.6, 0.6)
    glEnd()

    glBegin(GL_POLYGON) #10
    glVertex2f(0.6 , 3)
    glVertex2f(0.6, 3)
    glVertex2f(0, 2.4)
    glVertex2f(0.6, 2.4)
    glEnd()

    glBegin(GL_POLYGON) #11
    glVertex2f(3.4 , 3)
    glVertex2f(0.6, 3)
    glVertex2f(0.6, 2.4)
    glVertex2f(3.4, 2.4)
    glEnd()

    glBegin(GL_POLYGON) #12
    glVertex2f(0.6 , 5)
    glVertex2f(0, 4.4)
    glVertex2f(0.6, 4.2)
    glVertex2f(1.2, 4.8)
    glEnd()

    glBegin(GL_POLYGON) #13
    glVertex2f(4 , 4.4)
    glVertex2f(3.4, 5)
    glVertex2f(3, 4.4)
    glVertex2f(3.4, 4)
    glEnd()

    glBegin(GL_POLYGON) #14
    glVertex2f(4 , 0.6)
    glVertex2f(3.4, 1)
    glVertex2f(3, 0.6)
    glVertex2f(3.4, 0)
    glEnd()

    glBegin(GL_POLYGON) #15
    glVertex2f(0 , 0.6)
    glVertex2f(0.6, 1)
    glVertex2f(1, 0.6)
    glVertex2f(0.6, 0)
    glEnd()

    glBegin(GL_POLYGON) #16
    glVertex2f(0.6 , 3)
    glVertex2f(0, 2.4)
    glVertex2f(0.6, 2)
    glVertex2f(1, 2.4)
    glEnd()

    glEndList()
   