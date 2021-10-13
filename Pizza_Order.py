print("Welcome to python pizza deliveries!\n")
size = input("What size pizza do you want?S,M or L ?:")
add_pepperoni = input("Do you want pepperoni? Y or N ?: ")
extra_cheese = input("Do you want extra cheese? Y or N? ")

bill = 0

if size == 'S':
    bill+=200
elif size == 'M':
    bill+=350
else:
    bill+=500

if add_pepperoni == "Y":
    if size == "S":
        bill+=50
    else:
        bill+=100
if extra_cheese == "Y":
    bill+=30
print(f"Your final bill is Rs {bill}")
