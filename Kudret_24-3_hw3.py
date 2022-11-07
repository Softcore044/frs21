while True:
    user = str(input('Введите слово:'))
    if user == 'exit':
        break
    print('Слово: ' + user)
    print ('Количество букв: '+ str(len([i for i in user if i.isalpha()])))
    vowels = 0
    consonants = 0
    for i in user:
        letter = i.lower()
        if letter == "a" or letter == "e" or \
            letter == "i" or letter == "o" or \
            letter == "u" or letter == "y" or \
            letter == "а" or letter == "у" or \
            letter == "о" or letter == "ы" or \
            letter == "э" or letter == "я" or \
            letter == "ю" or letter == "е" or \
            letter == "и" or letter == "э":
            vowels += 1
        else:
            consonants += 1
    quantity = (vowels / consonants) * 50
    quantity1 = (consonants / vowels) * 50
    print("Гласные буквы:  %i\nСогласные буквы:  %i" % (vowels, consonants))
    print('Гласные/Согласные: ' + str(float(round(quantity, 1))) + '%/' + str(float(round(quantity1, 1))) + '%')
    print('Введите ''exit'' для завершения программы')