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
	'ซ': [171, 3, 0],
	'ฒ': [178, 6.6, 0],
	'า': [210, 3, 0],
	'้': [233, 1.8, 0],
	'M': [77, 4, 0],
	'h': [104, 4, 0],
}

#position in letter dictionary
ASCII = 0
SIZE = 1
CLST = 2

def init_font():
    sorso()
    thoputhal()
    saraR()
    M()
    h()
    maitho()

def sorso():
    info = letter_dict.get('ซ')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)
    
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

    #3
    glBegin(GL_POLYGON)
    glVertex2f(1.4,4.4)
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
    glEndList()
  
   
   
def thoputhal():
    info = letter_dict.get('ฒ')
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


def saraR():
    info = letter_dict.get('า')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)
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
    glEndList()
   


def h():
    info = letter_dict.get('h')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)
    glBegin(GL_POLYGON)
    glVertex2f(0,8)
    glVertex2f(0.6,8)
    glVertex2f(0.6,0)
    glVertex2f(0,0)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0,5)
    glVertex2f(0,4.4)
    glVertex2f(4,4.4)
    glVertex2f(3.4,5)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(3.4,5)
    glVertex2f(4,4.4)
    glVertex2f(4,0)
    glVertex2f(3.4,0)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(4.0,4.2)
    glVertex2f(3.4,4.2)
    glVertex2f(2.8,4.8)
    glVertex2f(3.4,4.8)
    glEnd()
    glEndList()
   
   
   
def M():
    info = letter_dict.get('M')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)
    glBegin(GL_POLYGON)
    glVertex2f(0,0)
    glVertex2f(0.6,0)
    glVertex2f(0.6,8)
    glVertex2f(0,8)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0,8)
    glVertex2f(0.6,8)
    glVertex2f(2,5)
    glVertex2f(2,4)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(2,5)
    glVertex2f(2,4)
    glVertex2f(4,8)
    glVertex2f(3.4,8)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(3.4,8)
    glVertex2f(4,8)
    glVertex2f(4,0)
    glVertex2f(3.4,0)
    glEnd()
    glEndList()

def maitho():
    info = letter_dict.get('้')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)
    glPushMatrix()
    glTranslatef(2.2,6,0)

    glBegin(GL_POLYGON)
    glVertex2f(0.4,0.0)
    glVertex2f(0.8,0.0)
    glVertex2f(0.8,1.4)
    glVertex2f(0.4,1.4)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0.0,1.4)
    glVertex2f(0.4,1.4)
    glVertex2f(0.4,0.8)
    glVertex2f(0.0,0.8)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0.4,0.0)
    glVertex2f(0.8,0.0)
    glVertex2f(1.8,0.6)
    glVertex2f(1.2,0.6)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(1.8,0.6)
    glVertex2f(1.2,0.6)
    glVertex2f(1.2,1.4)
    glVertex2f(1.8,1.4)
    glEnd()

    glPopMatrix()
    glEndList()