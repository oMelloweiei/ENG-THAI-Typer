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
	'Z': [90, 4, 0],
	'E': [69, 4, 0],
	'u': [117, 4, 0],
	'ต': [181, 4, 0],
	'ฮ': [206, 4, 0],
	'ู': [217, 3.4, 0]
}

ASCII = 0
SIZE = 1
CLST = 2

def init_font():
    To_Tao()
    Hor()
    Oo()
    E()
    Z()
    u()

##################### ต #####################
def To_Tao():
    info = letter_dict.get('ต')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)
    
    glBegin(GL_POLYGON)
    #glColor3f(255 , 0 , 0)
    glVertex2f(0, 4.4)
    glVertex2f(0.6, 5.0)
    glVertex2f(0.6, 0)
    glVertex2f(0,0)
    glEnd()

    #เส้นบน(ซ้าย)
    glBegin(GL_POLYGON)
    #glColor3f(0 , 255 , 0)
    glVertex2f(0, 4.4)
    glVertex2f(0.6, 5.0)
    glVertex2f(1.4, 5.0)
    glVertex2f(2.0, 4.4)
    glEnd()
    
    #เส้นบน(ขวา)
    glBegin(GL_POLYGON)
    #glColor3f(0 , 255 , 0)
    glVertex2f(2, 4.4)
    glVertex2f(2.6, 5.0)
    glVertex2f(3.4, 5.0)
    glVertex2f(4.0, 4.4)
    glEnd()

    #เส้นเฉือนดิ่ง(ซ้าย)
    glBegin(GL_POLYGON)
    #glColor3f(255 , 255 , 255)
    glVertex2f(2.0 + 0.3, 4.2)
    glVertex2f(1.2 + 0.3, 5.0)
    glVertex2f(0.6 + 0.3, 5.0)
    glVertex2f(1.4 + 0.3, 4.2)
    glEnd()

    #เส้นเฉือนดิ่ง(ขวา)
    glBegin(GL_POLYGON)
    #glColor3f(255 , 255 , 255)
    glVertex2f(2.4 + 0.1, 5.0)
    glVertex2f(3.0 + 0.1, 5.0)
    glVertex2f(2.2 + 0.1, 4.2)
    glVertex2f(1.6 + 0.1, 4.2)
    glEnd()

    #เส้นดิ่ง
    glBegin(GL_POLYGON)
    #glColor3f(255 , 255 , 255)
    glVertex2f(2.3, 4.4)
    glVertex2f(1.7, 4.4)
    glVertex2f(1.7, 3.4)
    glVertex2f(2.3, 3.4)
    glEnd()
    

    #เส้นเฉือน(ซ้าย)
    glBegin(GL_POLYGON)
    #glColor3f(100,100 , 0)
    glVertex2f(0 , 4.2)
    glVertex2f(0.8, 5.0)
    glVertex2f(1.4, 5.0)
    glVertex2f(0.6, 4.2)
    glEnd()

    glBegin(GL_POLYGON)
    #glColor3f(0 , 0 , 255)
    glVertex2f(4.0, 4.4)
    glVertex2f(4.0, 0)
    glVertex2f(3.4, 0)
    glVertex2f(3.4, 4.4)
    glEnd()

    #เส้นเฉือน(ขวา)
    glBegin(GL_POLYGON)
    #glColor3f(100,100 , 0)
    glVertex2f(4.0, 4.2)
    glVertex2f(3.4, 4.2)
    glVertex2f(2.6, 5.0)
    glVertex2f(3.2, 5.0)
    glEnd()

    #เส้นใน
    glBegin(GL_POLYGON)
    #glColor3f(100,100 , 0)
    glVertex2f(0.6, 0.0)
    glVertex2f(2.6, 2.0)
    glVertex2f(2.0, 2.0)
    glVertex2f(0, 0)
    glEnd()

    #เส้นหัว
    glBegin(GL_POLYGON)
    #glColor3f(100,100 , 0)
    glVertex2f(2.6, 2.0)
    glVertex2f(1.4, 2.0)
    glVertex2f(1.4, 2.6)
    glVertex2f(2.6, 2.6)
    glEnd()
    
    #glPopMatrix()
    glEndList()


##################### ฮ #####################
def Hor():
    info = letter_dict.get('ฮ')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)
    
    glBegin(GL_POLYGON)
    glVertex2f(0.6, 3)
    glVertex2f(2,3)
    glVertex2f(2,2.4)
    glVertex2f(0,2.4)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(0.6, 2.4)
    glVertex2f(0.0, 2.4)
    glVertex2f(0,0.6)
    glVertex2f(0.6,0)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(0,0.6)
    glVertex2f(3.4,0.6)
    glVertex2f(3.4,0)
    glVertex2f(0.6,0)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(2.8,4.8)
    glVertex2f(3.4,4.8)
    glVertex2f(4.0,5.4)
    glVertex2f(3.4,5.4)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(3.4,5.4)
    glVertex2f(4.0,5.4)
    glVertex2f(4.0,6.0)
    glVertex2f(3.4,6.0)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(4.0,0.6)
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
    glVertex2f(3.8,1.2)
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

    #glPopMatrix()
    glEndList()


