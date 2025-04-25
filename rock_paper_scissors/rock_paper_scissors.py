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

def get_result(user_choice, computer_choice, options):
    if user_choice == computer_choice:
        return "draw"

    user_index = options.index(user_choice)
    rotated = options[user_index+1:] + options[:user_index]
    half = len(rotated) // 2
    loses_to_user = rotated[:half]

    if computer_choice in loses_to_user:
        return "win"
    else:
        return "lose"


def main():
    options = ("rock", "fire", "scissors", "snake", "human", "tree", "wolf", "sponge", "paper", "air", "water", "dragon", "devil", "lightning" "gun")
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


            result = get_result(player, computer, options)
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