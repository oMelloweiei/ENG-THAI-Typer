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
  
from Group_10_Font import *

left = -3
right = 10
bottom = -6
top = 12
near = 10
far = -10

move = 5

mini_height = 5
mini_width = 4
big_height = 8

ex_height_b = -3

win_width = 640
win_height = 1000
win_x = 100
win_y = 100

my_char = ''
text = ''
alpha = ''
n = 0
s_table = True

KorKai_ThaiLetter , L_AL_Letter, g_Engletter , saraae_letter ,YOR_YAK_thailetter = 0 , 0 , 0 , 0 ,0

def ro_rua():
    glPushMatrix()
    glBegin(GL_POLYGON)
    glVertex2f(0.6, 4)
    glVertex2f(0, 4)
    glVertex2f(0,0.6)
    glVertex2f(0.6,0)
    glEnd()
    
    #เล้นนอนล่าง
    glBegin(GL_POLYGON)
    glVertex2f(0,0.6)
    glVertex2f(2.4,0.6)
    glVertex2f(2.4,0)
    glVertex2f(0.6,0)
    glEnd()
    
    #เส้นขวาสุด
    glBegin(GL_POLYGON)
    glVertex2f(3.0,0.6)
    glVertex2f(2.4,0)
    glVertex2f(2.4,mini_height)
    glVertex2f(3.0,5.0)
    glEnd()
    
    #เส้นบนสุด
    glBegin(GL_POLYGON)
    glVertex2f(3,mini_height) 
    glVertex2f(3,4.4) 
    glVertex2f(1.6,4.4) 
    glVertex2f(1.6,mini_height) 
    glEnd()

    #ทะแยงล่างขวา           
    glBegin(GL_POLYGON)
    glVertex2f(2.4,0.8)
    glVertex2f(3.0,0.8)
    glVertex2f(1.6,0.0)
    glVertex2f(2.4 ,0.0)
    glEnd() 

    #ทะแยงล่างซ้าย
    glBegin(GL_POLYGON)
    glVertex2f(0.6, 0.8)
    glVertex2f(0.0, 0.8)
    glVertex2f(0.6, 0.2)
    glVertex2f(1.2, 0.2)
    glEnd() 

    glPopMatrix()



def draft():
    glColor3f(1,0,0)
    glPushMatrix()
    glTranslatef(3,6, 0) # ปรับตำแหน่งให้ตัวอักษรอยู่ด้านบน
    #glTranslatef(0, move + 0.5, 0) 

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

    
def init():
    glClearColor (0,0,0,0) 
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    #define display mode to orthographics
    glOrtho(left, right, bottom, top, near, far)
    glShadeModel(GL_SMOOTH)

def draw_box():
    glColor3f(1,0.5,1)

    glPolygonMode(GL_FRONT_AND_BACK , GL_LINE)
    glBegin(GL_QUADS)
    glVertex2f(0,mini_height)
    glVertex2f(mini_width,mini_height)
    glVertex2f(mini_width,0)
    glVertex2f(0,0)
    glEnd()


def extra_height_line_t():
    global left, right , big_height
    glColor3f(0,0,1)

    glBegin(GL_LINES)
    glVertex2f(left, big_height)
    glVertex2f(right, big_height)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(left, ex_height_b)
    glVertex2f(right, ex_height_b)
    glEnd()
    

def table():
    global left ,right , bottom , top
    
    glBegin(GL_LINES)  
    for i in range(-10,11):
        if i == 0 :
            glColor3f(0,1,0)
        else:
            glColor3f(0.5,0,0)
        glVertex2f(left , i)
        glVertex2f(right , i)
    glEnd()
    
    glColor3f(1,0,0)
    glBegin(GL_LINES)
    for j in range(-10,11):
        if j == 0:
            glColor3f(0,1,0)
        else:
            glColor3f(0.5,0,0)
        glVertex2f(j , top)
        glVertex2f(j , bottom)
    glEnd()
   
def display():
    global my_char , s_table , n
    glClear (GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity ()             # clear the matrix 
    
    if s_table:
        table()    
        extra_height_line_t()
        draw_box()
        
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    glColor3f(1.0, 1.0, 1.0)

    ro_rua()
    
    glPushMatrix()
    draft()
    glPopMatrix()

    glFlush()
    glutSwapBuffers()
    glMatrixMode(GL_PROJECTION)
    
def addText(texts, alpha):
    character = str(alpha)
    texts = texts + character
    pass

def mouse(btn, state, x, y):
    global s_table
    
    if btn == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        s_table = not s_table
        print("right mouse clicked")

def keyboard (key,x,y):
    global my_char , text , s_table
        
    if key == b'\r':
        my_char = ''
    if key == b'\x7f':
        my_char = my_char[:-1]     
  
    glutPostRedisplay()

def reshape(w, h):
    global left, right, bottom, top, a, k
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    l_a = left
    r_a = right
    t_a = top
    b_a = bottom
    a = float(w) / h  # aspect ratio
    k = (right-left) / (top-bottom)

    if a >= 1:  # width >= height
        l_a = a * left
        r_a = a * right
    else:
        t_a = top / a
        b_a = bottom / a

    if k >= 1:
        l_a /= k
        r_a /= k
    else:
        t_a *= k
        b_a *= k

    glOrtho(l_a, r_a, b_a, t_a, 5, -5)
    glutPostRedisplay()
    
def main():

    glutInit(sys.argv)
    glutInitDisplayMode (GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize (win_width, win_height)
    glutInitWindowPosition (win_x, win_y)
    glutCreateWindow ('Font'.encode())

    init ()
    #callback registers
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutMouseFunc(mouse)
    glutReshapeFunc(reshape)
    glutMainLoop()

main()