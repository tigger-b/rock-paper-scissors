import random
print("welcome to rock paper scissors")
print("1 rock, 2 paper, 3 scissors")
for i in range(3):
    val = input("Enter your value: ")
    weapons = {'1': "rock", '2': "paper", "3":"scissors"}
    weaponschoice = weapons[val]
    print("you chose " + weaponschoice)

    computer = random.randint(1,3)
    if computer == 1:
        computer = 'rock'
    elif computer == 2:
        computer = 'paper'
    else:
        computer = 'scissors'


    
    ##cheat_wins = {
       ## "rock": "paper",
       ## "scissors": "rock",
       ## "paper": "scissors"
    ##}

    print("Computer chooses " + computer)
    ##print("\u001b[31mYOU LOOSE AGAIN\u001b[37m")

##if computer == weaponschoice:
        ##print("tie")
    if weaponschoice == computer:
        print('tie,you both select same')
    elif weaponschoice == 'rock' and computer == 'paper':
        print('you loose, computer selected paper')
    elif weaponschoice == 'rock' and computer == 'scissors':
        print('you win, computer selected scissors')
    elif weaponschoice == 'paper' and computer == 'scissors':
        print('you loose, computer selected scissors')
    elif weaponschoice == 'paper' and computer == 'rock':
        print('you win, computer selected rock')
    elif weaponschoice == 'scissors' and computer == 'rock':
        print('you loose,computer selected rock')
    elif weaponschoice == 'scissors' and computer == 'paper':
        print('you win, computer selected paper')
    else:
        print('invalid: choose any one -- rock, paper, scissors')
    
