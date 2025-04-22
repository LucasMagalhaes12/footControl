import configparser
import os

DEFAULT = {}

DEFAULT["programs"] = {}

DEFAULT["sounds"] = {}

DEFAULT["macros"] = {}

DEFAULT["mouse"] = {
	"acceleration":"on",
	"velocity_x":10,
	"velocity_y":10
}

DEFAULT["geral"] = {
	"theme":"dark"
}


def exists(path):
	if os.path.exists(path):
		return True
	return False


class Parser:
	def __init__(self, filePath):

		self.__filePath = filePath 
		self.__parser = configparser.ConfigParser()
		self.__parser.read_dict(DEFAULT)
		self.__config = {}
		self.__read()

	def __read(self):
		if not exists(self.__filePath):
			print(f"Error: File {self.__filePath} not found!")
			self.__create()
			
		print("Reading file...")
		self.__parser.read(self.__filePath, encoding="utf-8")
		for section in self.__parser.sections():
			self.__config[section] = dict(self.__parser.items(section))	


	def __create(self):
		print("Creating config file...")
		with open(self.__filePath, 'w', encoding='utf-8') as file:
			self.__parser.write(file)


	def get(self):
		return self.__config



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


