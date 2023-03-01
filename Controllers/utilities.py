from datetime import date, timedelta

# score
SCORE_LOOSER = 0
SCORE_WINNER = 1
SCORE_NULL = 0.5


def input_text_field(user_input):
    print("- " + user_input + ": ")
    if input() == "":
        return "empty"
    return input()

def date_text_field(user_input): 
    print("- " + user_input + ": ")
    if input() == "" and user_input == "ending date (jj/mm/aaaa) : \n(if empty, ending date is in one day) ' ":
        return date.today() + timedelta(days=1) 
    elif input() == "":
        return date.today()
    else:
        return input()