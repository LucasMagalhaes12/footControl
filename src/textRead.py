import configparser
import os


class Parser:
	def __init__(self, file):

		self.__file = file 
		self__config = configparser.ConfigParser()
		self.__configuracoes = {}



	def exists(self, file):
		if os.path.exists(file):
			return True
		return False


	def sectionsCapture(self):
		if self.exists(self.__file):
			config.read(file, ecoding="utf-8")
			for section in config.sections():
				self.__configuracoes[section] = dict(config.items(section))	

		else:
			print(f"Error: File {file} not found!")
	

	def write(self, filePath):
		config = configparser.ConfigParser()
		config["programs"] = {
			'vlc':"/bin/vlc",
			"bash":"/bin/bash"
		}

		config["macros"] = {
			"exit":"alt+f4"
		}

		config["geral"] = {
			"theme":"dark"
		}
		
		with open(filePath, 'w', encoding='utf-8') as file:
			config.write(file)

class Text:

	def __init__(self, text):
		self.__text = ""


	def read(path:str):
		try:
			with open(path, 'r', encoding='utf-8') as file:
				for line in file:
					self.__text = line.strip()

		except FileNotFoundError:
			print("File Not Found!")

		except Exception as e:
			print("Error: ", e)


