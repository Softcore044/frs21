while True:
    Day = int(input("Введите день рождения: "))
    month = int(input("Введите месяц рождения: "))


    if (Day >= 21 and Day <= 31 and month == 3)or(Day >= 1 and Day <= 20 and month == 4 ):
        print('Овен ')

    elif (Day >= 21 and Day <= 30 and month == 4)or(month ==5 and Day >= 1 and Day <= 21):
        print('Телец ')

    elif (Day >= 22 and Day <= 31 and month == 5)or(month ==6 and Day >= 1 and Day <= 21):
        print('Близнецы ')

    elif (Day >= 22 and Day <= 30 and month == 6)or(month ==7 and Day >= 1 and Day <= 22):
        print('Рак ')

    elif (Day >= 23 and Day <= 31 and month == 7)or(month ==8 and Day >= 1 and Day <= 21):
        print('Лев ')

    elif (Day >= 22 and Day <= 31 and month == 8)or(month ==9 and Day >= 1 and Day <= 23):
        print("Дева ")

    elif (Day >= 24 and Day <= 30 and month == 9)or(month ==10 and Day >= 1 and Day <= 23):
        print("Весы ")

    elif (Day >= 24 and Day <= 31 and month == 10)or(month ==11 and Day >= 1 and Day <= 22):
        print("Скорпион ")

    elif (Day >= 23 and Day <= 30 and month == 11)or(month ==12 and Day >= 1 and Day <= 22):
        print("Стрелец ")

    elif (Day >= 23 and Day <= 31 and month == 12)or(month ==1 and Day >= 1 and Day <= 20):
        print("Козерог ")

    elif (Day >= 21 and Day <= 31 and month == 1)or(month ==2 and Day >= 1 and Day <= 19):
        print("Водолей ")

    elif (Day >= 20 and Day <= 28 and month == 2)or(month ==3 and Day >= 1 and Day <= 20):
        print("Рыбы ")

    else:
      'Не понятно'