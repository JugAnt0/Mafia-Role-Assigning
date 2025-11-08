import random
import time
import sys

print("Welcome to Mafia!")

while True:
    num_players = int(input("Enter number of players (4-10): "))

    if not (4 <= num_players <= 10):
        print("Invalid number of players. Please enter a number between 4 and 10.")
        continue

    print("Let's begin the game!")
    input("Press Enter to assign roles...")
    time.sleep(1)

    # Create player labels
    players = [f"Player {i+1}" for i in range(num_players)]

    # Create roles
    roles = ["Mafia", "Detective", "Doctor"] + ["Villager"] * (num_players - 3)
    random.shuffle(roles)

    # Assign roles to players
    player_roles = dict(zip(players, roles))

    # Secretly reveal roles to each player
    for player in players:
        print(f"\n{player}, your role is: {player_roles[player]}")
        input("Press Enter when you're done (make sure nobody else is looking)...")
        print("\n" * 50)  # Clear-ish screen

    print("All roles have been assigned. Let the game begin!")
    time.sleep(2)
    sys.exit()
