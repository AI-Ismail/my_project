print("welcome to my computer")
playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()    
print("okay! let's play game")
score = 0

answer = input("What Does CNG stand for? ")
if answer.lower() == "compressed natural gas":
    print("You got Correct!")
    score += 1
else:
    print("wrong asnwer")
answer = input("What Does RAM stand for? ")
if answer.lower() == "random access memory":
    print("You got Correct!")
    score += 1
else:
    print("wrong asnwer")
answer = input("What Does gpu stand for? ")
if answer.lower() == "graphics processing unit":
    print("You got Correct!")
    score += 1
else:
    print("wrong asnwer")
answer = input("What Does gps? ")
if answer.lower() == "global positioning system":
    print("You got Correct!")
    score += 1
else:
    print("wrong asnwer")
print("You got", str(score), "correct quetions")
print("You got", str(score / 4 * 100), ("%."))