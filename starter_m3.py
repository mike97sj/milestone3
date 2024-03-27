
# [Michael Schmitt]
# [3/23/2024]
# [python 3.10.3]
# [Milestone 3]


# 1. You need to create a new Python file named utilities.py and place custom functions inside. We will call those functions into this script.
# Import the utilities file 👇
import utilities 

# 2. The transformers need to be moved to a new text file. We will read the code from the file to select transformers.
# Import the transformers.txt file 👇
transformers = utilities.importer('transformers.txt')

#####  Attacks List #####
attack = ['punch', 'kick', 'throw']

# 3. Use the utilites to randomly pick transformers for player and opponent 👇
player = utilities.randomized_pick(transformers)
opponent = utilities.randomized_pick(transformers)

# 4. Add a while loop so that the transformers are not the same 👇
while player == opponent or opponent == player:
    utilities.randomized_pick(transformers)

##### Announce Game Start #####
    print("Welcome to the Paper, Rock, Scissors: Transformers Edition! The battle awaits!")
    print(f"{player} has challenged {opponent} in one on one combat!")

##### Initialize Scoring Variables ##### 
pscore = 0
oscore = 0

# Use what you created from Milestone 2 OR Create a loop that will run UNTIL either the player or opponent scores 5 points
# Write your code below this row 👇
while pscore < 5 or oscore < 5:

    # 5. Exception - Add a while True and exception. 
    # Hint: the player attack variable should allow the user to pick between the different attack options by pressing 1, 2 or 3 
    # Write your code below this row 👇
    while attack is True:
        prompt = print('Pick a number, either 1, 2, or 3')
        attack_pick = input(prompt)
        
    # 6. Player only - Create an if/elif statement to set the number entry to the correct attack.
    # Write your code below this row 👇
    if player == input('1'):
        attack = 'punch'
    elif player == input('2'):
        attack = 'kick'
    elif player == input('3'):
        attack = 'throw'

    # The program randomly picks the attack for the opponent
    pattack = utilities.randomized_pick(attack)
    oattack = utilities.randomized_pick(attack)
    

    # 7. Add a while loop so that the attacks are not the same. Use the utilities module.
    while pattack == oattack:
        utilities.randomized_pick(attack)
        break 

    # Announcing the competitors and attacks 
    print(f'{player} attacks with {pattack}, while {opponent} attacks with {oattack}')


    # Use the scoring system from Milestone 2 OR Create a new one for this week.
    # Write your code below this row 👇
    if pattack == oattack:
        print("It's a tile! No points awarded.")
    elif (pattack == 'pulse cannon' and oattack == 'ion grenade') or \
         (pattack == 'ion grenade' and oattack == 'plasma shield') or \
         (pattack == 'plasma shield' and oattack == 'pulse cannon'):
        pscore += 1
        print(f'{player} wins this round!')
    break
print('Game Over!')


    # Once the game is over and someone scored 5 points:
    # You may borrow code used for Milestone 2 for this step.
    # 8. Print a string that includes the player and opponent names along with the final score to the game.
    # Write your code below this row 👇
if pscore > oscore:
    print(f'{player} has defeated {opponent}! The final score is {pscore} - {oscore}')
else:
    print(f'{player} has defeated {opponent}! The final score is {pscore} - {oscore}')

