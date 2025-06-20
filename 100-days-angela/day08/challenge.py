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
user_word = input("Type your message: >>> ")
shift_num = int(input("Type the shift number: >>> "))


def ceasar(original_text, shift_amount, encode_decode):

    user_word_list = list(original_text)
    newWord = ""

    for letter in user_word_list:
        letterIndex = alphabet.index(letter)

        if encode_decode == "encode":
            newLetterIndex = letterIndex + shift_amount
        else:
            newLetterIndex = letterIndex - shift_amount

        if newLetterIndex > 25:
            newRoundIndex = newLetterIndex % len(alphabet)
            newWord += alphabet[newRoundIndex]
        else:
            newWord += alphabet[newLetterIndex]

    print(f"Here is the {encode_decode}d text: {newWord}")


ceasar(original_text=user_word, shift_amount=shift_num, encode_decode=user_choice)
