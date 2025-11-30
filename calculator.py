#Prevents the program from breaking when incorrect number is entered
def get_number(prompt):
	global last_result
	while True:
		raw = input(prompt).strip().lower()
		#Allows ANS(answer) if a previous result is present
		if raw == "ans" :
			if isinstance(last_result, (int, float)):
				return last_result
			else:
				print("No previous answer saved yet!")
				continue

		#Normal number handling
		try:
			return float(raw)
		except ValueError:
			print("Nahhh, that's not a number. Try again!")

#Prevents the program from breaking when incorrect operation is entered
def get_operation():
	valid_ops = ["+", "-", "*", "/", "**", "%"]
	while True:
		op = input("Enter your operation (+,-,*,/,**,%): ").strip()
		if op in valid_ops:
			return op
		else:
			print("Thats not a valid operation...try again!")

last_result = None

#Calculator Loop
while True:
	num1 = get_number("Please enter first number: ")
	num2 = get_number("Please enter second number: ")

	op = get_operation()

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
	elif op == "%" :
		if num2 == 0:
			print("Can't do that in this one Buddy")
			result = "undefined"
		else:
			result = num1 % num2
	else:
		print("Invalid operation!")
		result = "undefined"


	print(f"{num1} {op} {num2} = {result}")

	# Updates last_result if the value of result is a number
	if isinstance(result, (int, float)):
		last_result = result

	play_again = input("Do another calculation? (y/n): ").lower().strip()
	if play_again != "y" :
		print("Goodbye and Good Riddance!")
		break

