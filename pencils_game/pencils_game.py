import random

def counts_pencils():
    while True:
        pencils = input("How many pencils you want use:\n")
        if not pencils.isdigit() or int(pencils) <= 0:
            print("The number of pencils should be positive.")
        else:
            return int(pencils)


def players(player1, player2):
    while True:
        player = input(f"Who will be the first one? ({player1}, {player2}):\n")
        if player not in [player1, player2]:
            print(f"Choose {player1} or {player2}")
        else:
            return player


def bot(pencils_left):
    """Бoт грає за стратегією"""
    if pencils_left % 4 == 0:
        return 3
    elif pencils_left % 4 == 3:
        return 2
    elif pencils_left % 4 == 2:
        return 1
    else:
        return random.randint(1, min(3, pencils_left))


def game():
    player1 = "Mia"
    player2 = "Zask"

    pencils = counts_pencils()
    player = players(player1, player2)

