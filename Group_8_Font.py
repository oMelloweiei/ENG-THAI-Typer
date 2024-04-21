#!/usr/bin/python

#Made by Group8 

# Kanyamon Rungtanasombut  64080500203
# Jadesalit Suriyanimitsuk 64080500207
# Chayasa Taweekun         64080500209
# Namnueng Intason         64080500223
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
	's': [115, 4, 0],
	'X': [88, 4, 0],
	'C': [67, 4, 0],
	'ธ': [184, 4, 0],
	'ฯ': [207, 3, 0],
	'ษ': [201, 5, 0]
}

ASCII = 0
SIZE = 1
CLST = 2

def init_font():
    s_Letter()          #203_209
    X_letter()          #203_209
    PAIYANNOI()         #203_209
    tong()              #207
    C_letter()          #223
    leusee()            #223

    
def s_Letter():
    info = letter_dict.get('s')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)
    
    glBegin(GL_POLYGON)
    glVertex2f(4.0, 2.2)
    glVertex2f(3.4, 2.8)
    glVertex2f(3.4, 0.0)
    glVertex2f(4.0, 0.6)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(0.0, 2.8)
    glVertex2f(0.6, 2.2)
    glVertex2f(0.6, 5.0)
    glVertex2f(0.0, 4.4)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0.6,5.0)
    glVertex2f(0.0,4.4)
    glVertex2f(4.0,4.4)
    glVertex2f(3.4,5.0)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(0.6,0.0)
    glVertex2f(0.0,0.6)
    glVertex2f(4.0,0.6)
    glVertex2f(3.4,0.0)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(0.6,2.2)
    glVertex2f(0.0,2.8)
    glVertex2f(3.4,2.8)
    glVertex2f(4.0,2.2)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(0.6,2.2)
    glVertex2f(0.0,2.8)
    glVertex2f(3.4,2.8)
    glVertex2f(4.0,2.2)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(0.0,1.0)
    glVertex2f(0.6,1.0)
    glVertex2f(0.6,0.0)
    glVertex2f(0.0,0.6)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(4.0,4.4)
    glVertex2f(3.4,5.0)
    glVertex2f(3.4,4.0)
    glVertex2f(4.0,4.0)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(0.0,0.8)
    glVertex2f(0.6,0.8)
    glVertex2f(1.2,0.2)
    glVertex2f(0.6,0.2)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(4.0,0.8)
    glVertex2f(3.4,0.8)
    glVertex2f(2.8,0.2)
    glVertex2f(3.4,0.2)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(0.0,3.0)
    glVertex2f(0.6,3.0)
    glVertex2f(1.2,2.4)
    glVertex2f(0.6,2.4)
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
    glVertex2f(4.0,2.0)
    glVertex2f(3.4,2.0)
    glVertex2f(2.8,2.6)
    glVertex2f(3.4,2.6)
    glEnd()
    
    glEndList()
        
    
def X_letter():
    info = letter_dict.get('X')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)
    
    glBegin(GL_POLYGON)
    glVertex2f(4.0,8.0)
    glVertex2f(3.4,8.0)
    glVertex2f(3.4,6.2)
    glVertex2f(4.0,6.8)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(0.0,8.0)
    glVertex2f(0.6,8.0)
    glVertex2f(0.6,6.2)
    glVertex2f(0.0,6.8)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(0.0,0.0)
    glVertex2f(0.6,0.0)
    glVertex2f(0.6,1.8)
    glVertex2f(0.0,1.2)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(4.0,0.0)
    glVertex2f(3.4,0.0)
    glVertex2f(3.4,1.8)
    glVertex2f(4.0,1.2)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(4.0,1.2)
    glVertex2f(3.4,1.2)
    glVertex2f(0.0,6.8)
    glVertex2f(0.6,6.8)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(4.0,6.8)
    glVertex2f(3.4,6.8)
    glVertex2f(0.0,1.2)
    glVertex2f(0.6,1.2)
    glEnd()
    
    glEndList()

