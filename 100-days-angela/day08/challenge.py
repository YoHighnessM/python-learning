alphabet = [
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
]

user_choice = input("Type 'encode' to encrypt, type 'decode' to decrypt: >>> ")


def ceasar():

    if user_choice == "encode":

        user_word = input("Type your message: >>> ")
        shift_num = int(input("Type the shift number: >>> "))

        def encrypt(original_text, shift_amount):

            user_word_list = list(original_text)
            newWord = ""

            for letter in user_word_list:
                letterIndex = alphabet.index(letter)
                newLetterIndex = letterIndex + shift_amount

                if newLetterIndex > 25:
                    newRoundIndex = newLetterIndex % len(alphabet)
                    newWord += alphabet[newRoundIndex]
                else:
                    newWord += alphabet[newLetterIndex]

            print(f"Here is the encoded text: {newWord}")

        encrypt(original_text=user_word, shift_amount=shift_num)

    elif user_choice == "decode":

        encryptedWord = input("Type the encrypted word: >>> ")
        encryptShiftAmount = int(input("Type the shift amount used to encrypt: >>> "))

        def decrypt(encryptWord, encryptShift):
            encryptedWordList = list(encryptWord)
            newWord = ""

            for letter in encryptedWordList:
                letterIndex = alphabet.index(letter)
                newLetterIndex = letterIndex - encryptShift
                newWord += alphabet[newLetterIndex]

            print(f"Here is the decoded text: {newWord}")

        decrypt(encryptWord=encryptedWord, encryptShift=encryptShiftAmount)
    else:
        print("Insert the correct text")


ceasar()
