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

    if userLetter in correct_letters:
        print(f"You've already guessed the letter {userLetter}")

    if userLetter not in randomWord:
        lives -= 1
        print(f"*************** {lives}/6 LIVES LEFT ***************")

        if lives == 0:
            print(stages[lives])
            print(
                f"*************** You Lost!!! The word was '{randomWord}' ***************"
            )
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
    if userLetter not in randomWord:
        print(f"You guessed {userLetter}, which is not in the word. You'll lose a live")

    if "_" not in displayLetter:
        print("*************** You Won ***************")

    print(stages[lives])
