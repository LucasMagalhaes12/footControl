import microcontroller 
import system


# Read config for set paths
pathPrograms = [
"/bin/vlc",
"/bin/bash"
]

pathSounds = [
"sounds/notification.wav",
"sounds/sound1.wav",
"sounds/record/audio.wav"
]

system = system.Control(pathPrograms, pathSounds)
#system.getPathSounds()


micro = microcontroller.Connect()
system.playSound(0)
system.notify("Microcontroller", "Is Connected")

cont = 0

while True:
	microRead = micro.read()
#	print(microRead, " - ", cont)
	cont += 1



	if "AUDIO#" in microRead:
		volume = microRead.replace("AUDIO#", '')
		if volume.isdigit():
			pass
			#system.setVolume(int(volume))

	elif "BUTTON#" in microRead:
		output = microRead.replace("BUTTON#", '')

		print(output)
		match output:
			case '0':
				system.startProgram(0)
				print("start program")

			case '1':
				system.playSound(1)
				print("start audio")

			case '2':
				system.recordSound()
			
