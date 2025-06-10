# userNum = int(input("Enter a number: "))

# if userNum % 2 == 0:
#     print("it's even")
# else:
#     print("it's odd")


height = int(input("what is your height? "))
bill = 0

if height > 120:
    age = int(input("how old are you? "))

    if age >= 45 and age <= 55:
        print("the ticket is on us. enjoy")
    elif age <= 12:
        bill = 5
    elif age <= 18:
        bill = 7
    else:
        bill = 12

    photo = input("do you wnat to include photo? (yes/no) ")

    if photo == "yes":
        totalBill = 3 + bill
        print(f"your total bill will be ${totalBill}")
    else:
        print(f"your final bill is ${bill}")
else:
    print("You can't ride")
