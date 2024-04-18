from random import choice, randint


# User input will be of type string and return string
def get_response(user_input : str):
    lowered_str = user_input.lower()

    if lowered_str == '':
        return "Say Something!"
    elif "hello" in  lowered_str:
        return "Hi!"
    elif "how are you" in  lowered_str:
        return "I am good thanks! How are you?"
    elif "bye" in lowered_str:
        return "cya!"
    else:
        return choice(["Sorry I cannot understand", "What u talking about?", "Bruh", "English?"])
    
    #raise NotImplemented("Code is not implemented yet")
