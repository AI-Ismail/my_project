import random

top_of_range = input("Type a number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("please type a number larger than 0 next time")
        quit()
else:
    print("please type a number larger than 0 next time")
    quit()
random_number = random.randrange(top_of_range)
gasses = 0
while True:
    gasses += 1
    user_guess = input("make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("please type a number larger than 0 next time")
        continue
    if user_guess == random_number:
        print("you got it")
        break
    elif user_guess > random_number:
        print("You are above the number")
    else:
        print("You are below the number")
print("yoy got it in", gasses, "gasses")


print("hello World")
