import random

def banker_roulette():
    num_participants = int(input("Enter the number of participants: "))

    # create empty list to store names
    names = []

    # collect names from user
    for _ in range(num_participants):
        name = input("Enter a name: ")
        names.append(name)

    #randomly pick a name from the list
    chosen_one = names[random.randint(0, len(names) -1)]

    print(f"The chosen one is {chosen_one}!")

banker_roulette()