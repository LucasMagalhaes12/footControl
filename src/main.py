import microcontroller 
import subprocess

pathNotification = "sounds/notification.wav"
pathSound = "sounds/sound1.wav"

arduino = microcontroller.Connect();
subprocess.run(["notify-send", "Arduino", "Connected"])
subprocess.run(["aplay", pathNotification])

cont = 1

programs = [False]

while True:
	arduinoRead = arduino.read()

	print(arduinoRead, " - ", cont)
	cont += 1
	
	if "AUDIO#" in arduinoRead:
		volume = int(arduinoRead.replace("AUDIO#", ''))
		volume = str((volume // 100) * 10)
		print("--------"+volume)
		subprocess.run(["amixer", "-D", "pulse", "set", "Master", volume+'%'])

	else:
		match arduinoRead:
			case "bt1":
				if not programs[0]:
					program = subprocess.Popen("/bin/vlc")
					programs[0] = True
				
				if program.poll() != None:
					program = subprocess.Popen("/bin/vlc")

			case "bt2":
				subprocess.Popen(["aplay", pathSound])

