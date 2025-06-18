import random

stages = [
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
]

word_list = ["bird", "banana", "sky", "table", "laptop"]

numOfWordList = len(word_list)
randomIndex = random.randint(0, numOfWordList - 1)
randomWord = word_list[randomIndex]

print("You have a total of 6 tries")
print(randomWord)

dash = "_"
randomWordLen = len(randomWord)

for i in range(randomWordLen):
    print(dash, end="")


displayLetter = ""
correct_letters = []

lives = 6

while displayLetter != randomWord:

    displayLetter = ""

    userLetter = input("\nGuess a letter: ").lower()

    if userLetter not in randomWord:
        lives -= 1
        print(f"lives left {lives}")

        if lives == 0:
            print(stages[lives])
            print("You Lost")
            break

    for letter in randomWord:
        if letter == userLetter:
            displayLetter += letter
            correct_letters.append(userLetter)
        elif letter in correct_letters:
            displayLetter += letter
        else:
            displayLetter += "_"

    print(displayLetter)

    if "_" not in displayLetter:
        print("You Won")

    print(stages[lives])
