import random

number_to_guess = random.randint(1,100)

while True:
    try:
        guess = int(input("Enter your number: "))

        if(guess < number_to_guess):
            print("too high")
        elif(guess > number_to_guess):
            print("too low")

        else:
            print("congratulation you guessed correct")
            break

    except ValueError:
        print("invalid value")