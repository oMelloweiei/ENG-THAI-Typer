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
	'p': [112, 4, 0],
	'U': [85, 4, 0],
	'ฌ': [172, 6.6, 0],
	'ข': [162, 3, 0],
	'เ': [224, 1.4, 0],
	'่': [232, 0.6, 0]
}

ASCII = 0
SIZE = 1
CLST = 2

def init_font():
    create_a_list()
    create_p_list()
    create_U_list()
    create_ข_list()
    create_ฌ_list()
    create_เ_list()

def create_p_list():
    info = letter_dict.get('p')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE) 
    glBegin(GL_POLYGON)
    glVertex2f(0,4.4)
    glVertex2f(0.6, 5)
    glVertex2f(0.6,-3)
    glVertex2f(0,-3)
    glEnd()
    
    #2
    glBegin(GL_POLYGON)
    glVertex2f(0,4.4)
    glVertex2f(0.6, 5)
    glVertex2f(3.6,5)
    glVertex2f(4,4.4)
    glEnd()
    
    #3
    glBegin(GL_POLYGON)
    glVertex2f(3.4,5)
    glVertex2f(4,4.4)
    glVertex2f(4,0.6)
    glVertex2f(3.4,0)
    glEnd()
    
    #4
    glBegin(GL_POLYGON)
    glVertex2f(4,0.6)
    glVertex2f(3.4,0)
    glVertex2f(0,0)
    glVertex2f(0,0.6)
    glEnd()
    
    #ตัดล่าง
    glBegin(GL_POLYGON)
    glVertex2f(0,4.4)
    glVertex2f(0.6, 5)
    glVertex2f(0.8,4.4)
    glVertex2f(0.6,4.2)
    glEnd()
    

    #ตัดบน
    glBegin(GL_POLYGON)
    glVertex2f(3.6,5)
    glVertex2f(4,4.4)
    glVertex2f(3.6,3.9)
    glVertex2f(3.2,4.4)
    glEnd()
    
    #ตัดบนซ้าย
    glBegin(GL_POLYGON)
    glVertex2f(4,0.6)
    glVertex2f(3.4,0)
    glVertex2f(3.2,0.6)
    glVertex2f(3.4,0.8)
    glEnd()
    glEndList()


def create_U_list():
    info = letter_dict.get('U')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE) 
    glBegin(GL_POLYGON)
    glVertex2f(0, 8)
    glVertex2f(0.6, 8)
    glVertex2f(0.6,0)
    glVertex2f(0,0.6)
    glEnd()
    
    #2
    glBegin(GL_POLYGON)
    glVertex2f(0.6,0)
    glVertex2f(0,0.6)
    glVertex2f(4,0.6)
    glVertex2f(3.4,0)
    glEnd()
    
    #3
    glBegin(GL_POLYGON)
    glVertex2f(3.4, 8)
    glVertex2f(4, 8)
    glVertex2f(4,0.6)
    glVertex2f(3.4,0)
    glEnd()
    
    # ซ้ายล่างตัด   
    glBegin(GL_POLYGON)
    glVertex2f(0.6,0)
    glVertex2f(0,0.6)
    glVertex2f(0.8,0.6)
    glVertex2f(0.6,0.8)
    glEnd()
    
    # ขวาล่างตัด   
    glBegin(GL_POLYGON)
    glVertex2f(4,0.6)
    glVertex2f(3.4,0)
    glVertex2f(3.2,0.6)
    glVertex2f(3.4,0.8)
    glEnd()
    glEndList()

def create_ข_list():
    info = letter_dict.get('ข')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE) 
    #1

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
    
    #6
    glBegin(GL_POLYGON)
    glVertex2f(2.4, 5)
    glVertex2f(3, 5)
    glVertex2f(3,0.6)
    glVertex2f(2.4,0)
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
    glEndList()

def create_ฌ_list():
    info = letter_dict.get('ฌ')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE) 


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

    glBegin(GL_POLYGON)
    glVertex2f(6.0,0.0)
    glVertex2f(6.0,5.0)
    glVertex2f(6.6,5.0)
    glVertex2f(6.6,0.6)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(6.6,0.6)
    glVertex2f(6.0,0.0)
    glVertex2f(4.8,0.0)
    glVertex2f(4.2,0.6)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(4.2,0.6)
    glVertex2f(4.8,0.6)
    glVertex2f(4.0,1.4)
    glVertex2f(3.4,1.4)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(6.6,0.8)
    glVertex2f(6.0,0.8)
    glVertex2f(5.4,0.2)
    glVertex2f(6.0,0.2)
    glEnd()
    glEndList()

def create_เ_list():
    info = letter_dict.get('เ')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE) 
    #1
    glBegin(GL_POLYGON)
    glVertex2f(0, 0.6)
    glVertex2f(0.6, 0)
    glVertex2f(0.6,5)
    glVertex2f(0,5)
    glEnd()
    
    #2
    glBegin(GL_POLYGON)
    glVertex2f(0, 0.6)
    glVertex2f(0.6, 0)
    glVertex2f(1.4,0)
    glVertex2f(1.4,0.6)
    glEnd()
    
    # ซ้ายล่างตัด   
    glBegin(GL_POLYGON)
    glVertex2f(0, 0.6)
    glVertex2f(0.6, 0)
    glVertex2f(0.8,0.6)
    glVertex2f(0.6,0.8)
    glEnd()
    glEndList()

def create_a_list():
    info = letter_dict.get('่')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE) 

    glPushMatrix()
    glTranslatef(3.4,6,0)
    glBegin(GL_POLYGON)
    glVertex2f(0, 1.4)
    glVertex2f(0.6, 1.4)
    glVertex2f(0.6,0)
    glVertex2f(0,0)
    glEnd()

    glPopMatrix()

    glEndList()