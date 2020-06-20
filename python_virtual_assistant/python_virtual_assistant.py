# Library..........................................
import speech_recognition
import pyttsx3
from datetime import date, datetime
# Init.............................................
robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""

while True:
	# Listening........................................
	with speech_recognition.Microphone() as mic:
		print("Python VA: I'm listening..")
		audio = robot_ear.listen(mic)
	print("Python VA: ...")
	try:
		you = robot_ear.recognize_google(audio)
	except:
		you = ""
	print("You : " + you)
	# AI...............................................
	if you == '':
		robot_brain = "I can't hear you, try again !"
	elif 'hello' in you:
		robot_brain = 'Hi...'
	elif "time" in you:
		robot_brain = datetime.now().strftime("%H hours, %M minutes, %S seconds")

	elif "today" in you:
		robot_brain = date.today().strftime("%B %d, %Y")
	elif "bye" in you:
		robot_brain = "See you soon !"
		print("Python VA: " + robot_brain)
		# Speech............................................
		robot_mouth.say(robot_brain)
		robot_mouth.runAndWait()
		break
	else:
		robot_brain = "I'm fine, thank you and you !"
	print("Python VA: " + robot_brain)
	# Speech............................................
	robot_mouth.say(robot_brain)
	robot_mouth.runAndWait()
