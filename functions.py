import datetime


def welcome(name):

    current_hour = datetime.datetime.now().hour
    if 20 <= current_hour < 24 or 0 <= current_hour < 6:
        return f"¡Buenas noches {name}!"
    elif 6 <= current_hour < 12:
        return f"¡Buenos días {name}!"
    elif 12 <= current_hour < 20:
        return f"¡Buenas tardes {name}!"


def handle_word(word):
    if word == word[::-1]:
        return "¡Bonita palabra!"
    else:
        return word[::-1]


def handle_stop(name):
    return f"Adios {name}!"


def main_loop(name, word_1, word_2, word_3, word_4):
    log = ""
    log += welcome(name)
    words = [word_1, word_2, word_3, word_4]
    i = 0
    while True:
        word = words[i]
        if word == "stop!":
            log = log + f"\n{handle_stop(name)}"
            break
        else:
            log = log + f"\n{handle_word(word)}"
        i += 1
    return log
