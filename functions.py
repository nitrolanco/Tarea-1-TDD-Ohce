import datetime

def welcome(name):
    
    current_hour = datetime.datetime.now().hour
    if 20 <= current_hour < 24 or 0 <= current_hour < 6:
        return f'¡Buenas noches {name}!'
    elif 6 <= current_hour < 12:
        return f'¡Buenos días {name}!'
    elif 12 <= current_hour < 20:
        return f'¡Buenas tardes {name}!'
    

def handle_word(word):
    if word == word[::-1]:
        return "¡Bonita palabra!"
    else:
        return word[::-1]
def handle_stop(name):
    return f"Adios {name}!"