#Snake water gun game

print("Welcome to the Snake, Water and Gun GAME")
print("You have 10 chances and the majority times winner will win this GAME")
print("Enter S for Snake W for Water and G for Gun")
import random
list = ["Snake","Water","Gun"]
i = 0
sum = 0
win = 0
lose = 0
while i < 10:
    i += 1
    sum = sum +1
    n = input()
    choice = random.choice(list)
    print(choice)
    if n == choice:
        print("Enter again match tie")
    elif n == "S" and choice == "Water":
        print("You won")
        win += 1
    elif n == "W" and choice == "Gun":
        print("You won")
        win += 1
    elif n == "G" and choice == "Snake":
        print("You won")
        win += 1
    else:
        print("You lost")
        lose += 1
print(sum)
print(win)
print(lose)
if win > lose:
    print("You won the GAME")
else:
    print("You lost the GAME")