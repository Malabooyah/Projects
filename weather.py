
def get_diagnosis(weather):
	if weather >= 80:
		return 'hot'
	elif weather >= 55 and weather < 80:
		return 'warm'
	else:
		return 'cold'
while True: 
	weather = int(input("What is the temp in *F today?: "))

	print(f"It is {get_diagnosis(weather)} as fuck out today man!")
