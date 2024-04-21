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
	'ฝ': [189, 4, 0],
	'ท': [183, 4, 0],
	'K': [75, 4, 0],
	'f': [102, 3, 0],
	'โ': [226, 2, 0],
	'ฆ': [166, 4, 0],
}

#position in letter dictionary
ASCII = 0
SIZE = 1
CLST = 2

def init_font():
    Furfar()
    TorTahan()
    KYai()
    FLek()
    SraO()
    rakang()

def Furfar():
    info = letter_dict.get('ฝ')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)
    glBegin(GL_POLYGON) 
    glVertex2f(1.2, 5.0)
    glVertex2f(1.2, 4.4)
    glVertex2f(0.0,4.4)
    glVertex2f(0.0,5.0)
    glEnd()

    # เส้นต่อหัว
    glBegin(GL_POLYGON)
    glVertex2f(0.6,5.0)
    glVertex2f(0.0,5.0)
    glVertex2f(0.0,0.6)
    glVertex2f(0.6,0.6)
    glEnd()

    # ดิ่งกลาง
    glBegin(GL_POLYGON)
    glVertex2f(1.7, 3.0)
    glVertex2f(2.3, 3.0)
    glVertex2f(2.3, 0.6)
    glVertex2f(1.7, 0.6)
    glEnd() 

    # นอน 1
    glBegin(GL_POLYGON)
    glVertex2f(2.3, 0.6)
    glVertex2f(0.0, 0.6)
    glVertex2f(0.6, 0.0)
    glVertex2f(1.7, 0.0)
    glEnd()

    # นอน 2
    glBegin(GL_POLYGON)
    glVertex2f(1.7, 0.6)
    glVertex2f(4.0, 0.6)
    glVertex2f(3.4, 0.0)
    glVertex2f(2.3, 0.0)
    glEnd()

    # หางยาว
    glBegin(GL_POLYGON)
    glVertex2f(4.0,8.0)
    glVertex2f(3.4,8.0)
    glVertex2f(3.4,0.6)
    glVertex2f(4.0,0.6)
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
    glVertex2f(2.2,0.8)
    glVertex2f(1.7,0.8)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(2.8,0.2)
    glVertex2f(3.4,0.2)
    glVertex2f(4.0,0.8)
    glVertex2f(3.4,0.8)
    glEnd()
    glEndList()
   
def TorTahan():
    info = letter_dict.get('ท')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)
    # หัว
    glBegin(GL_POLYGON)
    glVertex2f(0.0, 5.0)
    glVertex2f(0.0, 4.4)
    glVertex2f(1.0,4.4)
    glVertex2f(1.0,5.0)
    glEnd()
    # เส้นดิ่งซ้าย
    glBegin(GL_POLYGON)
    glVertex2f(1.2,5.0)
    glVertex2f(0.6, 5.0)
    glVertex2f(0.6,0.0)
    glVertex2f(1.2, 0.0)
    glEnd()
    # เส้นนอน
    glBegin(GL_POLYGON)
    glVertex2f(1.8,4.4)
    glVertex2f(2.0,5.0)
    glVertex2f(3.6,5.0)   
    glVertex2f(4.0,4.4) 
    glEnd()
    # ดส้นดิ่งขวา
    glBegin(GL_POLYGON)
    glVertex2f(4.0,0.0)
    glVertex2f(3.4,0.0)
    glVertex2f(3.4,4.4)
    glVertex2f(4.0,4.4)
    glEnd()

    #-----------------------------------

    glBegin(GL_POLYGON)
    glVertex2f(1.2, 3.6)
    glVertex2f(0.6, 3.6)
    glVertex2f(2.0, 5.0)
    glVertex2f(2.8, 5.0)
    glEnd() 

    glBegin(GL_POLYGON)
    glVertex2f(3.6, 4.0)
    glVertex2f(4.0, 4.0)
    glVertex2f(3.2, 5.0)
    glVertex2f(2.6, 5.0)
    glEnd()
    glEndList()

