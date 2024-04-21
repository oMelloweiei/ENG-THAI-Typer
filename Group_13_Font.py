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
	'n': [110, 4, 0],
	'S': [83, 4, 0],
	'ถ': [182, 4, 0],
	'ฑ': [177, 4, 0],
	'ั': [209, 3.4, 0],
	'์': [236, 3, 0],
}

ASCII = 0
SIZE = 1
CLST = 2

def init_font(): 
    #เรียกฟังก์ชันเพื่อวาดไว้รอเรียกคอลลิสอีกที
    Nlek() # n ตัวพิมพ์เล็ก
    Syai() # S ตัวพิมพ์ใหญ่
    MAI_HAN_AKAT() #  ั ไม้หันอากาศ
    Thanthakhat() # ์ ทัณฑฆาต
    Thor_Thung() # ถ.ถุง
    Tor_montho() # ฑ.มณโฑ

def Nlek(): # n ตัวพิมพ์เล็ก
    info = letter_dict.get('n')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)

    glPushMatrix()
    glPushMatrix()
    glBegin(GL_POLYGON)
    glVertex2f(4.0,0.0)
    glVertex2f(3.4,0.0)
    glVertex2f(3.4,5)
    glVertex2f(4.0,4.4)
    glEnd()
    
    #บน
    glBegin(GL_POLYGON)
    glVertex2f(3.4,5) 
    glVertex2f(4.0,4.4) 
    glVertex2f(0.0,4.4) 
    glVertex2f(0.6,5) 
    glEnd()
    
    #ซ้าย
    glBegin(GL_POLYGON)
    glVertex2f(0.0,4.4)
    glVertex2f(0.6,5.0)
    glVertex2f(0.6,0.0)
    glVertex2f(0.0,0.0)
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

    glPopMatrix()          
    glEndList()

def Syai(): # S ตัวพิมพ์ใหญ่
    info = letter_dict.get('S')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)

    glPushMatrix()
    #ขีดซ้ายล่าง
    glBegin(GL_POLYGON)
    glVertex2f(0.0,1.4)
    glVertex2f(0.6,1.4)
    glVertex2f(0.6,0.0)
    glVertex2f(0.0,0.6)
    glEnd()

    #ขีดล่าง
    glBegin(GL_POLYGON)
    glVertex2f(0.0,0.6)
    glVertex2f(0.6,0.0)
    glVertex2f(3.4,0.0)
    glVertex2f(4.0,0.6)
    glEnd()

    #ขีดขวา
    glBegin(GL_POLYGON)
    glVertex2f(3.4,0.0)
    glVertex2f(4.0,0.6)
    glVertex2f(4.0,3.7)
    glVertex2f(3.4,4.3)
    glEnd()

    #ขีดกลาง
    glBegin(GL_POLYGON)
    glVertex2f(0.6,3.7) 
    glVertex2f(0.0,4.3) 
    glVertex2f(3.4,4.3) 
    glVertex2f(4.0,3.7) 
    glEnd()

    #ขีดซ้าย
    glBegin(GL_POLYGON)
    glVertex2f(0.6,8.0)
    glVertex2f(0.0,7.4)
    glVertex2f(0.0,4.3)
    glVertex2f(0.6,3.7)
    glEnd()

    #ขีดบน
    glBegin(GL_POLYGON)
    glVertex2f(0.0,7.4)
    glVertex2f(0.6,8.0)
    glVertex2f(3.4,8.0)
    glVertex2f(4.0,7.4)
    glEnd()
    
    #ขีดขวาบน
    glBegin(GL_POLYGON)
    glVertex2f(3.4,6.4)
    glVertex2f(4.0,6.4)
    glVertex2f(4.0,7.4)
    glVertex2f(3.4,8.0)
    glEnd()

    glPopMatrix()  
    glEndList()

def MAI_HAN_AKAT(): #  ั ไม้หันอากาศ
    info = letter_dict.get('ั')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)

    glPushMatrix()
    glTranslatef(0.5, 6, 0) # ปรับตำแหน่งให้ตัวอักษรอยู่ด้านบน
    #glTranslatef(0, move + 0.5, 0) 

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
    glEndList()

def Thor_Thung(): # ถ.ถุง
    info = letter_dict.get('ถ')
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

def Thanthakhat(): # ์ ทัณฑฆาต
    info = letter_dict.get('์')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)

    glPushMatrix()
    glTranslatef(3,6, 0) # ปรับตำแหน่งให้ตัวอักษรอยู่ด้านบน

    glBegin(GL_POLYGON)
    glVertex2f(0.6,0.0)
    glVertex2f(1.0,0.0)
    glVertex2f(1.0,0.4)
    glVertex2f(0.6,0.4)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0.0,0.0)
    glVertex2f(0.6,0.0)
    glVertex2f(0.6,1.6)
    glVertex2f(0.0,1.0)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0.0,1.0)
    glVertex2f(0.6,1.6)
    glVertex2f(2.8,1.6)
    glVertex2f(2.2,1.0)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(2.8,1.6)
    glVertex2f(2.2,1.6)
    glVertex2f(2.8,2.2)
    glVertex2f(3.4,2.2)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(2.8,2.2)
    glVertex2f(3.4,2.2)
    glVertex2f(3.4,3.0)
    glVertex2f(2.8,3.0)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0.6,1.4)
    glVertex2f(1.2,1.4)
    glVertex2f(0.6,0.8)
    glVertex2f(0.0,0.8)
    glEnd()

    glPopMatrix()
    glEndList()

def Tor_montho(): # ฑ.มณโฑ 
    info = letter_dict.get('ฑ')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)

    glPushMatrix()
    # เริ่มต้น
    glBegin(GL_POLYGON)
    glVertex2f(3.4,0.0)
    glVertex2f(4.0,0.0)
    glVertex2f(4.0,5.0)
    glVertex2f(3.4,5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0.0,0.0)
    glVertex2f(0.6,0.0)
    glVertex2f(0.6,3.7)
    glVertex2f(0.0,3.3)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(3.4,5.0)
    glVertex2f(3.4,4.4)
    glVertex2f(1.8,4.4)
    glVertex2f(2.4,5.0)
    glEnd()
    # glColor3f(0,1,0)
    glBegin(GL_POLYGON)
    glVertex2f(0.0,3.3)
    glVertex2f(0.6,3.3)
    glVertex2f(2.8,5.0)
    glVertex2f(2.2,5.0)
    glEnd()

    # glColor3f(1,0,0)

    glBegin(GL_POLYGON)
    glVertex2f(0.0,5.0)
    glVertex2f(0.4,5.0)
    glVertex2f(0.4,4.4)
    glVertex2f(0.0,4.4)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(1.0,5.0)
    glVertex2f(1.4,5.0)
    glVertex2f(1.4,4.4)
    glVertex2f(1.0,4.4)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0.0,4.4)
    glVertex2f(1.4,4.4)
    glVertex2f(1.0,4.0)
    glVertex2f(0.4,4.0)
    glEnd()

    glPopMatrix()
    glEndList()