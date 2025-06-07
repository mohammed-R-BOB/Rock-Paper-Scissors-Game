import random
print("welcome to the paper, rock, scissors game")
help = input("press enter to continue or type 'help' for instructions: ")
# rules
if help.lower() == "help":
    print("the rules are simple: ")
    print("********Rules********")
    print("1) you choose and computer chooses")
    print("2) paper beats rock")
    print("3) rock beats scissors")
    print("4) scissors beats paper")
# computer and player choices
moves = ["rock", "paper", "scissors"]
ascii_art = ["""    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)""", """     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)""", """    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)"""]

pc_turn = random.choice(moves)
# player choice
player_choice = input("enter your choice (rock, paper, scissors): ").lower()
if player_choice not in moves:
    print("invalid choice, please try agian!!")
    exit()
# game logic
if player_choice == pc_turn:
    print("it's a tie, you both choice", player_choice)
    print(ascii_art[moves.index(player_choice)])
    print("computer choice", pc_turn)
    print(ascii_art[moves.index(pc_turn)])
elif player_choice == "rock" and pc_turn == "scissors" or player_choice == "paper" and pc_turn == "rock" or player_choice == "scissors" and pc_turn == "paper":
    print("you choce", player_choice, )
    print(ascii_art[moves.index(player_choice)])
    print("computer choice", pc_turn)
    print(ascii_art[moves.index(pc_turn)])
    print("you win")

else:
    print("you choce", player_choice)
    print(ascii_art[moves.index(player_choice)])
    print("computer choice", pc_turn)
    print(ascii_art[moves.index(pc_turn)])
    print("you lose")

# end of game
print("thanks for playing the game")
