import random

# ASCII Art for dice faces
dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

# Function to roll the dice
def roll_dice(num_rolls):
    dice = [random.randint(1, 6) for _ in range(num_rolls)]
    return dice

# Function to display dice art side by side
def display_dice(dice):
    print("\nYour Dice Rolls:")
    for h in range(5):  # 5 lines for each dice
        for d in dice:
            print(dice_art[d][h], end="  ")  # Display side by side
        print()  # Move to the next line after printing one row for all dice

# Main program logic
def main():
    while True:
        # Input validation for dice rolls
        while True:
            try:
                rolls = int(input("How many dice would you like to roll? (1-10): "))
                if 1 <= rolls <= 10:
                    break
                else:
                    print("Please enter a number between 1 and 10.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        # Roll the dice
        dice = roll_dice(rolls)

        # Display dice art
        print("\n" + "="*30)
        display_dice(dice)
        print("="*30)

        # Calculate and display the total
        total = sum(dice)
        print(f"\nTotal value of all dice: {total}")

        # Option to roll again
        roll_again = input("\nWould you like to roll again? (y/n): ").lower()
        if roll_again != 'y':
            print("Thanks for playing! Goodbye!")
            break

# Run the program
if __name__ == "__main__":
    main()
