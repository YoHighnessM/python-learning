from art import logo

print(logo)
auctionDict = {}

print("Welcome to secret auction program.")


continueBid = True

while continueBid:
    userName = input("What's your name? ")
    bidAmount = int(input("What's your bid? $"))

    askUser = input("Are there any biders? (Yes or No): ")

    if askUser == "no":
        continueBid = False
        print("Bye")
    else:
        print("\n" * 50)

    auctionDict.update({userName: bidAmount})

valueList = list(auctionDict.values())
# print(valueList)

maxBidAmount = max(valueList)

for name, bid in auctionDict.items():
    if bid == maxBidAmount:
        print(f"The winner is {name} with ${bid} bid.")

# print(auctionDict)
