import random
player_name = input("Player 1 enter your name: ").strip().title()

while True:
	try:
		win_goal = int(input(f"Hi {player_name}, how many wins to finish the match today?"))
		if win_goal > 0:
			break
		else:
			print("Please enter a positive number.")
	except ValueError:
		print("Invalid number. Try again.")


#Getting the choices
def get_choices():
	options = ["rock", "paper", "scissors"]
	player_choice = ""
	# keep asking until player types valid response

	while player_choice not in options:
		player_choice = input ("Enter a choice (rock, paper, scissors): ").lower().strip()
		if player_choice not in options:
			print("Not a valid choice. Try again!")
	
	computer_choice = random.choice(options)
	return {"player": player_choice, "computer": computer_choice}
	
#Win Conditions
def check_win(player, computer):
	print(f"You chose {player}, Computer chose {computer}")
	if player == computer:
		print("It's a tie!")
		return "tie"
	# Player Chooses Rock
	elif player == "rock":
		if computer == "scissors":
			print ("Rock crushes scissors! Win :)")
			return "player"	
		else:	
			print("Paper covers rock! You lose.")
			return "computer"
	
	# Player Chooses Paper
	elif player == "paper":
		if computer == "scissors":
			print("Scissors slice Paper! You lose.")
			return "computer"
		else:	
			print("Paper covers rock! Win :)")
			return "player"

	# Player Chooses Scissors
	elif player == "scissors":
		if computer == "rock":
			print("Rock crushes scissors! You lose.")
			return "computer"
		else:	
			print("Scissors slice Paper! Win :)")
			return "player"

#Replay logic
def ask_replay():
	while True:
		answer = input("Play again? (y/n)").lower().strip()
		if answer in ["y","n"]:
			return answer
		else:
			print( "Bro… that wasn’t even close. Try typing 'y' or 'n'" )

#Keeps a running score
scores = {'player':0, "computer": 0, "tie": 0}

#Keeps the game on a loop
while True:
	choices = get_choices()
	result = check_win(choices["player"], choices["computer"])
	if result in scores:
		scores[result] += 1
	#Scoreboard
	print("scoreboard")
	print(f"{player_name}: {scores['player']} | Computer: {scores['computer']} | Ties: {scores['tie']}")
	
	print (result)

#Check who wins best of input win total
	if scores["player"] == win_goal:
		print( f"\nCongratulations {player_name.title()}! First to reach the goal of {win_goal} wins!")
		break
	if scores["computer"] == win_goal:
		print( f"\nYou lost to the CPU? Computer has reached the goal of {win_goal} wins!")
		break

#Replay the game
	play_again = ask_replay()
	if play_again == 'y':
		scores = {'player': 0, 'computer': 0, 'tie': 0}
		print("\nNew Round starting! Good Luck!\n")
	else:
		print("\nGoodbye.. :/")
		print("\nFinal Score")
		print(f"{player_name}: {scores['player']} | Computer: {scores['computer']} | Ties: {scores['tie']}")
		break

