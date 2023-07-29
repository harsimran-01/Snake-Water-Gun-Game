# Snake Water Gun Game

import random

while True:
    def gamewinner(comp, b):
        if comp == b:
            return None
        elif comp == 'S':
            if b == "W":
                return False
            elif b == "G":
                return True
        elif comp == "W":
            if b == "S":
                return True
            elif b == "G":
                return False
        elif comp == "G":
            if b == "S":
                return True
            elif b == "W":
                return False

    print("\n                        **** Computer's Turn ****\n")
    print("Computer Has choosed. Now it's Your Turn\n")
    randno = random.randint(1, 3)
    if randno == 1:
        comp = "S"
    elif randno == 2:
        comp = "W"
    elif randno == 3:
        comp = "G"

    # print(f"Computer chooses {comp}.")
    print("                          ****Your's Turn ****\n")
    b = input("What do you want: 'S'-> Snake /'W' -> Water /'G' -> Gun : ") 
    print(f"\nComputer choosed {comp}")
    print(f"You Choosed {b}\n")
    win = gamewinner(comp, b)

    if win == None:
        print("\n\t  It's a Tie...  \n")
    elif win == True:
        print("\n\t You Won the Game.. \n")
    else:
        print("\n\t You Loose The Game.. \n")       

    ask = input("Do You want to Continue: ").lower()
    if ask == "no":
        print("\nSnake-Water-Gun Game is CLOSED..\n")
        break
