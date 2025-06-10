# small = $15
# medium = #20
# large = $25
# pepperoni for small = +$2
# pepperoni for medium and large = +$3
# extra cheese = +$1

print("Welcome to python pizza delivery!")

size = input("What size pizza do you want? (S, M, L) ")
pepperoni = input("Do you want pepperoni on your pizza? (Y or N) ")
cheese = input("Do you want extra cheese on your pizza? (Y or N) ")

amount = 0

if size == "S":
    amount += 15
elif size == "M":
    amount += 20
else:
    amount += 25


if pepperoni == "Y":
    if size == "S":
        amount += 2
    else:
        amount += 3
else:
    print(f"Your total bill is ${amount}")


if cheese == "Y":
    amount += 1
    print(f"Your total bill is ${amount}")
else:
    print(f"Your total bill is ${amount}")
