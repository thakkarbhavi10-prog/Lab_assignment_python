#Dice Rolling Simulator Project
# Description: Students must simulate the rolling of dice using random number generation.
# They must also design a user interface for rolling the dice and displaying results
# that includes error handling for unexpected inputs or errors during the simulation.
# Skills Required: Random number generation, loops, user input handling.
# Drawbacks: Limited scope.
# Tips: Utilize the "random" module to generate random numbers corresponding to dice faces


import random

def roll_dice(total_dice):
    numbers = []
    for _ in range(total_dice):
        numbers.append(random.randint(1, 6))
    return numbers

print("Welcome to Dice Rolling Simulator")

while True:
    user = input("\nEnter how many dice you want to roll (or press 'q' to quit): ")

    if user.lower() == 'q':
        print("Thank you for playing!")
        break

    try:
        dice_count = int(user)

        if dice_count <= 0:
            print("Error: Please enter a number greater than 0.")
        elif dice_count > 100:
            print("Error: Too many dice! Please enter a smaller number.")
        else:
            result = roll_dice(dice_count)
            print("Dice values:", result)
            print("Total:", sum(result))

    except ValueError:
        print("Invalid input! Please enter a valid number.")