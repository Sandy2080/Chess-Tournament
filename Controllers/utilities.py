def input_text_field(user_input):
    print("- " + user_input + ": ")
    if user_input == "":
        return None
    return input()
    
def date_text_field(user_input):
    print(user_input)
    if user_input == "":
        return str(date.today())
    elif user_input == "" and user_input.find("ending"): 
        return str(date.today() + 1)
    else:
        return input()