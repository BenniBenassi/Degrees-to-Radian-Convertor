# 1. Write a Python program to convert degree to radian. Also the other way (radian to degree).
# Note : The radian is the standard unit of angular measure, used in many areas of mathematics. 
# An angle's measurement in radians is numerically equal to the length of a corresponding arc of a unit circle; 
# one radian is just under 57.3 degrees (when the arc length is equal to the radius).
# Degree × π/180
# Test Data:
# Degree : 15
# Expected Result in radians: 0.2619047619047619

# 2. Write a Python program to convert radian to degree. Go to the editor 
# Test Data:
# Radian : .52
# Expected Result : 29.781818181818185

import math
import os
import sys



os.system('cls')

def main_loop():
	cont = input('\nWould you like to continue? y/n\n> ')
	if cont.lower() == 'y':
		os.system('cls')
		menu_system()
	else:
		print('Thanks for using this utility')

def menu_system():	
	menu_choice = 0
	print('\nPlease type your selection and then press **ENTER**\n')
	while menu_choice not in (1,2):
		try:
			menu_choice = int(input("\n1 for Degree > Radian\n2 for Radian > Degree\n> "))
		except(ValueError, TypeError, UnboundLocalError):
   			print("\nError occurred, please ensure you type a number\n")
		if menu_choice == 1:
					radian()
		if menu_choice == 2:
					degree()
		else:
			print("\nPlease try again and choose the correct number\n")

def radian():
	try:
		degree1 = float(input("\nPlease enter the degree\n> "))
	except(ValueError, TypeError, UnboundLocalError):
		print("\nError occurred, please ensure you type a number\n")
	radian1 = degree1 * math.pi/180
	print("\nThe radian is equal to:\n" + str(radian1))
	main_loop()
	

def degree():
	try:
		radian2 = float(input("\nPlease enter the radian\n> "))
	except(ValueError, TypeError, UnboundLocalError):
		print("\nError occurred, please ensure you type a number\n")
	degree2 = radian2 * 180/math.pi
	print("\nThe degrees are equal to:\n" + str(degree2))
	main_loop()

os.system('cls')
menu_system()



