import random
# for _ in range(0, 100):
#     print(random.randint(1, 5))

def get_user_input():
    while True:
        user_input = input("Make a choice r/p/s: ")
        if user_input in ["r", "p", "s"]:
            return user_input


def get_computer_input():
    return random.choice(["r", "p", "s"])

def play_game():
    user_input = get_user_input()
    computer_input = get_computer_input()

    if user_input == computer_input:
        return "draw"
    elif (user_input == "r" and computer_input == "s") or (user_input == "s" and computer_input == "p") or (user_input == "p" and computer_input == "r"):
        return "win"
    else:
        return "lose"

print(play_game)
print(play_game())

def play_game(name):
    return f"no gmaes to play, {name}"


print(play_game)
print(play_game("Filip"))