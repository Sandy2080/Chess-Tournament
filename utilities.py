
# score
SCORE_LOOSER = 0
SCORE_WINNER = 1
SCORE_NULL = 0.5

bcolors = {
    "header": '\033[95m',
    "blue": '\033[94m',
    "cyan": '\033[96m',
    "green": '\033[92m',
    "yellow": '\033[93m',
    "white": '\033[37m'
}


def input_text_field(user_input):
    print("- " + user_input + ": ")
    return input()
