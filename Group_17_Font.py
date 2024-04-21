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
	'O': [79, 4, 0],
	'j': [106, 1, 0],
	'ม': [193, 4, 0],
	'ห': [203, 4, 0],
	'ล': [197, 4, 0],
	'ื': [215, 3, 0]
}

ASCII = 0
SIZE = 1
CLST = 2

def init_font():
    O_letter()
    j_letter()
    MO_MA()
    LO_LING()
    HO_HIP()
    Sara_Uee()
    
def O_letter():
    info = letter_dict.get('O')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE) 
 
    glBegin(GL_POLYGON)
    glVertex2f(0.0, 7.4)
    glVertex2f(0.6, 8.0)
    glVertex2f(0.6, 0.0)
    glVertex2f(0.0, 0.6)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(0.6,8.0)
    glVertex2f(0.0,7.4)
    glVertex2f(4.0,7.4)
    glVertex2f(3.4,8.0)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(0.6,0.0)
    glVertex2f(0.0,0.6)
    glVertex2f(4.0,0.6)
    glVertex2f(3.4,0.0)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(3.4,8.0)
    glVertex2f(4.0,7.4)
    glVertex2f(4.0,0.6)
    glVertex2f(3.4,0.0)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(0.0,7.2)
    glVertex2f(0.6,7.2)
    glVertex2f(1.2,7.8)
    glVertex2f(0.6,7.8)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(4.0,7.2)
    glVertex2f(3.4,7.2)
    glVertex2f(2.8,7.8)
    glVertex2f(3.4,7.8)
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
    
    
def j_letter():
    info = letter_dict.get('j')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE) 
    glPushMatrix()
    glTranslatef(0.2,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(0.6, 8.0)
    glVertex2f(0.0, 8.0)
    glVertex2f(0.0,6.6)
    glVertex2f(0.6,6.6)
    glEnd()

    glBegin(GL_POLYGON) #เส้นตรง
    glVertex2f(0.6, 5.0)
    glVertex2f(0.0, 5.0)
    glVertex2f(0.0, -2.8)
    glVertex2f(0.6, -2.2)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0.0,-2.2)
    glVertex2f(0.6,-2.2)
    glVertex2f(0.0,-2.8)
    glVertex2f(-0.6,-2.8)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0.0,-2.8)
    glVertex2f(-0.6,-2.8)
    glVertex2f(-0.8,-3.0)
    glVertex2f(-0.2,-3.0)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(-0.2,-2.4)
    glVertex2f(-1.0,-2.4)
    glVertex2f(-1.0,-3.0)
    glVertex2f(-0.2,-3.0)
    glEnd()
    glPopMatrix()
    glEndList()
    
    
def MO_MA():
    info = letter_dict.get('ม')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE) 
    
    glBegin(GL_POLYGON) #เส้นตรงหน้า
    glVertex2f(0.6, 5.0)
    glVertex2f(0.0, 5.0)
    glVertex2f(0.0,0.0)
    glVertex2f(0.6,0.0)
    glEnd()
    
    glBegin(GL_POLYGON) #เส้นตรงหลัง
    glVertex2f(3.4, 5.0)
    glVertex2f(4.0, 5.0)
    glVertex2f(4.0,0.6)
    glVertex2f(3.4,0.0)
    glEnd()
    
    glBegin(GL_POLYGON) #เส้นล่าง
    glVertex2f(1.8, 0.0)
    glVertex2f(3.4, 0.0)
    glVertex2f(4.0,0.6)
    glVertex2f(1.2,0.6)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(1.8,0.0)
    glVertex2f(2.4,0.0)
    glVertex2f(0.6,1.8)
    glVertex2f(0.0,1.8)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(4.0,0.8)
    glVertex2f(3.4,0.8)
    glVertex2f(2.8,0.2)
    glVertex2f(3.4,0.2)
    glEnd()
    
    glEndList()
    
def LO_LING():
    info = letter_dict.get('ล')
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
    
    glEndList()
    
def HO_HIP():
    info = letter_dict.get('ห')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE) 
    
    glBegin(GL_POLYGON) #ตั้งซ้าย
    glVertex2f(0.6, 5.0) 
    glVertex2f(0.0, 5.0) 
    glVertex2f(0.0,0.0) 
    glVertex2f(0.6,0.0) 
    glEnd()
    
    glBegin(GL_POLYGON) #ตั้งบนขวา
    glVertex2f(3.4,5.0)
    glVertex2f(4.0,5.0)
    glVertex2f(4.0,4.2)
    glVertex2f(3.4,4.2)
    glEnd()
    
    glBegin(GL_POLYGON) #ตั้งล่างขวา
    glVertex2f(3.4,3.0)
    glVertex2f(4.0,3.0)
    glVertex2f(4.0,0.0)
    glVertex2f(3.4,0.0)
    glEnd()
        
    glBegin(GL_POLYGON) #นอนกลาง
    glVertex2f(0.6,3.9)
    glVertex2f(3.2,3.9)
    glVertex2f(3.2,3.3)
    glVertex2f(0.6,3.3)
    glEnd()

    glBegin(GL_POLYGON) #เฉียงบน
    glVertex2f(3.4,4.2)
    glVertex2f(4.0,4.2)
    glVertex2f(3.4,3.6)
    glVertex2f(2.8,3.6)
    glEnd()

    glBegin(GL_POLYGON) #เฉียงล่าง
    glVertex2f(3.4,3.0)
    glVertex2f(4.0,3.0)
    glVertex2f(3.4,3.6)
    glVertex2f(2.8,3.6)
    glEnd()

    glEndList()
    
def Sara_Uee():
    info = letter_dict.get('ื')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE) 
    
    glPushMatrix()
    glTranslatef(1,move+1,0)
    
    glBegin(GL_POLYGON) #นอนล่าง
    glVertex2f(0.0, 0.6) 
    glVertex2f(3.0, 0.6) 
    glVertex2f(3.0,0.0) 
    glVertex2f(0.0,0.0) 
    glEnd()
    
    glBegin(GL_POLYGON) #ตั้ง1
    glVertex2f(1.4,1.6)
    glVertex2f(1.4,0.0)
    glVertex2f(2.0,0.0)
    glVertex2f(2.0,1.6)
    glEnd()   
    
    glBegin(GL_POLYGON) #ตั้ง2
    glVertex2f(2.4,1.6)
    glVertex2f(3.0,1.6)
    glVertex2f(3.0,0.0)
    glVertex2f(2.4,0.0)
    glEnd()
    
    glPopMatrix()

    glEndList()
   
   