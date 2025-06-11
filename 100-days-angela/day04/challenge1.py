import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

print("Welcome to Rock, Paper, Scissor game")

userChoice = int(
    input("Choose one: \n1 for Rock, \n2 for Paper and \n3 for Scissors: ")
)

if userChoice == 1:
    print("\nYou Choose: Rock")
    print(rock)
elif userChoice == 2:
    print("\nYou Choose: Paper")
    print(paper)
elif userChoice == 3:
    print("\nYou Choose: Scissors")
    print(scissors)
else:
    print("Enter the correct number")


comChoice = random.randint(1, 3)

if comChoice == 1:
    print("\n\nComputer choose: Rock")
    print(rock)
elif comChoice == 2:
    print("\n\nComputer choose: Paper")
    print(paper)
else:
    print("\n\nComputer choose: Scissors")
    print(scissors)


# rock wins against scissors    (done)
# scissors win against paper    ()
# paper win against rock        ()


#
if userChoice > 3 or userChoice < 1:
    print("\nEnter the valid number. You Lost")
elif userChoice == 1 and comChoice == 2:
    print("\nComputer Won")
elif userChoice == 3 and comChoice == 1:
    print("\nComputer Won")
elif userChoice == 2 and comChoice == 3:
    print("\nComputer Won")
elif userChoice == 1 and comChoice == 3:
    print("\nYou Won")
elif userChoice == 3 and comChoice == 2:
    print("\nYou Won")
elif userChoice == 2 and comChoice == 1:
    print("\nYou Won")
else:
    print("\nIt's a Draw")
