import random

while True:
    user = input("choose (y/n): ").lower()
    if (user == "y"):
        dice = random.randint(1,6)
        dice1 = random.randint(1,6)
        print(f"({dice},{dice1})")

    elif(user == "n"):
        print("thanks for playing")

    else:
        print("invaid tying")