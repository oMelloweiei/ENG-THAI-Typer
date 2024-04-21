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

move = 5 # ค่าของการเลื่อนของ 'z'

letter_dict = {
	'y': [121, 4, 0],
	'I': [73, 3, 0],
	'd': [100, 4, 0],
	'ว': [199, 3, 0],
	'ด': [180, 4, 0],
	'ึ': [214, 3, 0]
}

ASCII = 0
SIZE = 1
CLST = 2


def init_font():
    wowan()
    dordek()
    au()
    yyellow()
    Iiron()
    ddog()

def wowan(): #สร้าง ว
    info = letter_dict.get('ว')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)
    
    glBegin(GL_POLYGON) 
    glVertex2f(0,4.4) 
    glVertex2f(0.6,5) 
    glVertex2f(2.4,5) 
    glVertex2f(3,4.4) 
    glEnd()
    
    glBegin(GL_POLYGON) 
    glVertex2f(0, 4.4)
    glVertex2f(0.6, 4.4)
    glVertex2f(0.6, 3)
    glVertex2f(0, 3)
    glEnd()
    
    glBegin(GL_POLYGON) 
    glVertex2f(3,4.4)
    glVertex2f(3,0.6)
    glVertex2f(2.4,0)
    glVertex2f(2.4,4.4)
    glEnd()
       
    glBegin(GL_POLYGON) 
    glVertex2f(3,0.6) 
    glVertex2f(2.4,0) 
    glVertex2f(1,0)
    glVertex2f(1,0.6)  
    glEnd()
    
    glBegin(GL_POLYGON) 
    glVertex2f(2.4,4) 
    glVertex2f(2,4.4) 
    glVertex2f(2.4,5) 
    glVertex2f(3,4.4) 
    glEnd()
    
    glBegin(GL_POLYGON) 
    glVertex2f(0,4.4) 
    glVertex2f(0.6,5) 
    glVertex2f(1,4.4) 
    glVertex2f(0.6,4) 
    glEnd()
    
    glBegin(GL_POLYGON) 
    glVertex2f(2,0.6)   
    glVertex2f(2.4,1) 
    glVertex2f(3,0.6) 
    glVertex2f(2.4,0) 
    glEnd()

    glEndList()


def yyellow():#สร้าง y
    info = letter_dict.get('y')
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
    glVertex2f(4.0,-2.4)
    glVertex2f(3.4,-2.4)
    glVertex2f(3.4,5)
    glVertex2f(4.0,5.0)
    glEnd()
    
    
    glBegin(GL_POLYGON)
    glVertex2f(0.0,5.0)
    glVertex2f(0.6,5.0)
    glVertex2f(0.6,2.2)
    glVertex2f(0.0,2.2)
    glEnd()
            
    glBegin(GL_POLYGON)
    glVertex2f(3.4,1.2)
    glVertex2f(4.0,1.2)
    glVertex2f(3.0 ,0.0)
    glVertex2f(2.4 ,0.0)
    glEnd() 

    glBegin(GL_POLYGON)
    glVertex2f(0.6, 0.8)
    glVertex2f(0.0, 0.8)
    glVertex2f(0.6, 0.2)
    glVertex2f(1.2, 0.2)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0.6,-2.4)
    glVertex2f(3.4,-2.4)
    glVertex2f(3.4,-3)
    glVertex2f(0.6,-3)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(3.2,-3.0)
    glVertex2f(3.4,-3.0)
    glVertex2f(4.0,-2.4)
    glVertex2f(3.0 ,-2.4)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(3.2,-2.4)
    glVertex2f(3.4,-2.4)
    glVertex2f(4.0,-1.6)
    glVertex2f(4.0,-1.6)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0.6, -3.0)
    glVertex2f(0.6, -3.0)
    glVertex2f(0.0, -2.0)
    glVertex2f(0.6, -2.0)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0.6,-2.4)
    glVertex2f(0.8,-2.4)
    glVertex2f(0.6,-2.0)
    glVertex2f(0.0,-2.0)
    glEnd()

    glEndList()
    
