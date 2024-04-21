#!/usr/bin/python

import sys

from OpenGL.GL.VERSION import GL_1_0
from OpenGL.raw.GLUT import STRING
try:
    from OpenGL.GLUT import *
    from OpenGL.GL import *
    from OpenGL.GLU import *
except:
    print('''ERROR: PyOpenGL not installed properly.''')

mini_height = 5
mini_width = 4
big_height = 8

ex_height_b = -3

move = 5

letter_dict = {
	'g': [103, 4, 0],
	'L': [76, 4, 0],
	'ย': [194, 4, 0],
	'แ': [225, 3.4, 0],
	'ก': [161, 4, 0],
}

ASCII = 0
SIZE = 1
CLST = 2

def init_font():
    yak()
    korkai()
    sara_ae()
    L()
    g()

def yak():
    info = letter_dict.get('ย')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE) 
    glBegin(GL_POLYGON)
    glVertex2f(0.6, 2.7)
    glVertex2f(0, 2.1)
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
    glVertex2f(3.4,mini_height)
    glVertex2f(4.0,mini_height)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(2,mini_height) 
    glVertex2f(2,4.4) 
    glVertex2f(0.0,4.4) 
    glVertex2f(0.6,mini_height) 
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(2.0,3.0) 
    glVertex2f(2.0,2.4) 
    glVertex2f(0.6,2.4) 
    glVertex2f(0.6,3.0) 
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(0.0,3.8)
    glVertex2f(0.0,3.0)
    glVertex2f(0.6 ,2.4)
    glVertex2f(0.8 ,3.0)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(0.0,2.4)
    glVertex2f(0.0,1.6)
    glVertex2f(0.8 ,2.4)
    glVertex2f(0.6 ,3.0)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(0.0,4.4)
    glVertex2f(0.6,5.0)
    glVertex2f(0.6,2.7)
    glVertex2f(0.0,3.3)
    glEnd()
            
    glBegin(GL_POLYGON)
    glVertex2f(4.0,1.4)
    glVertex2f(4.0,0.6)
    glVertex2f(3.4 ,0.0)
    glVertex2f(2.6 ,0.0)
    glEnd() 

    glBegin(GL_POLYGON)
    glVertex2f(0.6,4.8)
    glVertex2f(1.2,4.8)
    glVertex2f(0.6 ,4.2)
    glVertex2f(0.0 ,4.2)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0.6, 0.8)
    glVertex2f(0.0, 0.8)
    glVertex2f(0.6, 0.2)
    glVertex2f(1.2, 0.2)
    glEnd() 
    glEndList()

def korkai():
    info = letter_dict.get('ก')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE) 
    glBegin(GL_POLYGON)
    glVertex2f(0.6, 3.0)
    glVertex2f(0.0, 3.0)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.6, 0.0)
    glEnd()
    
    #back
    glBegin(GL_POLYGON)
    glVertex2f(4.0, 0)
    glVertex2f(3.4, 0)
    glVertex2f(3.4,5.0)
    glVertex2f(4.0,4.4)
    glEnd()
    
    #top
    glBegin(GL_POLYGON)
    glVertex2f(3.4,5.0) 
    glVertex2f(4.0,4.4) 
    glVertex2f(0.0,4.4) 
    glVertex2f(0.4,5.0) 
    glEnd()
    #LeftTop
    glBegin(GL_POLYGON)
    glVertex2f(0,4.4)
    glVertex2f(0.6,4.4)
    glVertex2f(0.6,3.6)
    glVertex2f(0,3.6)
    glEnd()
    
    #TopEdge
    glBegin(GL_POLYGON)
    glVertex2f(3.4, 4.2)
    glVertex2f(4.0, 4.2)
    glVertex2f(3.2, 5.0)
    glVertex2f(2.6, 5.0)
    glEnd() 
    
    #TopLeftEdge
    glBegin(GL_POLYGON)
    glVertex2f(0.6, 4.2)
    glVertex2f(0, 4.2)
    glVertex2f(0.8, 5.0)
    glVertex2f(1.4, 5.0)
    glEnd() 

    #Mouth
    glBegin(GL_POLYGON)
    glVertex2f(0, 4.0)
    glVertex2f(1.4, 4.0)
    glVertex2f(1.4, 3.6)
    glVertex2f(0, 3.6)
    glEnd() 
    
    #DownMouth
    glBegin(GL_POLYGON)
    glVertex2f(0.6, 3)
    glVertex2f(0.0, 3)
    glVertex2f(0.8, 3.6)
    glVertex2f(1.4, 3.6)
    glEnd()
    glEndList()

def L():
    info = letter_dict.get('L')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE) 
    glBegin(GL_POLYGON)
    glVertex2f(0, 8.0)
    glVertex2f(0.6, 8.0)
    glVertex2f(0.6,0.0)
    glVertex2f(0,0.0)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0, 0.6)
    glVertex2f(0, 0)
    glVertex2f(4.0, 0)
    glVertex2f(4.0, 0.6)  
    glEnd()
    glEndList()

def g():
    info = letter_dict.get('g')
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
    glVertex2f(3.4,mini_height)
    glVertex2f(4.0,4.4)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(3.4,mini_height) 
    glVertex2f(4.0,4.4) 
    glVertex2f(0.0,4.4) 
    glVertex2f(0.6,mini_height) 
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(0.0,4.4)
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

def sara_ae():
    info = letter_dict.get('แ')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE) 
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

    glBegin(GL_POLYGON)
    glVertex2f(2, 0.6)
    glVertex2f(2.6, 0)
    glVertex2f(2.6,5)
    glVertex2f(2,5)
    glEnd()
    
    #2
    glBegin(GL_POLYGON)
    glVertex2f(2, 0.6)
    glVertex2f(2.6, 0)
    glVertex2f(3.4,0)
    glVertex2f(3.4,0.6)
    glEnd()
    
    # ซ้ายล่างตัด   
    glBegin(GL_POLYGON)
    glVertex2f(2, 0.6)
    glVertex2f(2.6, 0)
    glVertex2f(2.8,0.6)
    glVertex2f(2.6,0.8)
    glEnd()

    glEndList()