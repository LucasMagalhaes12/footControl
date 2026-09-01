import subprocess

# pyautogui.PAUSE = 0.1
# pyautogui.FAILSAFE = True

class Control:
	def __init__(self):
		self.maxValueMousePosX = self.maxValueMousePosY = 0


	def notify(self, title:str, comment:str):
		pyautogui.alert(text=comment, title=title)


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

		# subprocess.run(["xdotool", "mousemove_relative", "--", str(self.maxValueMousePosX*2), str(self.maxValueMousePosY*2)])
		pyautogui.move(self.maxValueMousePosX*2, self.maxValueMousePosY*2)


	def mouseClickRight(self):
		pyautogui.click(button='left')
		

	def mouseClickLeft(self):
		pyautogui.click(button='right')


	def mouseScrollUp(self):
		pyautogui.scroll(10)


	
	def mouseScrollDown(self):
		pyautogui.scroll(-10)