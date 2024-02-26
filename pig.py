import random


def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll


while True:
    players = input("Enter the number of player (1-4): ")
    if players.isdigit():
        players = int(players)
        if 1 <= players <= 4:
            break
        else:
            print("must be between 2 - 4 players. ")
    else:
        print("Invalid, try again")


max_score = 50
player_score = [0 for _ in range(players)]

while max(player_score) < max_score:
    should_roll = input("Would you like to roll (y) : ")
