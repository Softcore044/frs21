data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
letters = []
numbers = []
for i in data_tuple:
    if type(i) == str:
        letters.append(i)
    else:
        numbers.append(i)
numbers.remove(6.13)
letters.append(numbers.pop(0))
numbers.insert(1, 2)
numbers.sort()
letters.reverse()
letters[1] = letters[1].upper()
letters[-2] = letters[-2].lower()
numbers = [i**2 for i in numbers]
letters = tuple(letters)
numbers = tuple(numbers)
print(letters, numbers)
