import numpy as np
import json

def add_student(name, surname):
	
	student_dict = {}
	subjects = {'Math':{'marks': [], 'attendance': 0}, \
				'English':{'marks': [], 'attendance': 0}, \
				'Physics':{'marks': [], 'attendance': 0}, \
				'PE':{'marks': [], 'attendance': 0}, \
				'History':{'marks': [], 'attendance': 0}, \
				'Polish':{'marks': [], 'attendance': 0}}

	student_dict.update({'{} {}'.format(surname, name) : subjects})
	return student_dict

def print_diary(class_diary, letter):

	print("\n\t\t\t\t\t\tCLASS: {}".format(letter))

	for i, stud in enumerate(sorted(class_diary[letter].keys()),1):
			print("\n{}. {}: ".format(i,stud))
			print("\t\t\tABSENCE:\t\t\t\tGRADES:")

			for subj in class_diary[letter][stud].keys():
				print ("\t"+subj+"\t\t", end = '')
			
				attendance = class_diary[letter][stud][subj]['attendance']
				marks = class_diary[letter][stud][subj]['marks']
				print("{0}\t\t\t\t\t{1}".format(attendance, marks))
			

def student_average(class_diary, letter, name, surname):
	aver = 0.0
	name_key = surname + " " + name
	temp_subj = class_diary[letter][name_key]
	amount_of_subjects = len(temp_subj.keys())

	for subj in temp_subj.keys():
		aver+=np.average(temp_subj[subj]['marks'])

	aver /= amount_of_subjects
	return aver


def class_average(class_diary, letter):
	average = 0.0
	amount_of_classes = len(class_diary[letter].keys())
	for x in sorted(class_diary[letter].keys()):
		name = x.split(' ')[1]
		surname = x.split(' ')[0]
		average += student_average(class_diary, letter, name, surname)

	average /=amount_of_classes
	return average

def add_grade(class_diary, letter, subject):
	print ("\nWhich student should receive a grade? Type their surname and name")
	student_name = input()

	if student_name not in class_diary[letter].keys():
		if ' ' in student_name:
			student_name2 = student_name.split(' ')[1] + ' ' + student_name.split(' ')[0]
			student_name = student_name2

	while student_name not in class_diary[letter].keys(): # and student_name2 not in class_diary[letter].keys():
		
		print("There is no student named {} in the diary! Type correct surname and name".format(student_name))
		student_name = input()
		if ' ' in student_name:
			if student_name not in class_diary[letter].keys(): 
				student_name2 = student_name.split(' ')[1] + ' ' + student_name.split(' ')[0]
				student_name = student_name2

	print("Type the grade which you want to add: ")
	grade = input()

	while True:
			try:
				grade = int(grade)
			except ValueError:
				print ("Please type a number")
				grade = input()
				continue
			else:
				break

	while grade < 1 or grade > 6 :
		print("The grading scale is between 1 and 6. Type correct grade")
		grade = input()
		grade = int(grade)

	class_diary[letter][student_name][subject]['marks'].append(grade)


def take_attendance(class_diary, letter, subject):
	
	for stud in class_diary[letter].keys():
		print ("Is {} present?".format(stud))
		present = input()
		present = present[0].upper()
		if present == 'N':
			class_diary[letter][stud][subject]['attendance'] += 1

def count_total_attendance(class_diary, letter, student):
	
	total_attendance = 0
	for subj in class_diary[letter][student].keys():
		attendance = class_diary[letter][student][subj]['attendance']
		total_attendance += attendance

	return total_attendance

if __name__ == "__main__":
	
	with open ('data.txt') as json_file:
		class_dict = json.load(json_file)
	
	which_class = 'A'
	print("\nWelcome to an electronic class diary. There are 3 classes: A, B and C.")
	print("Choose a class: ")
	class_choice = input().upper()

	while class_choice not in ['A', 'B', 'C']:
		print("Wrong class! Try again")
		class_choice = input().upper()

	print("Choose a subject: ")
	subject_choice = input()
	subject_choice = subject_choice[0].upper() + subject_choice[1:]
	while subject_choice not in  ['Math', 'English', 'Physics', 'PE', 'History', 'Polish']:
		print("There is no subject called {}".format(subject_choice))
		subject_choice = input()
		subject_choice = subject_choice[0].upper() + subject_choice[1:]
	answer = 'start'
	while(answer != 'q'):

		print("\nWhat do you want to do? Type a number of a proper option.")
		print("1. Add new student.\n2. Take attendance.\n3. Add grade.")
		print("4. See the diary of a class.\n5. Get average score of a student.")
		print("6. Get average score of a class.\n7. Get total absence of a student.")
		print("8. Change a subject.\n9. Change a class.\n10. Quit.")
		choice = input()
		while True:
			try:
				choice = int(choice)
			except ValueError:
				print ("Please type a number")
				choice = input()
				continue
			else:
				break
		while choice < 1 or choice > 10:
			print("Wrong number! Try again")
			choice = input()
			choice = int(choice)

		if choice == 1:
			if len(class_dict[class_choice]) > 30:
				print("Class {} is already full!".format(class_choice))
			else:
				print("Type name of a new student:")
				name = input()
				print("Type surname of a new student:")
				surname = input()
			
				class_dict[class_choice].update(add_student(name, surname))


		elif choice == 2:
			take_attendance(class_dict, class_choice, subject_choice)

		elif choice == 3:
			add_grade(class_dict, class_choice, subject_choice)

		elif choice == 4:
			print_diary(class_dict, class_choice)

		elif choice == 5:
			print("Whose average score do you want to know?")
			print("Type the name:")
			name = input()
			print("Type the surname:")
			surname = input()
			name_and_surname = surname + " " + name
			while name_and_surname not in class_dict[class_choice]:
				print("There is no student {}. Please type correct surname.".format(name_and_surname))
				surname = input()
				print("Type correct name.")
				name = input()
				name_and_surname = surname + " " + name

			average_score = student_average(class_dict, class_choice, name, surname)
			print("{0} {1} average score is {2:.2f}".format(name, surname, average_score))

		elif choice == 6:
			average_score = class_average(class_dict, class_choice)
			print("Class {0} average score is {1:.2f}".format(class_choice, average_score))

		elif choice == 7:
			print("Whose amount of absence do you want to know?")
			print("Type the surname:")
			surname = input()
			print("Type the name:")
			name = input()

			name_and_surname = surname + " " + name
			while name_and_surname not in class_dict[class_choice]:
				print("There is no student {}. Please type correct surname.".format(name_and_surname))
				surname = input()
				print("Type correct name.")
				name = input()
				name_and_surname = surname + " " + name

			total_absence = count_total_attendance(class_dict, class_choice, surname+" "+name)
			print("Total {} {} absence is {}".format(name, surname, total_absence))

		elif choice == 8:
			print("Type name of the wanted subject: ")
			subject_choice = input()
			subject_choice = subject_choice[0].upper() + subject_choice[1:]
			while subject_choice not in  ['Math', 'English', 'Physics', 'PE', 'History', 'Polish']:
				print("There is no subject called {}".format(subject_choice))
				subject_choice = input()
				subject_choice = subject_choice[0].upper() + subject_choice[1:]

		elif choice == 9:
			print("Choose a class: ")
			class_choice = input().upper()

			while class_choice not in ['A', 'B', 'C']:
				print("Wrong class! Try again")
				class_choice = input().upper()
		else:
			answer = 'q'

		with open('data.txt', 'w') as outfile:
					json.dump(class_dict, outfile)