def KYai():
    info = letter_dict.get('K')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)
    # เส้นดิ่งซ้ายสุด
    glBegin(GL_POLYGON)
    glVertex2f(0.6,8.0)
    glVertex2f(0.0,8.0)
    glVertex2f(0.0,0.0)
    glVertex2f(0.6,0.0)
    glEnd()

    # เส้นนอนกลาง
    glBegin(GL_POLYGON)
    glVertex2f(3.0,4.0)
    glVertex2f(0.6,4.0)
    glVertex2f(0.6,3.4)
    glVertex2f(3.0,3.4)
    glEnd()

    # เส้นดิ่งขวาบน
    glBegin(GL_POLYGON)
    glVertex2f(4.0,8.0)
    glVertex2f(3.4,8.0)
    glVertex2f(3.4,4.5)
    glVertex2f(4.0,4.5)
    glEnd()

    # เส้นดิ่งขวาล่าง
    glBegin(GL_POLYGON)
    glVertex2f(3.8,0.0)
    glVertex2f(3.2,0.0)
    glVertex2f(3.2,2.8)
    glVertex2f(3.8,2.8)
    glEnd()

    # เฉียงบน
    glBegin(GL_POLYGON)
    glVertex2f(4.0,4.5)
    glVertex2f(3.4,4.7)
    glVertex2f(2.8,4.0)
    glVertex2f(3.0,3.4)
    glEnd()

    # เฉียงล่าง
    glBegin(GL_POLYGON)
    glVertex2f(3.8,2.8)
    glVertex2f(3.2,2.6)
    glVertex2f(2.8,3.4)
    glVertex2f(3.0,4.0)
    glEnd()
    glEndList()


def FLek():
    info = letter_dict.get('f')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)
    glPushMatrix()
    glTranslatef(-0.5,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(2.3,7.4)
    glVertex2f(1.7,7.4)
    glVertex2f(1.7,0.0)
    glVertex2f(2.3,0.0)
    glEnd()

    # 
    glBegin(GL_POLYGON)
    glVertex2f(3.5,4.4)
    glVertex2f(3.5,5.0)
    glVertex2f(0.5,5.0)
    glVertex2f(0.5,4.4)
    glEnd()

    # นอนบน
    glBegin(GL_POLYGON)
    glVertex2f(2.3,8.0)
    glVertex2f(2.3,7.4)
    glVertex2f(3.4,7.4)
    glVertex2f(3.4,8.0)
    glEnd()

    # เฉียง 2
    glBegin(GL_POLYGON)
    glVertex2f(2.3,8.0)
    glVertex2f(2.3,7.4)
    glVertex2f(1.7,7.4)
    glEnd()

    # เฉียง 1
    glBegin(GL_POLYGON)
    glVertex2f(2.7,7.4)
    glVertex2f(2.0,7.4)
    glVertex2f(2.0,6.8)
    glEnd()
    glPopMatrix()
    glEndList()
   
def SraO():
    info = letter_dict.get('โ')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)
    glBegin(GL_POLYGON)
    glVertex2f(1.6,0.0)
    glVertex2f(2.2,0.0)
    glVertex2f(2.2,0.6)
    glVertex2f(1.6,0.6)
    glEnd()
    # ดิ่งยาว
    glBegin(GL_POLYGON)
    glVertex2f(1.0,6.2)
    glVertex2f(1.0,0.0)
    glVertex2f(1.6,0.0)
    glVertex2f(1.6,6.2)
    glEnd()
    # นอน 1 
    glBegin(GL_POLYGON)
    glVertex2f(0.0,7.2)
    glVertex2f(0.0,6.6)
    glVertex2f(1.6,6.0)
    glVertex2f(1.6,6.6)
    glEnd()
    # ดิ่งสั้น
    glBegin(GL_POLYGON)
    glVertex2f(0.6,8.4)
    glVertex2f(0.0,8.4)
    glVertex2f(0.0,6.8)
    glVertex2f(0.6,6.8)
    glEnd()
    # เฉียง
    glBegin(GL_POLYGON)
    glVertex2f(0.0,8.4)
    glVertex2f(0.6,9.0)
    glVertex2f(0.6,8.4)
    glEnd()
    # นอน 2
    glBegin(GL_POLYGON)
    glVertex2f(0.6,8.4)
    glVertex2f(0.6,9.0)
    glVertex2f(3.0,9.0)
    glVertex2f(3.0,8.4)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0.0,8.2)
    glVertex2f(0.6,8.8)
    glVertex2f(1.2,8.8)
    glVertex2f(0.6,8.2)
    glEnd()

    glEndList()
   
def rakang():
    info = letter_dict.get('ฆ')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)
    glPushMatrix()

    glBegin(GL_POLYGON)
    glVertex2f(0.0,5.0)
    glVertex2f(0.4,5.0)
    glVertex2f(0.4,4.4)
    glVertex2f(0.0,4.4)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(1.0,5.0)
    glVertex2f(1.6,5.0)
    glVertex2f(1.6,4.4)
    glVertex2f(1.0,4.4)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0.0,4.4)
    glVertex2f(1.4,4.4)
    glVertex2f(1.0,4.0)
    glVertex2f(0.4,4.0)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(1.0,4.4)
    glVertex2f(0.0,2.8)
    glVertex2f(0.6,2.8)
    glVertex2f(1.6,4.4)
    glEnd()

    glBegin(GL_POLYGON) #เส้นตรงหน้า
    glVertex2f(0.6, 3.4)
    glVertex2f(0.0, 2.8)
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
    glPopMatrix()
    glEndList()