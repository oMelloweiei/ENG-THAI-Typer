import Group_19_Font as Group_19_Font

import sys

from OpenGL.GL.VERSION import GL_1_0
from OpenGL.raw.GLUT import STRING
try:
  from OpenGL.GLUT import *
  from OpenGL.GL import *
  from OpenGL.GLU import *
except:
  print ('''ERROR: PyOpenGL not installed properly.''')

left = -50
right = 50
bottom = -50
top = 50
near = -15
far = 15

move = 6

win_width = 640
win_height = 480

win_x = 100 + 1000
win_y = 100

begin_pos = [-40, 0]

grid = False

#main line
line = ""

#for condition
thai_slim = "ใ"
thai_normal = "รฏ"
eng_slim = "Y"

#position in letter dictionary
ASCII = 0
SIZE = 1
CLST = 2

def init():
	glClearColor (0,0,0,0) 
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	glOrtho(left, right, bottom, top, near, far)
	glShadeModel(GL_SMOOTH)

	Group_19_Font.init_font()

def table():
	global left ,right , bottom , top
		
	glBegin(GL_LINES)  
	for i in range(-10,11):
		glColor3f(1,0,0)
		if i == 0:
			glColor3f(0,1,0)
		glVertex2f(left , i)
		glVertex2f(right , i)
	glEnd()
		
	glBegin(GL_LINES)
	for j in range(-10,11):
		glColor3f(1,0,0)
		if j == 0:
			glColor3f(0,1,0)
		glVertex2f(j , top)
		glVertex2f(j , bottom)
	glEnd()  

def display_letter():
	glTranslatef(begin_pos[0], begin_pos[1], 0)

	position = 0
	move = 0
	for i in range(0, len(line)):
		letter = line[i]
		info = Group_19_Font.letter_dict.get(letter)
		letter_size = info[SIZE]
		if letter == 'ใ': 
			if (i != 0 and line[i - 1] in thai_normal):
				position -= 1
			move += position
			glTranslatef(position, 0, 0)
			glCallList(info[CLST])
		elif letter == 'ร':
			if (i != 0 and line[i - 1] in thai_slim):
				position -= 1
			move += position
			glTranslatef(position, 0, 0)
			glCallList(info[CLST])
		elif letter == 'ฏ':
			if (i != 0 and line[i - 1] in thai_slim):
				position -= 1
			move += position
			glTranslatef(position, 0, 0)
			glCallList(info[CLST])
		elif letter == 'D':
			move += position
			glTranslatef(position, 0, 0)
			glCallList(info[CLST])
		elif letter == 't':
			if (i != 0 and line[i - 1] in eng_slim):
				position -= 1
			move += position
			glTranslatef(position, 0, 0)
			glCallList(info[CLST])
		elif letter == 'Y':
			if (i != 0 and line[i - 1].lower()):
				position -= 1
			move += position
			glTranslatef(position, 0, 0)
			glCallList(info[CLST])
		position = letter_size + 1
	glTranslatef(-move, 0, 0)
	

def display():
	glClear (GL_COLOR_BUFFER_BIT)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity ()			 # clear the matrix 
	glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
	if grid:
		table()
	glColor3f(1.0, 1.0, 1.0)
	if len(line) != 0:
		display_letter()
	glFlush()
	glutSwapBuffers()
	glMatrixMode(GL_PROJECTION)

def mouse(button, state, x, y):
	global begin_pos
	global left, right, bottom, top, a, k
	if state == GLUT_DOWN:
		if (button == GLUT_LEFT_BUTTON):
			modelview = glGetDoublev(GL_MODELVIEW_MATRIX)
			projection = glGetDoublev(GL_PROJECTION_MATRIX)
			viewport = glGetIntegerv(GL_VIEWPORT)
			# Convert screen coordinates (x, y) to world coordinates
			winX, winY, winZ = gluUnProject(x, win_height - y, 0, modelview, projection, viewport)
			# Adjust for your coordinate system
			winX += begin_pos[0]
			winY += begin_pos[1]
			begin_pos[0] = winX
			begin_pos[1] = winY
	
	glutPostRedisplay()

def keyboard (key, x, y):
	global grid, line
		
	if key == b'\x83':  # Thai character ใ
		line += 'ใ'
	elif key == b'\xa3':  # Thai character ร
		line += 'ร'
	elif key == b'\x8f':  # Thai character ฏ
		line += 'ฏ'
	elif key == b'D':
		line += 'D'
	elif key == b't':
		line += 't'
	elif key == b'Y':
		line += 'Y'
	elif key == b'\x08':
		if len(line) != 0:
			line = line[:-1]
	elif key == b'\r':
		line = ""
	elif key == b'=':
		grid = not grid
	else:
		print("Nothing [", key, "]")
	print(line)
 
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

def idle():
	pass

glutInit(sys.argv)
glutInitDisplayMode (GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize (win_width, win_height)
glutInitWindowPosition (win_x, win_y)
glutCreateWindow ('Font'.encode())

init()
glutReshapeFunc(reshape)
glutDisplayFunc(display)
glutKeyboardFunc(keyboard)
glutMouseFunc(mouse)
glutIdleFunc(idle)
glutMainLoop()