##################### อู #####################
def Oo():
    info = letter_dict.get('ู')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)

    glPushMatrix()
    glTranslatef(0,-4,0)
    glBegin(GL_POLYGON)
    glVertex2f(1.2,3)
    glVertex2f(2,3)
    glVertex2f(2,2.4)
    glVertex2f(1.2,2.4)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(2.3,3)
    glVertex2f(1.7,3)
    glVertex2f(1.7,1)
    glVertex2f(2.3,0.4)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(1.7,1)
    glVertex2f(4,1)
    glVertex2f(3.4,0.4)
    glVertex2f(2.3,0.4)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(4,3)
    glVertex2f(3.4,3)
    glVertex2f(3.4,0.4)
    glVertex2f(4,1)
    glEnd()

    #glColor3f(1,0,0)
               
    glBegin(GL_POLYGON)
    glVertex2f(2.3, 1.2)
    glVertex2f(1.7, 1.2)
    glVertex2f(2.3, 0.6)
    glVertex2f(3, 0.6)
    glEnd() 

    glBegin(GL_POLYGON)
    glVertex2f(3.4, 1.2)
    glVertex2f(4, 1.2)
    glVertex2f(3.4, 0.6)
    glVertex2f(2.8, 0.6)
    glEnd() 
    
    glPopMatrix()
    glEndList()


##################### E #####################
def E():
    info = letter_dict.get('E')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)

    
    glBegin(GL_POLYGON)
    glVertex2f(0,8)
    glVertex2f(4,8)
    glVertex2f(4,7.4)
    glVertex2f(0,7.4)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(0,0.6)
    glVertex2f(4,0.6)
    glVertex2f(4,0)
    glVertex2f(0,0)
    glEnd()

    #glColor3f(1,1,0)

    glBegin(GL_POLYGON)
    glVertex2f(0.6,8)
    glVertex2f(0,8)
    glVertex2f(0,0)
    glVertex2f(0.6,0)
    glEnd()

    #glColor3f(0,1,1)

    glBegin(GL_POLYGON)
    glVertex2f(0,4.3)
    glVertex2f(3.2,4.3)
    glVertex2f(3.2,3.7)
    glVertex2f(0,3.7)
    glEnd()
    
    #glPopMatrix()
    glEndList()


##################### Z #####################
def Z():
    info = letter_dict.get('Z')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)

    glBegin(GL_POLYGON)
    glVertex2f(0,8)
    glVertex2f(4,8)
    glVertex2f(4,7.4)
    glVertex2f(0,7.4)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(0,0.6)
    glVertex2f(4,0.6)
    glVertex2f(4,0)
    glVertex2f(0,0)
    glEnd()

    #glColor3f(1,1,0)

    glBegin(GL_POLYGON)
    glVertex2f(4,7.4)
    glVertex2f(3.4,7.4)
    glVertex2f(0,0.6)
    glVertex2f(0.6,0.6)
    glEnd()

    #glPopMatrix()
    glEndList()


##################### u #####################
def u():
    info = letter_dict.get('u')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)

    glBegin(GL_POLYGON) #1
    glVertex2f(0.6, 5)
    glVertex2f(0, 5)
    glVertex2f(0, 1.6)
    glVertex2f(0.6, 1)
    glEnd()

    glBegin(GL_POLYGON) #2
    glVertex2f(4, 5)
    glVertex2f(3.4, 5)
    glVertex2f(3.4, 1)
    glVertex2f(4, 1.6)
    glEnd()

    glBegin(GL_POLYGON) #3
    glVertex2f(1, 0.6)
    glVertex2f(3, 0.6)
    glVertex2f(2.4, 0)
    glVertex2f(1.6, 0)
    glEnd()

   # เส้นมุมเฉียง
   # glColor3f(0,0,1)     
    glBegin(GL_POLYGON) #5
    glVertex2f(0, 1.6)
    glVertex2f(0, 0.8)
    glVertex2f(0.8, 0)
    glVertex2f(1.6, 0)
    glEnd()

    glBegin(GL_POLYGON) #6
    glVertex2f(2.4, 0)
    glVertex2f(4, 1.6)
    glVertex2f(4, 0.8)
    glVertex2f(3.2, 0)
    glEnd()

    #glPopMatrix()
    glEndList()
