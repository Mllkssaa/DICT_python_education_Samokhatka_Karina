import random

def load_rating():
    ratings = {}
    try:
        with open("rating.txt", "r") as file:
            for line in file:
                print("Reading Line", line)
                name, score = line.strip().split()
                ratings[name] = int(score)
    except FileNotFoundError:
        pass
    return ratings

def get_result(user_choice, computer_choice):
    rules = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock",
        "rock": "fire",
        "fire": "scissors",
        "scissors": "snake",
        "snake": "human",
        "human": "tree",
        "tree": "wolf",
        "wolf": "sponge",
        "sponge": "paper",
        "paper": "air",
        "air": "water",
        "water": "dragon",
        "dragon": "devil",
        "devil": "lightning",
        "lightning": "gun",
        "gun": "rock"
    }

    if user_choice == computer_choice:
        return "draw"
    elif computer_choice in rules[user_choice]:
        return "win"
    else:
        return "lose"

def main():
    options = ("rock", "paper", "scissors", "fire", "snake", "human", "tree", "wolf", "sponge", "air", "water", "dragon", "devil", "lightning", "gun")
    rating = load_rating()

    name = input("Enter your name \n>")
    print(f"Hello, {name}")
    score = rating.get(name, 0)

    while True:
        player = input("Enter a choice (rock, paper, scissors, fire, snake, human, tree, wolf, sponge, air, water, dragon, devil, lightning, gun), !rating to view score, or !exit to quit: \n>")

        if player == "!exit":
            print("Bye!")
            break
        elif player == "!rating":
            print(f"Your rating: {score}")
        elif player in options:
            computer = random.choice(options)
            print(f"Player: {player}")
            print(f"Computer: {computer}")


            result = get_result(player, computer)
            if result == "draw":
                print(f"There is a draw ({computer})")
                score += 50
            elif result == "win":
                print(f"well done. The computer chose {computer} and failed")
                score += 100
            else:
                print(f"Sorry, but the computer chose {computer}")
        else:
            print("Invalid input")
if __name__ == "__main__":
    main()