import pyttsx3
from datetime import date, datetime
robot_brain = datetime.now().strftime("%H hours, %M minutes, %S seconds")

robot_mouth = pyttsx3.init()
robot_mouth.say(robot_brain)
robot_mouth.runAndWait()