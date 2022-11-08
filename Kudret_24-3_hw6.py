def first_word(words='Hello bro'):
    if type(words) == str:
        first_word = words.split()
        return first_word [0]
    elif type(words) != str:
        return False

print(first_word())

def average(*args):
    return (int(sum(args))//(len(args)))
print(average(55, 45))

def check_password(password):
    if len(password) > 6 and not password.isdigit() and not password.isalpha():
        return True
    else:
        return False

print('hello world')