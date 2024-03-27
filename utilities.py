import random

# allows any list to be passed into the function
# L is a variable representing a list
def randomized_pick(L):
    return random.choice(L)

# opens a given text file and reads the file line by line
def importer(T):
    with open(T, 'r') as file:
        return file.read().splitlines()
    




