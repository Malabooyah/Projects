while True:
	num1 = float(input("Please enter first number: "))
	num2 = float(input("Please enter second number: "))

	op = input("Enter your operation (+,-,*,/,**): ").lstrip()

	if op == '+' :
		result = num1 + num2
	elif op == '-' :
		result = num1 - num2
	elif op == '*' :
		result = num1 * num2
	elif op == '/' :
		if num2 == 0:
			print("Can't divide by zero in this program!")
			result = "undefined"
		else:
			result = num1 / num2
	elif op == '**' :
		result = num1 ** num2
	else:
		print("Invalid operation!")
		result = "undefined"


	print(f"{num1} {op} {num2} = {result}")

	play_again = input("Do another calculation? (y/n): ").lower().strip()
	if play_again != "y" :
		print("Goodbye and Good Riddance!")
		break