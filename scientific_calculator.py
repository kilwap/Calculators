# This is scientific calculator
import math


# infinite loop keeps us in the program menu untili we want to end the program
while True:
	#printing menu that allows user to chose the operation
	print("\nChose the math operation:\n\n0 - Addition\n1 - Substraction\n2 - Multiplication\n3 - Division\n4 - Modulo\n5 - Rasing to a power\n6 - Square root\n7 - Logarithm\n8 - Sine\n9 - Csine\n10 - Tangent\n\nx - for exit\n")
	
	
	oper = input("\nYour option from the menu: ")#Variable that saves the operation chosed by user
	
	#Addition
	if oper == "0":
		#Try function check is user provided us an number
		try:
			val1 = float(input("\nFirst value: "))#The variable storing the first value converted from string to float
		except ValueError:
			print("\nThat is not a number, try again! ")
			continue
		try:
			val2 = float(input("\nSecond value: "))#The variable storing the second value converted from string to float
		except ValueError:
			print("\nThat is not a number, try again! ")
			continue
		
		print("\nThe result is: " + str(val1 + val2) + "\n")#Printing the result of operation
		
		#Going back to main menu or exiting the program
		back = input('\nGo back to the main menu? (y/n)')
		if back == 'y':
			continue
		else:
			break
		
	#Substraction
	elif oper == "1":
		try:
			val1 = float(input("\nFirst value: "))
		except ValueError:
			print("\nThat is not a number, try again! ")
			continue
		try:
			val2 = float(input("\nSecond value: "))
		except ValueError:
			print("\nThat is not a number, try again! ")
			continue
			
		print("\nThe result is: " + str(val1 - val2) + "\n")
		
		back = input('\nGo back to the main menu? (y/n)')
		if back == 'y':
			continue
		else:
			break
			
	#Multiplication
	elif  oper == "2":
		try:
			val1 = float(input("\nFirst value: "))
		except ValueError:
			print("\nThat is not a number, try again! ")
			continue
		try:
			val2 = float(input("\nSecond value: "))
		except ValueError:
			print("\nThat is not a number, try again! ")
			continue
			
		print("\nThe result is: " + str(val1 * val2) + "\n")
		
		back = input('\nGo back to the main menu? (y/n)')
		if back == 'y':
			continue
		else:
			break
			
	#Division
	elif oper == "3":
		try:
			val1 = float(input("\nFirst value: "))
		except ValueError:
			print("\nThat is not a number, try again! ")
			continue
		try:
			val2 = float(input("\nSecond value: "))
			if val2 == 0:  #Checking if user is entering valid number
				print("\nYou can not divide by zero!")
				continue
		except ValueError:
			print("\nThat is not a number, try again! ")
			continue
			
		print("\nThe result is: " + str(val1 / val2) + "\n")
		
		back = input('\nGo back to the main menu? (y/n)')
		if back == 'y':
			continue
		else:
			break
	
	#Modulo
	elif oper == "4":
		try:
			val1 = float(input("\nFirst value: "))
		except ValueError:
			print("\nThat is not a number, try again! ")
			continue
		try:
			val2 = float(input("\nSecond value: "))
		except ValueError:
			print("\nThat is not a number, try again! ")
			continue
			
		print("\nThe result is: " + str(val1 % val2) + "\n")
		
		back = input('\nGo back to the main menu? (y/n)')
		if back == 'y':
			continue
		else:
			break
	
	#Rising to a power
	elif oper == "5":
		try:
			val1 = float(input("\nEnter the base: "))
		except ValueError:
			print("\nThat is not a number, try again! ")
			continue
		try:	
			val2 = float(input("\nEnter the power: "))
		except ValueError:
			print("\nThat is not a number, try again! ")
			continue
			
		print("\nThe result is: " + str(math.pow(val1, val2)) + "\n")
		
		back = input('\nGo back to the main menu? (y/n)')
		if back == 'y':
			continue
		else:
			break
			
	#Square root
	elif oper == "6":
		try:
			val1 = float(input("\nEnter the value for extracting the square root: "))
			if val1 < 0:  #Checking if user is entering valid number
				print("\nYou have to enter positive number in this case!")
				continue
		except ValueError:
			print("\nThat is not a number, try again! ")
			continue
			
		print("\nThe result is: " + str(math.sqrt(val1)) + "\n")
		
		back = input('\nGo back to the main menu? (y/n)')
		if back == 'y':
			continue
		else:
			break
	
	#Logarithm
	elif oper == "7":
		try:
			val1 = float(input("\nEnter the value for calculating the logarithm: "))
			if val1 <= 0: #Checking if user is entering valid number
				print("\nThe nnumber must be greater rhan zero!")
				continue
		except ValueError:
			print("\nThat is not a number, try again! ")
			continue
		try:
			val2 = float(input("\nEnter the value for the logarithm base: "))
			if val2 <= 0 or val2 == 1: #Checking if user is entering valid number
				print("\nThe nnumber must be greater rhan zero and diffrent from one!")
				continue
		except ValueError:
			print("\nThat is not a number, try again! ")
			continue
			
		print("\nThe result is: " + str(math.log(val1, val2)) + "\n")
		
		back = input('\nGo back to the main menu? (y/n)')
		if back == 'y':
			continue
		else:
			break
	
	#Sine
	elif oper == "8":
		try:
			val1 = float(input("\nEnter the value (in degrees) for calculating the sine: "))
		except ValueError:
			print("\nThat is not a number, try again! ")
			continue
			
		print("\nThe result is: " + str(math.sin(math.radians(val1))) + "\n")
		
		back = input('\nGo back to the main menu? (y/n)')
		if back == 'y':
			continue
		else:
			break
	
	#cosine
	elif oper == "9":
		try:
			val1 = float(input("\nEnter the value (in degrees) for calculating the cosine: "))
		except ValueError:
			print("\nThat is not a number, try again! ")
			continue
			
		print("\nThe result is: " + str(math.cos(math.radians(val1))) + "\n")
		
		back = input('\nGo back to the main menu? (y/n)')
		if back == 'y':
			continue
		else:
			break
			
	#Tangent
	elif oper == "10":
		try:
			val1 = float(input("\nEnter the value (in degrees) for calculating the tangent: "))
		except ValueError:
			print("\nThat is not a number, try again! ")
			continue
			
		print("\nThe result is: " + str(math.tan(math.radians(val1))) + "\n")
		
		back = input('\nGo back to the main menu? (y/n)')
		if back == 'y':
			continue
		else:
			break
			
	elif oper == "x":
		break
	#Handling invalid options
	else:
		print("\nInvalid option!")
		continue
#End of the program