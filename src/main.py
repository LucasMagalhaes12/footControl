from file import Parser
import microcontroller 
import system

micro = microcontroller.Connect()

configFile = Parser("config.cfg")
configFile = configFile.get()

control = system.Control(list(configFile["programs"].values()), list(configFile["sounds"].values()))
control.playSound(0)
control.notify("Microcontroller", "Is Connected")


while True:
	option, value = micro.read().split('#')

	match option:
		
		case "AUDIO":
			# if volume.isdigit():
			control.setVolume(int(value))
			

		case "MOUSE":
			posValue = int(value[1:])
			if value[0] == 'X':
				control.mouseMove(x=posValue)
			
			if value[0] == 'Y':
				control.mouseMove(y=posValue)
				

		case "BUTTON":
			match int(value):
				case 0:
					control.startProgram(0)
					print("start program")

				case 1:
					control.playSound(1)
					print("start audio")

				# case 2:
				# 	control.recordSound()
