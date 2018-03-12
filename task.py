# Class diary  
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities. 
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing) 
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.
#If you can thing of any other features, you can add them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)

class classDiary:

	def __init__(self, name="noName", surname="noName", grade=1.0, attendance = 0):
		self.number_of_students=0;
		self.cDiary = {}
		self.cDiary['{} {}'.format(name, surname)] = [grade, attendance]

	def print_class_diary(self):
		print ("This is the diary of the class:")
		print ("All the information is in the following order:")
		print ("name and surname, grade, attendance")
		print (self.cDiary)

	def add_new_student(self, name, surname, grade, attendance):
		self.cDiary.update({'{} {}'.format(name, surname) : [grade, attendance]})
		self.number_of_students+=1

	def average(self):
		self.sum = 0.0

		for x in range(self.number_of_students):
			self.sum += self.cDiary[x][0]
		self.av = self.sum / self.number_of_students
		return self.av

	def totalAttendance(self):
		self.attendance_sum = 0

		for x in range(self.number_of_students):
			self.attendance_sum += self.cDiary[x][1]
		return self.attendance_sum




diary = classDiary("Ann", "Smith", 3.0, 2)
diary.print_class_diary()

diary.add_new_student("Tom", "Baker", 4.5, 5)
diary.print_class_diary()







