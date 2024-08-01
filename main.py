import random

def banker_roulette():
    num_participants = int(input("Enter the number of participants: "))

    # create empty list to store names
    names = []

    for _ in range(num_participants):
        name = input("Enter a name: ")
        names.append(name)