def dordek():#สร้าง ด
    info = letter_dict.get('ด')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)
    
    glBegin(GL_POLYGON) 
    glVertex2f(3.4,5) 
    glVertex2f(4,4.4) 
    glVertex2f(0,4.4) 
    glVertex2f(0.6,5) 
    glEnd()
    
    glBegin(GL_POLYGON) 
    glVertex2f(3.4,5) 
    glVertex2f(4,4.4) 
    glVertex2f(4,0) 
    glVertex2f(3.4,0) 
    glEnd()
    
    glBegin(GL_POLYGON) 
    glVertex2f(0.6,5) 
    glVertex2f(0,4.4) 
    glVertex2f(0,0) 
    glVertex2f(0.6,0) 
    glEnd()
    
    
    glBegin(GL_POLYGON) 
    glVertex2f(2.7,2.6) 
    glVertex2f(1.3,2.6) 
    glVertex2f(1.3,2) 
    glVertex2f(2.7,2) 
    glEnd()
    
    glBegin(GL_POLYGON) 
    glVertex2f(2.7,2)
    glVertex2f(2.1,2)  
    glVertex2f(0,0)
    glVertex2f(0.6,0)  
    glEnd()
    
    glBegin(GL_POLYGON) 
    glVertex2f(3.4,4.2)
    glVertex2f(3.2,4.4)  
    glVertex2f(3.4,5)
    glVertex2f(4,4.4)  
    glEnd()
    
    glBegin(GL_POLYGON) 
    glVertex2f(0.6,4.2)
    glVertex2f(0.8,4.4)  
    glVertex2f(0.6,5)
    glVertex2f(0,4.4)  
    glEnd() 

    glEndList()

   
def Iiron():#สร้าง I
    info = letter_dict.get('I')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)

    glPushMatrix()
    glTranslatef(-0.5,0,0)
    glBegin(GL_POLYGON) 
    glVertex2f(1.7,0) 
    glVertex2f(2.3,0) 
    glVertex2f(2.3,8) 
    glVertex2f(1.7,8) 
    glEnd()
    
    glBegin(GL_POLYGON) 
    glVertex2f(0.5,0) 
    glVertex2f(3.5,0) 
    glVertex2f(3.5,0.6) 
    glVertex2f(0.5,0.6) 
    glEnd()
    
    glBegin(GL_POLYGON) 
    glVertex2f(0.5,8) 
    glVertex2f(3.5,8) 
    glVertex2f(3.5,7.4) 
    glVertex2f(0.5,7.4)  
    glEnd()
    glPopMatrix()
    glEndList()
    
def ddog():#สร้าง d
    info = letter_dict.get('d')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)

    glBegin(GL_POLYGON) 
    glVertex2f(0,4.4) 
    glVertex2f(0.6,5) 
    glVertex2f(3.4,5) 
    glVertex2f(4,4.4) 
    glEnd()
    
    glBegin(GL_POLYGON) 
    glVertex2f(0, 4.4)
    glVertex2f(0.6, 4.4)
    glVertex2f(0.6, 0)
    glVertex2f(0, 0.6)
    glEnd()
    
    glBegin(GL_POLYGON) 
    glVertex2f(4,8)
    glVertex2f(4,0.6)
    glVertex2f(3.4,0)
    glVertex2f(3.4,8)
    glEnd()
       
    glBegin(GL_POLYGON) 
    glVertex2f(4,0.6) 
    glVertex2f(3.4,0) 
    glVertex2f(0.6,0)
    glVertex2f(0,0.6)  
    glEnd()
     
    glBegin(GL_POLYGON) 
    glVertex2f(0,4.4) 
    glVertex2f(0.6,5) 
    glVertex2f(1,4.4) 
    glVertex2f(0.6,4) 
    glEnd()
    
    glBegin(GL_POLYGON) 
    glVertex2f(0,0.6) 
    glVertex2f(0.6,0) 
    glVertex2f(1,0.6) 
    glVertex2f(0.6,1) 
    glEnd()
    
    glBegin(GL_POLYGON) 
    glVertex2f(3,0.6) 
    glVertex2f(3.4,1) 
    glVertex2f(4,0.6) 
    glVertex2f(3.4,0) 
    glEnd()

    glEndList()
    
def au():#สร้าง สระ  ึ
    info = letter_dict.get('ึ')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)
    glPushMatrix()
    glTranslatef(1,0,0)
    glBegin(GL_POLYGON) 
    glVertex2f(0,6 ) 
    glVertex2f(0,6.6 ) 
    glVertex2f(2.0,6.6 ) 
    glVertex2f(2.0,6) 
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(2.0,6.0)
    glVertex2f(2.3,6.0)
    glVertex2f(2.3,7.0)
    glVertex2f(2.0,7.0)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(3.0,6.0)
    glVertex2f(2.7,6.0)
    glVertex2f(2.7,7.0)
    glVertex2f(3.0,7.0)
    glEnd()

    glBegin(GL_POLYGON) 
    glVertex2f(2.3,6 ) 
    glVertex2f(2.3,6.3 ) 
    glVertex2f(2.7,6.3 ) 
    glVertex2f(2.7,6 ) 
    glEnd()

    glBegin(GL_POLYGON) 
    glVertex2f(2.3,6.7 ) 
    glVertex2f(2.3,7.0 ) 
    glVertex2f(2.7,7.0 ) 
    glVertex2f(2.7,6.7 ) 
    glEnd()
    glPopMatrix()
    glEndList()
