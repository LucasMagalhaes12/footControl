import subprocess
from time import sleep


class Control:
	def __init__(self):
		# self.maxValueMousePosX = self.maxValueMousePosY = 0
		subprocess.Popen(["ydotoold"])
		self.acceleration = 1


	def notify(self, title:str, comment:str):
		subprocess.run(["notify-send", title, comment]) 


	def mouseMove(self, x:int=0, y:int=0):
		if x != 0 or y != 0:
			subprocess.run([
				"ydotool", "mousemove", 
				"-x", str(x * self.acceleration), 
				"-y", str(y * self.acceleration)
        	])


	def mouseClickRight(self, state:int=0):
		if state == 0:
			subprocess.run(["ydotool", "click", "0x81"])

		elif state == 1:
			subprocess.run(["ydotool", "click", "0x41"])


	def mouseClickLeft(self, state:int=0):
		if state == 0:
			subprocess.run(["ydotool", "click", "0x80"])

		elif state == 1:
			subprocess.run(["ydotool", "click", "0x40"])
		
		
	def mouseScrollUp(self):
		subprocess.run(["ydotool", "mousemove", "-w", "--", "0", "1"])


	def mouseScrollDown(self):
		subprocess.run(["ydotool", "mousemove", "-w", "--", "0", "-1"])
