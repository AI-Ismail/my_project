import numpy as np

name = input("Type your Name: ")
print("Welcome to ", name, "to this adventure game")
answer = input(
    "you are on dangours road and you have to decide either you right/left which way you go? "
).lower()
if answer == "left":
    answer = input("You came to forest you walk to walk and swim to swim:")
    if answer == "swim":
        print("You swam accors and eaten by alligator ")
    elif answer == "walk":
        print("you walk many miles you ran out of water and you lost a game")
    else:
        print("not a valid option")

elif answer == "right":
    answer = input("you came to bridge you want cross it or head back it(cross/back)")
    if answer == "back":
        print("you go back and lose it")
    elif answer == "cross":
        print("you fall down from bridge and drowned in river and die you lose game")
    else:
        print("not valid option")

    answer = input("you want alive again you have to go back learn to swim (yes/no)")
    if answer == "yes":
        print("you alive now you cross bridge and swim and you win the game ")
    elif answer == "no":
        print("you die again")
    else:
        print("your option not a vaild")


else:
    print("not a valid option")
