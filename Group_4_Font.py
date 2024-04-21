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

move = 6

letter_dict = {
	'w': [119, 5, 0],
	'b': [98, 4, 0],
	'G': [71, 4, 0],
	'ำ': [211, 3, 0],
	'พ': [190, 4, 0],
	'ป': [187, 4, 0]
}

ASCII = 0
SIZE = 1
CLST = 2


def init_font():
    Small_Latter_w()
    Small_Latter_b()
    Big_Latter_G()
    Thai_Sara_Am()
    Thai_Po_Pla()
    Thai_Pho_Phan()
    
def Thai_Pho_Phan():
    info = letter_dict.get('พ')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)
    glPushMatrix()

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

    glPopMatrix()
    glEndList()
    
    
def Thai_Po_Pla():
    info = letter_dict.get('ป')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)
    glPushMatrix()
    
    glBegin(GL_POLYGON)
    glVertex2f(3.4, 8)
    glVertex2f(4.0, 8)
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
    
    glPopMatrix()
    glEndList()
    
    
def Thai_Sara_Am():
    info = letter_dict.get('ำ')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)
    glPushMatrix()

    glBegin(GL_POLYGON)
    glVertex2f(0.0,6.3)
    glVertex2f(0.0,6.9)
    glVertex2f(0.3,7.2)
    glVertex2f(0.3,6.0)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0.9,6.0)
    glVertex2f(0.9,7.2)
    glVertex2f(1.2,6.9)
    glVertex2f(1.2,6.3)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(0.3,7.2)
    glVertex2f(0.0,6.9)
    glVertex2f(1.2,6.9)
    glVertex2f(0.9,7.2)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0.3,6.0)
    glVertex2f(0.0,6.3)
    glVertex2f(1.2,6.3)
    glVertex2f(0.9,6.0)
    glEnd()

    # glColor3f(1,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(0.0,6.8)
    glVertex2f(0.3,6.8)
    glVertex2f(0.6,7.1)
    glVertex2f(0.3,7.1)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0.0,6.4)
    glVertex2f(0.3,6.4)
    glVertex2f(0.6,6.1)
    glVertex2f(0.3,6.1)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0.9,6.1)
    glVertex2f(0.6,6.1)
    glVertex2f(0.9,6.4)
    glVertex2f(1.2,6.4)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0.9,7.1)
    glVertex2f(0.6,7.1)
    glVertex2f(0.9,6.8)
    glVertex2f(1.2,6.8)
    glEnd()

    glPushMatrix()
    glTranslatef(1.6,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(2.4, 5.0)
    glVertex2f(3.0, 4.4)
    glVertex2f(3.0, 0.0)
    glVertex2f(2.4, 0.0)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(3.0,4.4)
    glVertex2f(2.4,5.0)
    glVertex2f(0.6,5.0)
    glVertex2f(0.0,4.4)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0.0,4.4)
    glVertex2f(0.6,4.4)
    glVertex2f(0.6,3.8)
    glVertex2f(0.0,3.8)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0.6,4.8)
    glVertex2f(1.2,4.8)
    glVertex2f(0.6,4.2)
    glVertex2f(0.0,4.2)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(2.4,4.8)
    glVertex2f(1.8,4.8)
    glVertex2f(2.4,4.2)
    glVertex2f(3.0,4.2)
    glEnd()
    glPopMatrix()
    glEndList()
    
def Small_Latter_w():
    info = letter_dict.get('w')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)
    glPushMatrix()
    
    #www 1
    glBegin(GL_POLYGON)
    glVertex2f(0,5)
    glVertex2f(0.6,5)
    glVertex2f(0.6,1.2)
    glVertex2f(0,2)
    glEnd()

    #www 2
    glBegin(GL_POLYGON)
    glVertex2f(2.2,5)
    glVertex2f(2.8,5)
    glVertex2f(2.8,1.6)
    glVertex2f(2.2,1.6)
    glEnd()
    
    #www 3
    glBegin(GL_POLYGON)
    glVertex2f(4.4,5)
    glVertex2f(5,5)
    glVertex2f(5,2)
    glVertex2f(4.4,1.2)
    glEnd()

    #www 4
    glBegin(GL_POLYGON)
    glVertex2f(0,2)
    glVertex2f(1.2,0.6)
    glVertex2f(1,0)
    glVertex2f(0,1.2)
    glEnd()

    #www 5
    glBegin(GL_POLYGON)
    glVertex2f(1.2,0.6)
    glVertex2f(1.4,0.6)
    glVertex2f(1.6,0)
    glVertex2f(1,0)
    glEnd()
    
    #www 6
    glBegin(GL_POLYGON)
    glVertex2f(1.4,0.6)
    glVertex2f(1.6,0)
    glVertex2f(2.5,1.2)
    glVertex2f(2.5,2)
    glEnd()
    
    #www 7
    glBegin(GL_POLYGON)
    glVertex2f(2.5,2)
    glVertex2f(3.6,0.6)
    glVertex2f(3.4,0)
    glVertex2f(2.5,1.2)
    glEnd()

    #www 8
    glBegin(GL_POLYGON)
    glVertex2f(3.6,0.6)
    glVertex2f(3.8,0.6)
    glVertex2f(4,0)
    glVertex2f(3.4,0)
    glEnd()
    
    #www 9
    glBegin(GL_POLYGON)
    glVertex2f(3.8,0.6)
    glVertex2f(4,0)
    glVertex2f(5,1.2)
    glVertex2f(5,2)
    glEnd()
    
    glPopMatrix()
    glEndList()
    
