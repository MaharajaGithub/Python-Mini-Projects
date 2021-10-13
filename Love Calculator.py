# Love Calculator Excersize:

print("Welcome to love calculator! \n")
name1 = input("What is your name? ")
name2 = input("What is their name? ")

combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = combined_string.count("t")
r = combined_string.count("r")
u = combined_string.count("u")
e = combined_string.count("e")

true = t+r+u+e

l = combined_string.count("l")
o = combined_string.count("o")
v = combined_string.count("v")
e = combined_string.count("e")

love = l+o+v+e

love_score = int(str(true)+str(love))

if love_score < 10 or love_score > 90:
    print(f"Your love score is {love_score}%. You go together like coke and mentos.")
elif love_score >= 40 and love_score <=50:
    print(f"Your love score is {love_score}%. you are alright together")
else:
    print(f"Yout love score is {love_score}%.")
