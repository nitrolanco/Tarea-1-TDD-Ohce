import datetime

def welcome(name):
    
    current_hour = datetime.datetime.now().hour
    if 20 <= current_hour < 24 or 0 <= current_hour < 6:
        return f'¡Buenas noches {name}!'
    elif 6 <= current_hour < 12:
        return f'¡Buenos días {name}!'
    elif 12 <= current_hour < 20:
        return f'¡Buenas tardes {name}!'
    

def is_palindrome(word):
    return