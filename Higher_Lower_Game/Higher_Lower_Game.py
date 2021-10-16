from game_data import data
import random

def format_data(city):
    city_name = city["Name"]
    city_state = city["State"]
    city_lang = city["Language"]
    return f"{city_name},state of {city_state}, official language is {city_lang}"

def check_answer(guess,a_population, b_population):
    if a_population > b_population:
        return guess == "a"
    else:
        return guess == "b"

city_a = random.choice(data)
city_b = random.choice(data)
if city_a == city_b:
    city_b = random.choice(data)

print(f"compare A:{format_data(city_a)}\n")
print("vs\n")
print(f"Against B: {format_data(city_b)}\n")

guess = input("Which city has most population in india ? Type 'A' or 'B': ").lower()

a_population_count = city_a["Population"]
b_population_count = city_b["Population"]

is_correct = check_answer(guess,a_population_count,b_population_count)

if is_correct:
    print(f"You're right. You Won!")
else:
    print(f"Sorry that's wrong. You Lose!")
