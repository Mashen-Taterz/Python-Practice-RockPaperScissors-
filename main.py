import random


def get_choices():
  player_choice = input("Enter a choice (rock, paper, scissors): ")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  choices = {"Player": player_choice, "Computer": computer_choice}
  return choices


def check_win(player, computer):
  print(f"You chose {player}, computer chose {computer}")
  if player == computer:
    return "Its a tie!"
  elif player == "rock": 
    if computer == "scissors":
      return "You win!"
  elif player == "paper": 
    if computer == "rock":
      return "You win!"
  elif player == "scissors": 
    if computer == "paper":
      return "You win!"
  else:
    return "Loser!"

choices = get_choices()
result = check_win(choices["Player"], choices["Computer"])
print(result)


  
