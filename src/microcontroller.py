import serial

class Connect():
	def __init__(self, port:str="/dev/ttyUSB0", baudrate:int=9600):

		while True:

			try:
				self._arduino = serial.Serial(port, baudrate)
				print("Arduino Connected!")
				break

			except:
				print("not connected")
				pass


	def read(self):
		msg = str(self._arduino.readline())	
		self._arduino.flush()
		return msg[2:-5]


	def send(self, message:str):
		self._arduino.write(message.encode())


	def isConnect(self):
		pass


