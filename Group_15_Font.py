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

move = 0

letter_dict = {
	'ฎ': [174, 4.6, 0],
	'ฃ': [163, 3, 0],
	'ํ': [237, 0.2, 0],
	'l': [108, 1, 0],
	'Q': [81, 4, 0],
}

ASCII = 0
SIZE = 1
CLST = 2

def init_font():
    Dorchada()
    Korkud()
    l_eng()
    Q_eng()
    sara__Nikhahit()
       
#================= ฏ =================#    
def Dorchada():
    info = letter_dict.get('ฎ')
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

    glBegin(GL_POLYGON)
    glVertex2f(4.0,-0.0)
    glVertex2f(4.0,-2.4)
    glVertex2f(3.4,-2.4)
    glVertex2f(3.4,-0.0)
    glEnd() 

    glBegin(GL_POLYGON)
    glVertex2f(4.0,-2.4)
    glVertex2f(3.4,-2.4)
    glVertex2f(2.0,-1.0)
    glVertex2f(2.6,-1.0)
    glEnd()  

    glBegin(GL_POLYGON)
    glVertex2f(2.2,-1.0)
    glVertex2f(3.0,-1.6)
    glVertex2f(0.0,-1.6)
    glVertex2f(0.0,-1.0)
    glEnd()	   

    glBegin(GL_POLYGON)
    glVertex2f(2.2,-1.6)
    glVertex2f(1.6,-1.6)
    glVertex2f(2.4,-0.8)
    glVertex2f(3.0,-0.8)
    glEnd() 

    glBegin(GL_POLYGON)
    glVertex2f(2.4,-0.8)
    glVertex2f(3.0,-0.8)
    glVertex2f(3.0,-0.4)
    glVertex2f(2.4,-0.4)
    glEnd()
    glPopMatrix()

    glEndList()

#================= ฃ =================#
def Korkud():
    info = letter_dict.get('ฃ')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)

    glPushMatrix()
    glTranslatef(0,0,0)
   
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
    glPopMatrix()

    glEndList()

#================= l =================#
def l_eng():
    info = letter_dict.get('l')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)
    glPushMatrix()
    glTranslatef(0.2,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(0.6, 8.0)
    glVertex2f(0.0, 8.0)
    glVertex2f(0.0,0.0)
    glVertex2f(0.6,0.0)
    glEnd()
    glPopMatrix()
    glEndList()

#================= Q =================#          
def Q_eng():
    info = letter_dict.get('Q')
    info[CLST] = glGenLists(info[ASCII])
    glNewList(info[CLST], GL_COMPILE)

    glBegin(GL_POLYGON)
    glVertex2f(0.6, 8.0)
    glVertex2f(0, 7.4)
    glVertex2f(0,0.6)
    glVertex2f(0.6,0.0)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(0.0,0.6)
    glVertex2f(4.0,0.6)
    glVertex2f(3.4,0.0)
    glVertex2f(0.6,0.0)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(4.0,0.6)
    glVertex2f(3.4,0.0)
    glVertex2f(3.4,8.0)
    glVertex2f(4.0,7.4)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(3.4,8.0) 
    glVertex2f(4.0,7.4) 
    glVertex2f(0.0,7.4) 
    glVertex2f(0.6,8.0) 
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(2.8,1.3) 
    glVertex2f(2.5,1.0) 
    glVertex2f(3.7,-0.6) 
    glVertex2f(4.0,-0.3) 
    glEnd()

   ##################### มุม Q #########################
               
    glBegin(GL_POLYGON)
    glVertex2f(3.4,0.8)
    glVertex2f(4.0,0.8)
    glVertex2f(3.4 ,0.2)
    glVertex2f(2.8 ,0.2)
    glEnd() 

    glBegin(GL_POLYGON)
    glVertex2f(0.6,7.8)
    glVertex2f(1.2,7.8)
    glVertex2f(0.6 ,7.2)
    glVertex2f(0.0 ,7.2)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(3.4, 7.2)
    glVertex2f(4.0, 7.2)
    glVertex2f(3.4, 7.8)
    glVertex2f(2.8, 7.8)
    glEnd() 

    glBegin(GL_POLYGON)
    glVertex2f(0.6, 0.8)
    glVertex2f(0.0, 0.8)
    glVertex2f(0.6, 0.2)
    glVertex2f(1.2, 0.2)
    glEnd()

    glEndList()
#================= อํ =================#
def sara__Nikhahit():
    info = letter_dict.get('ํ')
    info[CLST] = glGenLists(info[ASCII])

    glNewList(info[CLST], GL_COMPILE)
    glPushMatrix()
    glTranslatef(2.8, 6, 0)

    glBegin(GL_POLYGON)
    glVertex2f(0.0,0.3)
    glVertex2f(0.0,0.9)
    glVertex2f(0.3,1.2)
    glVertex2f(0.3,0.0)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0.9,0.0)
    glVertex2f(0.9,1.2)
    glVertex2f(1.2,0.9)
    glVertex2f(1.2,0.3)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(0.3,1.2)
    glVertex2f(0.0,0.9)
    glVertex2f(1.2,0.9)
    glVertex2f(0.9,1.2)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0.3,0.0)
    glVertex2f(0.0,0.3)
    glVertex2f(1.2,0.3)
    glVertex2f(0.9,0.0)
    glEnd()

    # glColor3f(1,0,0)
    glBegin(GL_POLYGON)
    glVertex2f(0.0,0.8)
    glVertex2f(0.3,0.8)
    glVertex2f(0.6,1.1)
    glVertex2f(0.3,1.1)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0.0,0.4)
    glVertex2f(0.3,0.4)
    glVertex2f(0.6,0.1)
    glVertex2f(0.3,0.1)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0.9,0.1)
    glVertex2f(0.6,0.1)
    glVertex2f(0.9,0.4)
    glVertex2f(1.2,0.4)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(0.9,1.1)
    glVertex2f(0.6,1.1)
    glVertex2f(0.9,0.8)
    glVertex2f(1.2,0.8)
    glEnd()

    glPopMatrix()

    glEndList()

#================= End =================#