def Small_Latter_b():
    info = letter_dict.get('b')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)
    glPushMatrix()
    
    #เส้น 1
    glBegin(GL_POLYGON)
    glVertex2f(0,8)
    glVertex2f(0.6,8)
    glVertex2f(0.6,0.8)
    glVertex2f(0,1.4)
    glEnd()

    #เส้น 2
    glBegin(GL_POLYGON)
    glVertex2f(3.4,4)
    glVertex2f(4,3.4)
    glVertex2f(4,1.4)
    glVertex2f(3.4,0.8)
    glEnd()

    #เส้น 3
    glBegin(GL_POLYGON)
    glVertex2f(0.6,5.0)
    glVertex2f(3.0,5.0)
    glVertex2f(3.6,4.4)
    glVertex2f(0.6,4.4)
    glEnd()

    #เส้น 4
    glBegin(GL_POLYGON)
    glVertex2f(0.8,0.6)
    glVertex2f(3.2,0.6)
    glVertex2f(2.6,0)
    glVertex2f(1.6,0)
    glEnd()

    #เส้น 5
    glBegin(GL_POLYGON)
    glVertex2f(2.6,4.8)
    glVertex2f(3.2,4.8)
    glVertex2f(4,4)
    glVertex2f(4,3.4)
    glEnd()

    #เส้น 6
    glBegin(GL_POLYGON)
    glVertex2f(0,1.4)
    glVertex2f(1.6,0)
    glVertex2f(0.8,0)
    glVertex2f(0,0.8)
    glEnd()

    #เส้น 7
    glBegin(GL_POLYGON)
    glVertex2f(4,1.4)
    glVertex2f(4,0.8)
    glVertex2f(3.2,0)
    glVertex2f(2.6,0)
    glEnd()
    
    glPopMatrix()
    glEndList()
    
def Big_Latter_G():
    info = letter_dict.get('G')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)
    glPushMatrix()
    
    glBegin(GL_POLYGON) #ซ้าย
    glVertex2f(0.6, 7)
    glVertex2f(0, 6.2)
    glVertex2f(0, 1.6)
    glVertex2f(0.6, 1)
    glEnd()

    glBegin(GL_POLYGON) #ล่าง
    glVertex2f(1, 0.6)
    glVertex2f(3, 0.6)
    glVertex2f(2.4, 0)
    glVertex2f(1.6, 0)
    glEnd()

    glBegin(GL_POLYGON) #ขวาล่าง
    glVertex2f(4, 4.4)
    glVertex2f(3.4, 4.4)
    glVertex2f(3.4, 1)
    glVertex2f(4, 1.6)
    glEnd()

    glBegin(GL_POLYGON) #บน
    glVertex2f(1.6, 8)
    glVertex2f(2.4, 8)
    glVertex2f(3, 7.4)
    glVertex2f(1, 7.4)
    glEnd()

    glBegin(GL_POLYGON) #ขวาบน
    glVertex2f(4, 6.4)
    glVertex2f(3.4, 7)
    glVertex2f(3.4, 5.2)
    glVertex2f(4, 5.2)
    glEnd()

    glBegin(GL_POLYGON) #ขีดกลาง
    glVertex2f(2, 4.4)
    glVertex2f(3.4, 4.4)
    glVertex2f(3.4, 3.8)
    glVertex2f(2, 3.8)
    glEnd()
   
   # เส้นมุมเฉียง
   # glColor3f(0,0,1)     
    glBegin(GL_POLYGON) # ซ้ายบน
    glVertex2f(1.6, 8)
    glVertex2f(0.8, 8)
    glVertex2f(0, 7.2)
    glVertex2f(0, 6.2)
    glEnd()

    glBegin(GL_POLYGON) # ซ้ายล่าง
    glVertex2f(0, 1.6)
    glVertex2f(0, 0.8)
    glVertex2f(0.8, 0)
    glVertex2f(1.6, 0)
    glEnd()

    glBegin(GL_POLYGON) # ขวาบน
    glVertex2f(3.2, 8)
    glVertex2f(2.4, 8)
    glVertex2f(4, 6.4)
    glVertex2f(4, 7.2)
    glEnd()

    glBegin(GL_POLYGON) # ขวาล่าง
    glVertex2f(4, 1.6)
    glVertex2f(2.4, 0)
    glVertex2f(3.2, 0)
    glVertex2f(4, 0.8)
    glEnd()

    glPopMatrix()
    glEndList()
   