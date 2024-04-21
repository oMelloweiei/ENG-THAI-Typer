import sys
from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
import Group_1_Font as G_1
import Group_2_Font as G_2
import Group_3_Font as G_3
import Group_4_Font as G_4
import Group_5_Font as G_5
import Group_6_Font as G_6
import Group_7_Font as G_7
import Group_8_Font as G_8
import Group_9_Font as G_9
import Group_10_Font as G_10
import Group_11_Font as G_11
import Group_12_Font as G_12
import Group_13_Font as G_13
import Group_14_Font as G_14
import Group_15_Font as G_15
import Group_16_Font as G_16
import Group_17_Font as G_17
import Group_18_Font as G_18
import Group_19_Font as G_19
import Group_20_Font as G_20
import Group_21_Font as G_21

list_of_font = [G_1, G_2, G_3, G_4, G_5, G_6, G_7, G_8, G_9, G_10,
				G_11, G_12, G_13, G_14, G_15, G_16, G_17, G_18, G_19, G_20 , G_21
				]

w_width , w_height = 1024 , 680

class Font_display:
	def __init__(self , list_font):
		#for condition
		self.eng_mini = "abcdefghjitklmnopqrsuwvyxz"
		self.language = ["ABCDEFGHIJKLMNOPQRSTUVWXYZabcedfghijklmnopqrstuvwxyz" , 
						"กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรลวศษสหฬอฮ ิ ื ์ ้ ่ ๋ ๊ ็ ี ั ํ ำ ๆฯ ุ ู ึะ า ฺ เโแไใา ฦ ฤ"]
		self.eng_bs = "YT"

		self.normal_sara = "าะแเ"
		self.sara_mai = "ใโไ"
		self.top_sara = " ิ ื ั  ี  ึ ํ ้  ็ ์  ๊".replace(" ", "")
		self.top_tan = "์"
		self.sara_a = "ั"
		self.top_mini = "่๋ํ"
		self.below_sara = "ฺุู"
		self.thai_tall = "ฟฝปฬ"
		self.thai_wide = "ณฒญฌ"
		self.thai_3 = "ขฃงจวะาฯ"
		self.thai_normal = "กคฅฆฉฑดตถทธนบผพภมยรลษหอฮ"
		self.thai_h_5 = "ชซศสฮ"
		self.thai_dive = "ฏฎฐญ"
		
		self.all_top_below_sara = self.top_sara + self.top_mini + self.below_sara
		self.all_top_sara = self.top_sara + self.top_mini
		self.all_thai_char = self.thai_normal + self.thai_h_5 + self.thai_3 + self.thai_tall + self.thai_wide + self.thai_dive
		self.all_normal_sara = self.sara_mai + self.normal_sara

		self.prev_size = 0
		self.prev_prev_size = 0

		#font detail
		self.ASCII = 0
		self.SIZE = 1
		self.CLST = 2
		self.move_slim = 1
		self.position = 0	

		self.add_ons = {' ': [1,1,0],
						'ๆ': [230,3,0]
					}

		self.list_font = list_font

		self.group_mapping = {"zeJจผะ": G_1, "ydIดวึ": G_2, "xcHศฐฺ": G_3, "Gbwพปำ": G_4, "avFงนิ": G_5, "ZEuตฮู": G_6, "DtYรฏใ": G_7,
							"CsXธษฯ": G_8, "rWBคฬฤ": G_9, "AqVบฉ็": G_10, "pUฌขเ่": G_11, "oTณสฦ๋": G_12, "nSฑ์ถั": G_13, "mRอภ๊ไ": G_14,
							"Qlฎฃํ": G_15, "Pkฟฅี": G_16, "Ojหมืล": G_17, "Niชญุ": G_18, "Mhฒซา้": G_19, "gLยกแ": G_20, "fKฝทโฆ": G_21,
							}

	def blank_space(self):
		info = self.add_ons.get(' ')
		info[self.CLST] = glGenLists(info[self.ASCII])
		glNewList(info[self.CLST], GL_COMPILE) 
		glPushMatrix()
		glTranslatef(1,0,0)
		glPopMatrix()
		glEndList()

	def Maiyamhok(self):
		info = self.add_ons.get('ๆ')
		info[self.CLST] = glGenLists(info[self.ASCII])
		glNewList(info[self.CLST], GL_COMPILE) 
		glPushMatrix()

		glBegin(GL_POLYGON)
		glVertex2f(0.6,3.0)
		glVertex2f(1.2,3.0)
		glVertex2f(1.2,3.6)
		glVertex2f(0.0,3.6)
		glEnd()

		glBegin(GL_POLYGON)
		glVertex2f(0.6,3.6)
		glVertex2f(0.0,3.6)
		glVertex2f(0.0,4.4)
		glVertex2f(0.6,5.0)
		glEnd()

		glBegin(GL_POLYGON)
		glVertex2f(0.0,4.4)
		glVertex2f(0.6,5.0)
		glVertex2f(0.9,5.0)
		glVertex2f(1.5,4.4)
		glEnd()

		glBegin(GL_POLYGON)
		glVertex2f(1.5,4.4)
		glVertex2f(2.1,5.0)
		glVertex2f(2.4,5.0)
		glVertex2f(3.0,4.4)
		glEnd()

		glBegin(GL_POLYGON)
		glVertex2f(1.2,4.4)
		glVertex2f(1.8,4.4)
		glVertex2f(1.8,4.0)
		glVertex2f(1.2,4.0)
		glEnd()

		glBegin(GL_POLYGON)
		glVertex2f(2.4,5.0)
		glVertex2f(3.0,4.4)
		glVertex2f(3.0,-1.2)
		glVertex2f(2.4,-1.2)
		glEnd()

		glBegin(GL_POLYGON)
		glVertex2f(3.0,-1.2)
		glVertex2f(2.4,-1.2)
		glVertex2f(1.8,-3.0)
		glVertex2f(2.4,-3.0)
		glEnd()

		glBegin(GL_POLYGON)
		glVertex2f(0.6,4.2)
		glVertex2f(0.2,4.2)
		glVertex2f(0.6,4.6)
		glVertex2f(1.0,4.6)
		glEnd()

		glBegin(GL_POLYGON)
		glVertex2f(1.8,4.2)
		glVertex2f(1.4,4.2)
		glVertex2f(1.8,4.6)
		glVertex2f(2.2,4.6)
		glEnd()

		glBegin(GL_POLYGON)
		glVertex2f(1.2,4.6)
		glVertex2f(0.8,4.6)
		glVertex2f(1.2,4.2)
		glVertex2f(1.6,4.2)
		glEnd()

		glBegin(GL_POLYGON)
		glVertex2f(2.4,4.6)
		glVertex2f(2.0,4.6)
		glVertex2f(2.4,4.2)
		glVertex2f(2.8,4.2)
		glEnd()

		glBegin(GL_POLYGON)
		glVertex2f(0.6,3.2)
		glVertex2f(1.2,3.2)
		glVertex2f(0.6,3.8)
		glVertex2f(0.0,3.8)
		glEnd()

		glPopMatrix()

		glEndList()

	def store(self):

		self.blank_space()
		self.Maiyamhok()

		for i in self.list_font:
			i.init_font()

	def get_info(self,letter):
		for key , group in self.group_mapping.items():
			if letter in key:
				return group.letter_dict.get(letter)
			elif letter == ' ' or letter == 'ๆ':
				return self.add_ons.get(letter)
			
	def sara_aum(self , letter_size = 0 , prev_letter = "" , shift = 0 , text = "" , len_text = 0):
		self.letter_size = letter_size + 1

		if prev_letter not in self.thai_normal and prev_letter not in self.thai_wide:
			shift = -1
		elif prev_letter in self.thai_wide:
			shift = 2.8

		glPushMatrix()
		if prev_letter == "" and len_text < 1:
			glTranslatef(0,0,0)
		else:
			glTranslatef(shift,0,0)
		self.info_nik = self.get_info('ํ')
		self.nik_size = self.info_nik[self.SIZE]
		glCallList(self.info_nik[self.CLST])
		glPopMatrix()

		glPushMatrix()
		if prev_letter == "" and len_text < 1:
			glTranslatef(5,0,0)
		else:
			glTranslatef(self.letter_size,0,0)
		self.info_a = self.get_info('า')
		self.a_size = self.info_a[self.SIZE]
		glCallList(self.info_a[self.CLST])
		glPopMatrix()

		return 4 + self.a_size

	def fly_check(self, text = "" , pre_letter = ""):
		if text in self.all_top_sara:
			return True
		else:
			return False
	
	def check_top_sara(self,letter ="" , prev_letter = []):
		if (letter in self.all_top_sara and
			(prev_letter in self.thai_tall or 
			prev_letter in self.thai_3  or
			prev_letter in self.thai_h_5)
	  		):
			return True
		else:
			return False
	
	def check_below_sara(self , prev_letter = "" , prev_text = "" , shift = 0 , dive = 0):
		if prev_letter in self.thai_3 or prev_letter in "ชซขฃ":
			shift = 1
		if prev_text in self.all_top_sara:
			dive = 2
		if prev_letter in self.thai_dive:
			dive += 2
		if prev_text in self.below_sara:
			if dive == 2 and prev_letter not in self.thai_dive: #debug for no space for below sara
				dive = 0
			if prev_letter in self.thai_dive:
				dive += 1
			else:
				dive += 3
		return shift , dive

	def draw(self, *text):
		space = 1
		position = 0
		prev_sara_size = 0
		fly = 0
		dive = 0
		letter_only = [""]
		prev_size_l = 0
		normal_size = 4
		lenght = len(text)
		print("start : ", text)
		# print("my letter only list", letter_only)

		for i, letter in enumerate(text):
			info = self.get_info(letter)
			letter_size = info[self.SIZE]
			move = 0
			shift = 0

			if letter in self.language[0]:
				if letter.isupper():
					if letter in self.eng_bs and i > 0 and text[i - 1] in self.eng_mini:
						move += self.move_slim
				elif letter.islower():
					if i > 0 and text[i - 1] in self.eng_bs:
						move += self.move_slim

			elif letter in self.language[1]:
				
				if lenght > 1:
					
					if not letter in self.all_top_sara:
						# print("reset fly")
						fly = 0
					if not letter in self.below_sara:
						# print("reset dive")
						dive = 0

					if letter == "ำ":
						self.sara_aum(prev_size_l , letter_only[-1] , shift , text[i-1] , lenght)
						glTranslatef(normal_size, fly - dive, 0)
						continue

					if letter in self.all_top_below_sara:
						move = prev_size_l + space

						if letter_only[-1] in self.thai_wide:
							shift = -2.6
							
						if letter in self.sara_a:
							shift = -1.5
							if letter_only[-1] in self.thai_wide:
								shift = -1.5 - 2.6
						if i < lenght - 1 and letter in self.all_top_sara and text[i + 1] == "ำ":
							fly += 2
						if self.check_top_sara(letter , letter_only[-1]):
							if not letter in self.sara_a:
								shift = 1

						if self.fly_check(text[i-1] , letter):
							fly += 2
					if letter in self.below_sara:
						shift , dive = self.check_below_sara(letter_only[-1] , text[i-1],shift,dive)
					
			position = (prev_size_l - move) + space

			print("prev", prev_sara_size , "self_pos" , position , "self_move" , move, "fly", fly, "dive", dive , "shift" , shift) #debug
			print("prev_letter_size" , prev_size_l)

			glTranslatef(position - shift, fly - dive, 0)
			glCallList(info[self.CLST])
			glTranslatef(shift, -fly + dive, 0)
			#After Finish Draw Letter
			if letter in self.all_top_below_sara:
				prev_sara_size = letter_size

			if ((len(letter_only) == 0 or letter != letter_only[-1]) and 
	   			(letter not in self.all_top_below_sara or letter in self.language[0])): #เก็บตัวอักษรอย่างเดียวเท่านั้นไม่เก็บสระ
					prev_size_l = letter_size
					letter_only.append(letter)
			

				
