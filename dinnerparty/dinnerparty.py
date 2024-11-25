import random

friends_dict = {}

people = int(input("Enter the number of people joining (including you): "))

if people <= 0:
    print("No one is joining for the party")
else:
    for i in range(people):
        name = input(f"Enter the name of person {i + 1}: ")
        friends_dict[name] = 0

print(friends_dict)

total_amount = float(input("Enter the total amount: "))
split_amount = round(total_amount / people, 2)

for name in friends_dict:
    friends_dict[name] = split_amount

print(friends_dict)

lucky_choise = input("Do you want to choose a lucky one? (Yes/No): ").strip().lower()

if lucky_choise == 'yes':
    lucky_people = random.choice(list(friends_dict.keys()))
    print(f"{lucky_people} is the lucky one!")

    split_amount = round(total_amount / (people -1), 2)

    for name in friends_dict:
        if name != lucky_people:
            friends_dict[name] = split_amount
else:
    print("No one is going to be lucky..")

    total_amount = round(total_amount / people, 2)

    for name in friends_dict:
        friends_dict[name] = split_amount

print(friends_dict)
