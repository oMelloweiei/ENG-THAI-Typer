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

mini_height = 5
mini_width = 4
big_height = 8
ex_height_b = -3

letter_dict = {
	'm': [109, 5, 0],
	'R': [82, 4, 0],
	'อ': [105, 4, 0],
	'ภ': [192, 4.6, 0],
	'ไ': [228, 2, 0],
	'๊': [234, 3.4, 0],
}

ASCII = 0
SIZE = 1
CLST = 2

def init_font():
    mlek() # m ตัวพิมพ์เล็ก
    Ryai() # R ตัวพิมพ์ใหญ่
    aor()  # อ.อ่าง
    porsum() # ตัว ภ
    aimaimalai() # สระไอ 
    maitri() #  ไม้ตรี
     

def mlek(): # m ตัวพิมพ์เล็ก
    info = letter_dict.get('m')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)
    glPushMatrix()
    
    glBegin(GL_POLYGON)
    glVertex2f(5.0,0.0)
    glVertex2f(4.4,0.0)
    glVertex2f(4.4,5)
    glVertex2f(5.0,4.4)
    glEnd()
    
    #บน
    glBegin(GL_POLYGON)
    glVertex2f(2.2,5) 
    glVertex2f(2.8,4.4) 
    glVertex2f(0.0,4.4) 
    glVertex2f(0.6,5) 
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(2.8,5) 
    glVertex2f(2.2,4.4) 
    glVertex2f(5.0,4.4) 
    glVertex2f(4.4,5) 
    glEnd()
    
    #ซ้าย
    glBegin(GL_POLYGON)
    glVertex2f(0.0,4.4)
    glVertex2f(0.6,5.0)
    glVertex2f(0.6,0.0)
    glVertex2f(0.0,0.0)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(2.2,4.4)
    glVertex2f(2.8,5.0)
    glVertex2f(2.8,0.0)
    glVertex2f(2.2,0.0)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(2.2,5.0)
    glVertex2f(2.8,4.4)
    glVertex2f(2.8,0.0)
    glVertex2f(2.2,0.0)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(2.2,4.2)
    glVertex2f(2.8,4.2)
    glVertex2f(2.2,4.8)
    glVertex2f(1.6,4.8)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0.0,4.2)
    glVertex2f(0.6,4.2)
    glVertex2f(1.2,4.8)
    glVertex2f(0.6,4.8)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(2.2,4.2)
    glVertex2f(2.8,4.2)
    glVertex2f(3.4,4.8)
    glVertex2f(2.8,4.8)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(5.0,4.2)
    glVertex2f(4.4,4.2)
    glVertex2f(3.8,4.8)
    glVertex2f(4.4,4.8)
    glEnd()

    glPopMatrix           
    glEndList()

def Ryai(): # R ตัวพิมพ์ใหญ่
    info = letter_dict.get('R')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)

    glPushMatrix()
    glBegin(GL_POLYGON)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.6,0.0)
    glVertex2f(0.6,8.0)
    glVertex2f(0.0,8.0)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(0.0,7.4)
    glVertex2f(0.0,8.0)
    glVertex2f(3.4,8.0)
    glVertex2f(4.0,7.4)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(4.0,7.4)
    glVertex2f(3.4,7.4)
    glVertex2f(3.4,4.0)
    glVertex2f(4.0,4.4)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(3.4,4.0)
    glVertex2f(3.4,3.4)
    glVertex2f(0.6,3.4)
    glVertex2f(0.6,4.0)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(3.4,3.4)
    glVertex2f(4.0,2.8)
    glVertex2f(4.0,0.0)
    glVertex2f(3.4,0.0)
    glEnd()

    glPopMatrix()  
    glEndList()

def maitri(): #   ไม้ตรี
    info = letter_dict.get('๊')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)

    glPushMatrix()
    glTranslatef(1.2, 6, 0) # ปรับตำแหน่งให้ตัวอักษรอยู่ด้านบน

    glBegin(GL_POLYGON)
    glVertex2f(0.0,0.0)
    glVertex2f(0.0,0.6)
    glVertex2f(1.0,0.6)
    glVertex2f(1.0,0.0)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(0.0,0.6)
    glVertex2f(0.6,0.6)
    glVertex2f(0.6,2.6)
    glVertex2f(0.0,2.0)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0.6,2.0)
    glVertex2f(0.6,2.6)
    glVertex2f(0.8,2.6)
    glVertex2f(1.2,2.0)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(1.8,2.0)
    glVertex2f(1.8,2.6)
    glVertex2f(1.6,2.6)
    glVertex2f(1.2,2.0)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(1.8,0.0)
    glVertex2f(2.4,0.0)
    glVertex2f(2.4,2.0)
    glVertex2f(1.8,2.6)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(2.8,0.9)
    glVertex2f(3.4,0.9)
    glVertex2f(3.4,3.0)
    glVertex2f(2.8,3.0)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(1.8,0.0)
    glVertex2f(2.4,0.0)
    glVertex2f(3.4,0.9)
    glVertex2f(2.8,0.9)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(1.0,2.0)
    glVertex2f(1.4,2.0)
    glVertex2f(1.4,1.4)
    glVertex2f(1.0,1.4)
    glEnd()

    # glColor3f(1,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(1.4,1.9)
    glVertex2f(1.2,1.9)
    glVertex2f(1.4,2.1)
    glVertex2f(1.6,2.1)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0.6,1.9)
    glVertex2f(0.4,1.9)
    glVertex2f(0.6,2.1)
    glVertex2f(0.8,2.1)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(1.0,2.1)
    glVertex2f(0.8,2.1)
    glVertex2f(1.0,1.9)
    glVertex2f(1.2,1.9)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(1.8,2.1)
    glVertex2f(1.6,2.1)
    glVertex2f(1.8,1.9)
    glVertex2f(2.0,1.9)
    glEnd()

    glPopMatrix()
    glEndList()


def aor(): # อ.อ่าง
    info = letter_dict.get('อ')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)

    glPushMatrix()

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

    glPopMatrix()
    glEndList()

def porsum(): # ตัว ภ
    info = letter_dict.get('ภ')
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
    glVertex2f(4,0)
    glVertex2f(3.4,0)
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

def aimaimalai(): # สระไอ 
    info = letter_dict.get('ไ')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)

    glPushMatrix()
    
    glBegin(GL_POLYGON)
    glVertex2f(1.6,0.0)
    glVertex2f(1.6,0.6)
    glVertex2f(2.2,0.6)
    glVertex2f(2.2,0.0)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(1.6,0.0)
    glVertex2f(1.0,0.0)
    glVertex2f(1.0,6.0)
    glVertex2f(1.6,6.0)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(1.6,6.0)
    glVertex2f(1.0,6.0)
    glVertex2f(2.4,7.8)
    glVertex2f(3.0,7.8)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(3.0,7.8)
    glVertex2f(2.4,7.8)
    glVertex2f(2.4,9.0)
    glVertex2f(3.0,9.0)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(2.4,8.4)
    glVertex2f(2.4,9.0)
    glVertex2f(1.8,8.4)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(3.0,9.0)
    glVertex2f(2.4,9.0)
    glVertex2f(1.0,7.6)
    glVertex2f(1.6,7.6)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(1.0,7.6)
    glVertex2f(1.6,7.6)
    glVertex2f(0.6,9.0)
    glVertex2f(0.0,9.0)
    glEnd()
    
    glPopMatrix()
    glEndList()