class Renderer:
	def __init__(self , myFont):
		self.left , self.bottom , self.far = -50,-50,-50
		self.top , self.right, self.near = 50 , 50 , 50
		self.aspect = 1.0
		self.line = ""
		self.myFont = myFont
		self.begin_pos = [self.left , 0]
		self.buffer = b''
		self.detect_thai = None
		self.key_eng_mapping = {b'A': 'A', b'B': 'B', b'C': 'C', b'D': 'D', b'E': 'E', b'F': 'F', b'G': 'G', b'H': 'H', b'I': 'I',
						b'J': 'J', b'K': 'K', b'L': 'L', b'M': 'M', b'N': 'N', b'O': 'O', b'P': 'P', b'Q': 'Q', b'R': 'R',
						b'S': 'S', b'T': 'T', b'U': 'U', b'V': 'V', b'W': 'W', b'X': 'X', b'Y': 'Y', b'Z': 'Z',
						b'a': 'a', b'b': 'b', b'c': 'c', b'd': 'd', b'e': 'e', b'f': 'f', b'g': 'g', b'h': 'h', b'i': 'i',
						b'j': 'j', b'k': 'k', b'l': 'l', b'm': 'm', b'n': 'n', b'o': 'o', b'p': 'p', b'q': 'q', b'r': 'r',
						b's': 's', b't': 't', b'u': 'u', b'v': 'v', b'w': 'w', b'x': 'x', b'y': 'y', b'z': 'z'
					} 

		self.key_thai_mapping = {b'\xe0\xb8\x81': 'ก', b'\xe0\xb8\x82': 'ข', b'\xe0\xb8\x83': 'ฃ', b'\xe0\xb8\x84': 'ค', 
					b'\xe0\xb8\x85': 'ฅ', b'\xe0\xb8\x86': 'ฆ', b'\xe0\xb8\x87': 'ง', b'\xe0\xb8\x88': 'จ', 
					b'\xe0\xb8\x89': 'ฉ', b'\xe0\xb8\x8a': 'ช', b'\xe0\xb8\x8b': 'ซ', b'\xe0\xb8\x8c': 'ฌ', 
					b'\xe0\xb8\x8d': 'ญ', b'\xe0\xb8\x8e': 'ฎ', b'\xe0\xb8\x8f': 'ฏ', b'\xe0\xb8\x90': 'ฐ', 
					b'\xe0\xb8\x91': 'ฑ', b'\xe0\xb8\x92': 'ฒ', b'\xe0\xb8\x93': 'ณ', b'\xe0\xb8\x94': 'ด', 
					b'\xe0\xb8\x95': 'ต', b'\xe0\xb8\x96': 'ถ', b'\xe0\xb8\x97': 'ท', b'\xe0\xb8\x98': 'ธ', 
					b'\xe0\xb8\x99': 'น', b'\xe0\xb8\x9a': 'บ', b'\xe0\xb8\x9b': 'ป', b'\xe0\xb8\x9c': 'ผ', 
					b'\xe0\xb8\x9d': 'ฝ', b'\xe0\xb8\x9e': 'พ', b'\xe0\xb8\x9f': 'ฟ', b'\xe0\xb8\xa0': 'ภ', 
					b'\xe0\xb8\xa1': 'ม', b'\xe0\xb8\xa2': 'ย', b'\xe0\xb8\xa3': 'ร', b'\xe0\xb8\xa4': 'ฤ', 
					b'\xe0\xb8\xa5': 'ล', b'\xe0\xb8\xa6': 'ฦ', b'\xe0\xb8\xa7': 'ว', b'\xe0\xb8\xa8': 'ศ', 
					b'\xe0\xb8\xa9': 'ษ', b'\xe0\xb8\xaa': 'ส', b'\xe0\xb8\xab': 'ห', b'\xe0\xb8\xac': 'ฬ', 
					b'\xe0\xb8\xad': 'อ', b'\xe0\xb8\xae': 'ฮ', 
					b'\xe0\xb8\xb0': 'ะ', b'\xe0\xb8\xb1': 'ั', b'\xe0\xb8\xb2': 'า', b'\xe0\xb8\xb3': 'ำ',
					b'\xe0\xb8\xb4': 'ิ', b'\xe0\xb8\xb5': 'ี', b'\xe0\xb8\xb6': 'ึ', b'\xe0\xb8\xb7': 'ื',
					b'\xe0\xb8\xb8': 'ุ', b'\xe0\xb8\xb9': 'ู',  b'\xe0\xb8\xba': 'ฺ', b'\xe0\xb9\x87': '็',
					b'\xe0\xb9\x88': '่', b'\xe0\xb9\x89': '้', b'\xe0\xb9\x8a': '๊',  b'\xe0\xb9\x8b': '๋', 
					b'\xe0\xb9\x8d': 'ํ',  b'\xe0\xb9\x86': 'ๆ', b'\xe0\xb9\x8c': '์', b'\xe0\xb8\xaf': 'ฯ',
					b'\xe0\xb9\x80': 'เ', b'\xe0\xb9\x81': 'แ', b'\xe0\xb9\x82': 'โ', b'\xe0\xb9\x83': 'ใ',
					b'\xe0\xb9\x84': 'ไ',
					}

		self.special_key_mapping = {b' ': ' '}
	
	def init(self):
		glClearColor(0.0,0.0,0.0,0.0)
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		glOrtho(self.left, self.right, self.bottom, self.top, self.near, self.far)
		glShadeModel(GL_SMOOTH)
		
	def display(self):
		glClear(GL_COLOR_BUFFER_BIT)
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()
		glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

		glBegin(GL_LINES)
		glVertex2f(self.begin_pos[0] , self.top)
		glVertex2f(self.begin_pos[0] , self.bottom)
		glEnd()

		glColor3f(1,1,1)
		glTranslatef(self.begin_pos[0],self.begin_pos[1],0)

		if len(self.line) != 0:
			self.myFont.draw(*self.line)

		glFlush()
		glutSwapBuffers()
		glMatrixMode(GL_PROJECTION)
		
	def reshape(self , w ,h):
		global w_width , w_height
		glViewport(0, 0, w, h)
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		
		self.aspect = float(w)/h
		
		if self.aspect >= 1:
			self.left *= self.aspect
			self.right *= self.aspect
		else:
			self.top    /= self.aspect
			self.bottom /= self.aspect
		w_width = w
		w_height = h
		glOrtho(self.left, self.right, self.bottom, self.top, self.near, self.far)
		glutPostRedisplay()

	def keyboard(self,key,x,y):

		if key in self.key_eng_mapping:
			self.line += self.key_eng_mapping[key]

		elif key == b'\xe0' or self.detect_thai:
			self.detect_thai = True
			self.buffer += key
			if len(self.buffer) == 3:
				self.detect_thai = False
				if self.buffer in self.key_thai_mapping:
					self.line += self.key_thai_mapping[self.buffer]
				self.buffer = b''

		elif key in self.special_key_mapping:
			self.line += self.special_key_mapping[key]
		elif key == b'\x7f':
			if len(self.line) > 0:
				self.line = self.line[:-1]
		else:
			print("Not Found")

		glutPostRedisplay()




myFont = Font_display(list_of_font)
render = Renderer(myFont)

def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
	glutInitWindowSize(w_width , w_height)
	glutInitWindowPosition(350 , 100)
	glutCreateWindow("CMM Font".encode())
	
	render.init()
	myFont.store()

	glutDisplayFunc(render.display)
	glutReshapeFunc(render.reshape)
	glutKeyboardFunc(render.keyboard)
	glutMainLoop()
	
if __name__ == "__main__":
	main()