import subprocess
from time import sleep


class Control:
	def __init__(self):
		self.maxValueMousePosX = self.maxValueMousePosY = 0
		subprocess.run(["ydotoold"])
		sleep(1)


	def notify(self, title:str, comment:str):
		subprocess.run(["notify-send", title, comment]) 


	def setVolume(self, volume:int):
			volume = str((volume // 100) * 10)
			print("--------"+volume)
			if self.__lastVolume != volume:
				subprocess.run(["amixer", "-D", "pulse", "set", "Master", volume+'%'])
				self.__lastVolume = volume


	def mouseMove(self, x:int=0, y:int=0):
		# print(x, y)
		if x == 0:
			self.maxValueMousePosX = 0
		elif (x > 0 and x > self.maxValueMousePosX) or x < self.maxValueMousePosX:
			self.maxValueMousePosX = x

		if y == 0:
			self.maxValueMousePosY = 0
		elif (y > 0 and y > self.maxValueMousePosY) or y < self.maxValueMousePosY:
			self.maxValueMousePosY = y

		subprocess.run(["ydotool", "mousemove", "-x", str(self.maxValueMousePosX*2), "-y", str(self.maxValueMousePosY*2)])


	def mouseClickRight(self):
		subprocess.run(["ydotool", "click", "0xC1"])
		

	def mouseClickLeft(self):
		subprocess.run(["ydotool", "click", "0xC0"])
		
		
	def mouseScrollUp(self):
		subprocess.run(["ydotool", "mousemove", "-h", "0", "10"])


	
	def mouseScrollDown(self):
		subprocess.run(["ydotool", "mousemove", "-h", "0", "-10"])
