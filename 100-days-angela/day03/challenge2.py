print("Welcome to Tressure Island.\nYour mission is to find the tressure")

actionOne = input("Right or Left? ")

if actionOne == "right":
    print("Game Over.")
elif actionOne == "left":
    actionTwo = input("Swim or Wait? ")

    if actionTwo == "swim":
        print("Game Over")
    elif actionTwo == "wait":
        actionThree = input("Which door? (Red, Yellow, Blue) ")

        if actionThree == "red":
            print("Game Over")
        elif actionThree == "blue":
            print("Game Over")
        elif actionThree == "yellow":
            print("You Won!")
        else:
            print("Enter the correct action")
    else:
        print("Enter the correct option")
else:
    print("Enter the correct option")
