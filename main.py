print("welcome to rock paper scissors")
print("1 rock, 2 paper, 3 scissors")
for i in range(3):
    val = input("Enter your value: ")
    weapons = {'1': "rock", '2': "paper", "3":"scissors"}
    print("you chose " + weapons[val])

    cheat_wins = {
        "rock": "paper",
        "scissors": "rock",
        "paper": "scissors"
    }

    print("Computer chooses " + cheat_wins[weapons[val]])
    print("\u001b[31mYOU LOOSE AGAIN\u001b[37m")