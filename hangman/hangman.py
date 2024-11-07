import random

def game_welcome():
    print("HANGMAN")
    print("The game will be available soon.")

game_welcome()

words = ["python", "java", "javascript", "php"]
random_word = random.choice(words)

display_gaps = ['_'] * len(random_word)

max_attempts = 7
sofar_attempts = 0

guessed_letters = []

hungman_figures = [
""" 
    +---+ 
    |   | 
        | 
        | 
        | 
        | 
==========
""",
""" 
    +---+ 
    |   | 
    o   | 
        | 
        | 
        | 
==========
""",
""" 
    +---+ 
    |   | 
    o   | 
    |   | 
        | 
        | 
==========
""",
""" 
    +---+ 
    |   | 
    o   | 
   /|   | 
        | 
        | 
==========
""",
""" 
    +---+ 
    |   | 
    o   | 
   /|\\  | 
        | 
        | 
==========
""",
""" 
    +---+ 
    |   | 
    o   | 
   /|\\  | 
   /    | 
        | 
==========
""",
""" 
    +---+ 
    |   | 
    o   | 
   /|\\ | 
   / \\ | 
        | 
==========
""",
]

while True:
    print(hungman_figures[sofar_attempts])
    print("  ".join(display_gaps))

    guess = input("guess a letter:  >  ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("you should enter a letter. ")
        continue

    if guess in guessed_letters:
        print("already guessed that. ")
        continue

    guessed_letters.append(guess)
    if guess in random_word:
        for i in range(len(random_word)):
            if random_word[i] == guess:
                display_gaps[i] = guess


    else:
        sofar_attempts += 1
        print("incorrect guess! you got ", max_attempts - sofar_attempts , "guesses left. ")

    if "_" not in display_gaps:
        print("Congratulations! you won. The word is ", random_word)
        break
    elif sofar_attempts == max_attempts:
        print("you raan out of attempts. the word was ", random_word)
        break