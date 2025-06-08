print("Welcome to the tip calculator!")

totalBil = float(input("What was the total bill? $"))

tipAmount = int(input("How much tip would you like to give? 10, 12, or 15? "))
actualTipAmount = tipAmount / 100

splitAmount = int(input("How many people to split the bill? "))

billTip = totalBil * actualTipAmount
newBill = totalBil + billTip

billTipSplitAmount = newBill / splitAmount

#
#

# billTipSplitAmount = (totalBil * actualTipAmount + totalBil) / splitAmount

#
#

finalAmount = round(billTipSplitAmount, 2)

print(f"Each person should pay: ${finalAmount}")
