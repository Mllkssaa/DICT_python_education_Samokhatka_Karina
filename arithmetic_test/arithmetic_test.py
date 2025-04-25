import random


def get_level():
    while True:
        level = input("Enter the level: 1 - simple operations (2-9), 2 - squaring (11-29). \n>")
        if level in ('1', '2'):
            return int(level)
        print("Incorrect format.")


def generate_question(level):
    if level == 1:
        num1 = random.randint(2, 9)
        num2 = random.randint(2, 9)
        operation = random.choice(['+', '-', '*'])
        question = f"{num1} {operation} {num2}"
        answer = eval(question)
    else:
        num1 = random.randint(11, 29)
        question = f"{num1}^2"
        answer = num1 ** 2
    return question, answer


def get_answer():
    while True:
        response = input("Your answer: ")
        if response.isdigit() or (response.startswith('-') and response[1:].isdigit()):
            return int(response)
        print("Incorrect format.")


def main():
    level = get_level()
    correct_answers = 0

    for _ in range(5):
        question, correct_answer = generate_question(level)
        print(f"What is {question}?")

        user_answer = get_answer()
        if user_answer == correct_answer:
            print("Right!")
            correct_answers += 1
        else:
            print("Wrong!")

    print(f"Your mark is {correct_answers}/5.")

    save_result = input("Would you like to save your result to the file? Enter yes or no: ").strip().lower()
    if save_result in ('yes', 'y'):
        name = input("Enter your name: ")
        level_description = "simple operations with numbers 2-9" if level == 1 else "squaring numbers 11-29"

        with open("results.txt", "a") as file:
            file.write(f"{name}: {correct_answers}/5 in level {level} ({level_description}).\n")
        print("The results are saved in 'results.txt'.")


if __name__ == "__main__":
    main()

