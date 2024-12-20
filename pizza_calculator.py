print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
bill = 0
if size == "S":
    bill = 15
    print("Your current bill is 15$ ")
elif size == "M":
    bill = 20
    print("Your current bill is 20$ ")
else:
    bill =25
    print("Your current bill is 25$ " )

pepperoni_extra = input("Do you want pepperoni on your pizza? Y or N: ")

pepperoni_small = 2
pepperoni_m_l = 3

if pepperoni_extra == "Y":
    print("Great!")
    if size == "S":
        bill = bill + pepperoni_small
        print(f"Your bill is {bill} $")
    elif size == "M":
        bill = bill + pepperoni_m_l
        print(f"Your bill is {bill} $")
    else:
     bill = bill + pepperoni_m_l
     print(f"Your bill is {bill} $")

cheese = input("Do you want some extra cheese? Y or N: ")

cheese_extra = 1


if cheese == "Y":
     print("Great!")
     bill = bill + cheese_extra
     print(f"Your bill is {bill}")
else:
    bill = bill
    print(f"Your total bill is {bill}")

print("Thank you!")
print("Bon Appeti")
