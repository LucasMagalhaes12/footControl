import subprocess


class Control:

	def __init__(self, path_programs:list, path_sounds:list):
		self.__pathPrograms = path_programs
		self.__pathSounds = path_sounds 

		self.__process = [None for _ in self.__pathPrograms]

		self.__lastVolume = 0


	def notify(self, title:str, comment:str):
		subprocess.run(["notify-send", title, comment]) 

	
	def playSound(self, id:int):
		subprocess.Popen(["aplay", self.__pathSounds[id]])
	
	
	def startProgram(self, id):
		print(self.__process)

		if self.__process[id] == None or self.__process[id].poll() != None:
			self.__process[id] = subprocess.Popen(self.__pathPrograms[id])
		
		"""	
		elif self.__process[id].poll() != None:
			self.__process[id] = subprocess.Popen(self.__pathPrograms[id])
		"""
	

	def setVolume(self, volume:int):
			volume = str((volume // 100) * 10)
			print("--------"+volume)
			if self.__lastVolume != volume:
				subprocess.run(["amixer", "-D", "pulse", "set", "Master", volume+'%'])
				self.__lastVolume = volume


	def getPathPrograms(self):
		for i, path in enumerate(self.__pathPrograms):
			print(f"{i} {path}/n")
		print()
	

	def getPathSounds(self):
		for i, path in enumerate(self.__pathSounds):
			print(f"{i} {path}/n")
		print()


	def recordSound(channels:int=2, rate:int=48000, time:int=5, output_path:str="sounds/record"):
		#subprocess.Popen(["arecord", "-c", channels, "-r", rate, "-d", time, "sounds/record/audio.wav"])
		subprocess.run(["arecord", "-f", "cd", "-d", "5", "sounds/record/audio.wav"])
		print("finish record")


