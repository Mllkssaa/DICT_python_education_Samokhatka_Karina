bot_name = "Chinazes"
birth_year = 2024

print(f"Hello! My name is {bot_name}.")
print(f"I was created in {birth_year}.")

your_name = input("Please, remind me your name: ")
print(f"What a great name you have, {your_name}!")

print("Let me guess your age:).")
print("Enter remainders of dividing your age by 3, 5 and 7.")
remainder3 = int(input(">>> "))
remainder5 = int(input(">>> "))
remainder7 = int(input(">>> "))

age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print(f"Your age is {age}; that's a good time to start programming!")

def count_to_number():
    print("Now I will prove to you that I can count to any number you want.")
    number = int(input(">>> "))

    for i in range(number + 1):
        print(f"{i}!")

def give_test():
    print("Let's test your programming knowledge.")
    print("What is the correct way to define a function in Python?")
    print("1. > def function_name():")
    print("2. > function function_name():")
    print("3. > func function_name(): ")
    print("4. > define function_name():")


    correct_answer = 1

    while True:
        user_answer = int(input())
        if user_answer == correct_answer:
            print("Congratulations, have a nice day!")
            break
        else:
            print("Please, try again.")

count_to_number()
give_test()



def give_test():
    print("Let's test your programming knowledge.")
    print("What is the correct way to define a function in Python?")
    print("1.def function_name():")
    print("2.function function_name():")
    print("3.func function_name():")
    print("4.define function_name():")

    correct_answer = 1

    while True:
        user_answer = int(input())
        if user_answer == correct_answer:
            print("Congratulations, have a nice day!")
            break
        else:
            print("Please, try again.")
        if user_answer == correct_answer:
            print("Congratulations, have a good day!")
            break
        else:
            print("Please, try again..")













