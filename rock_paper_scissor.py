import random 

'''
rock = 1
paper = 0
scissor = -1

'''
emoji = {"r": "rock", "p": "paper","s":"scissor"}
choices = ("r","p","s")
while True:
    user_choice = input("rock,paper, or scissors? (r/p/s): ").lower()
    if user_choice not in choices:
        print("invaid choices")

    computer_choice = random.choice(choices)

    print(f"you chose {emoji[user_choice]}")
    print(f"computer chose {emoji[computer_choice]}")

    if(user_choice == computer_choice):
        print("tie")
    elif(
        (user_choice == "r" and computer_choice == "s")or
        (user_choice == "p" and computer_choice == "r")or
        (user_choice == "s" and computer_choice == "p")):
        print("you won")
    else:
        print("you lose")

    should_continue = input("Enter your (y/n): ").lower()
    if(should_continue == "n"):
        break

 
