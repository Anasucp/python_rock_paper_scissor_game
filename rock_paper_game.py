import random





while True:


	user_choice = input("Select (Rock/Paper/Scissor):")

	print("|---------------------------------------|")

	possible_outcome = ['rock' , 'paper' , 'scissor']

	computer_choice = random.choice(possible_outcome)

	print ("You choose:" ,user_choice)
	print ("&& Computer choose:" , computer_choice)

	print("|---------------------------------------|")
	print("RESULT:")


	if user_choice == computer_choice:
		print ("You Both Chose: ",user_choice ,"So Its Tie")

	elif user_choice == "rock":
		if computer_choice == "paper":
			print ("Paper Cover Rock So You Lose!")
		elif computer_choice =="scissor":
			print ("Rock Break The Scissor So You Win!")

	elif user_choice == "paper":
		if computer_choice == "rock":
			print ("Paper Cover Rock So You Win!")
		elif computer_choice =="scissor":
			print ("Scissor Cuts The Paper So You Lose!")

	elif user_choice == "scissor":
		if computer_choice == "paper":
			print ("Scissor Cuts The Paper So You Win!")
		elif computer_choice =="rock":
			print ("Rock Break The Scissor So You Lose!")


	print("|---------------------------------------|")


	
	Play_again = input("You Want to play Again (Y/N):")
	if Play_again.lower() != "y":
		print ("Thanks For Playing")
		break
			
	


