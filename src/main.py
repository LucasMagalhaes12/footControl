
import microcontroller 
import system

micro = microcontroller.Connect()

control = system.Control()
control.notify("Microcontroller", "Is Connected")


while True:
	option, value = micro.read().split('#')
	print(option, value)
	
	match option:

		case "MOUSE":
			posValue = int(value[1:])
			if value[0] == 'X':
				control.mouseMove(x=posValue)
			
			if value[0] == 'Y':
				control.mouseMove(y=(posValue * -1))
				

		case "BUTTON":
			match int(value[0]):
				case 0:
					control.mouseClickRight(int(value[1]))

				case 1:
					control.mouseClickLeft(int(value[1]))

				case 2:
					control.mouseScrollUp()

				case 3:
					control.mouseScrollDown()
