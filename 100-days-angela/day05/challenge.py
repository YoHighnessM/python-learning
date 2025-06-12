import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

numLetter = int(input("How many Letter do you want? "))
numNumber = int(input("How many Number do you want? "))
numSymbol = int(input("How many Symbols do you want? "))

finalPassword = ""

for char in range(1, numLetter + 1):
    newLetter = random.choice(letters)
    finalPassword += newLetter

listPassword = list(finalPassword)


for num in range(1, numNumber + 1):
    newNumber = random.choice(numbers)
    finalPassword += newNumber

listNumber = list(finalPassword)


for symbol in range(1, numSymbol + 1):
    newSymbol = random.choice(symbols)
    finalPassword += newSymbol

listSymbol = list(finalPassword)
# print(f"not shuffled {listSymbol}")

# random.shuffle(listSymbol)
# print(f"yes shuffled {listSymbol}")

final = "".join(listSymbol)
print(f"\nHere is your password: {final}\n")
