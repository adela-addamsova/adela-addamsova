"""
Creating a program that simulates slot-machine. From four signs randomly generates three signs.
If signs are same, points are won. After every round program asks user if he wants to continue.
"""
import random

signs = ['♥', '♦', '♣', '♠']
points = 0
rounds = 0

next_round = "YES"

while next_round == "YES":
    x = []
    rounds += 1
    for i in range(0, 3):
        x.append(random.choice(signs))
    if x[0] == x[1] == x[2]:
        points += 1
        print("WIN")
    else:
        print("LOSE")
    print(x)
    print(f"You played {rounds} rounds. \nYou have {points} points.")

    next_round = input("To continue write 'YES' ")