def PAIYANNOI():
    info = letter_dict.get('ฯ')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)
    
    glBegin(GL_POLYGON)
    glVertex2f(0.0, 5.0)
    glVertex2f(0.6, 5.0)
    glVertex2f(0.6, 2.6)
    glVertex2f(0.0, 3.2)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(3.0, 5.0)
    glVertex2f(2.4, 5.0)
    glVertex2f(2.4, 0.4)
    glVertex2f(3.0, 1.0)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(3.0,1.0)
    glVertex2f(2.4,1.0)
    glVertex2f(1.4,0.0)
    glVertex2f(2.0,0.0)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0.0,3.2)
    glVertex2f(0.6,2.6)
    glVertex2f(1.4,2.6)
    glVertex2f(2.0,3.2)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(2.0,2.6)
    glVertex2f(1.4,2.6)
    glVertex2f(2.4,4.0)
    glVertex2f(3.0,4.0)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(0.0,3.4)
    glVertex2f(0.6,3.4)
    glVertex2f(1.2,2.8)
    glVertex2f(0.6,2.8)
    glEnd()
    
    glEndList()

def tong():
    info = letter_dict.get('ธ')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)

    glBegin(GL_POLYGON)
    glVertex2f(0.6, 2)
    glVertex2f(0.0, 2)
    glVertex2f(0,0)
    glVertex2f(0.6,0)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(0,0.6)
    glVertex2f(0,0)
    glVertex2f(4,0.0)
    glVertex2f(4,0.6)
    glEnd()

    # glColor3f(1,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(3.4,0)
    glVertex2f(4,0.0)
    glVertex2f(4,2.7)
    glVertex2f(3.4,3.3)
    glEnd()      
    
    glBegin(GL_POLYGON)
    glVertex2f(0,3.3)
    glVertex2f(0,2.7)
    glVertex2f(4,2.7)
    glVertex2f(3.4,3.3)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(0,3)
    glVertex2f(0.6,3)
    glVertex2f(0.6,5)
    glVertex2f(0,4.4)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0.6,5.0) 
    glVertex2f(3.4,5) 
    glVertex2f(4,4.4) 
    glVertex2f(0.6,4.4) 
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(3.4,5)
    glVertex2f(4,4.4)
    glVertex2f(4,4)
    glVertex2f(3.4,4)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(4.0,2.5)
    glVertex2f(3.4,2.5)
    glVertex2f(2.8,3.1)
    glVertex2f(3.4,3.1)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(4.0,4.2)
    glVertex2f(3.4,4.2)
    glVertex2f(2.8,4.8)
    glVertex2f(3.4,4.8)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0.6,4.2)
    glVertex2f(0.0,4.2)
    glVertex2f(0.6,4.8)
    glVertex2f(1.2,4.8)
    glEnd()
   
    glEndList()

def C_letter():
    info = letter_dict.get('C')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)
    
    glBegin(GL_POLYGON)
    glVertex2f(0,7.4)
    glVertex2f(0.6,8)
    glVertex2f(3.4,8)
    glVertex2f(4,7.4)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0.6,8)
    glVertex2f(1.6,8)
    glVertex2f(0,6.4)
    glVertex2f(0,7.4)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0.6,8)
    glVertex2f(0,7.4)
    glVertex2f(0,0.6)
    glVertex2f(0.6,0)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(3.4,8)
    glVertex2f(4,7.4)
    glVertex2f(4,6)
    glVertex2f(3.4,6)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(3.4,2)
    glVertex2f(4,2)
    glVertex2f(4,0.6)
    glVertex2f(3.4,0)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0,0.6)
    glVertex2f(0.6,0)
    glVertex2f(3.4,0)
    glVertex2f(4,0.6)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(2.4,8)
    glVertex2f(3.4,8)
    glVertex2f(4,7.4)
    glVertex2f(4,6.4)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0,1.6)
    glVertex2f(0,0.6)
    glVertex2f(0.6,0)
    glVertex2f(1.6,0)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(4,1.6)
    glVertex2f(4,0.6)
    glVertex2f(3.4,0)
    glVertex2f(2.4,0)
    glEnd()

    glEndList()
    
def leusee():
    info = letter_dict.get('ษ')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)
    glBegin(GL_POLYGON)
    glVertex2f(3.4, 5)
    glVertex2f(4.0, 5)
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

    glBegin(GL_POLYGON)
    glVertex2f(2.0,3.3)
    glVertex2f(5.0,3.3)
    glVertex2f(5.0,2.7)
    glVertex2f(2.0,2.7)
    glEnd()
    glEndList()
