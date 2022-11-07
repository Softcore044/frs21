ten = list(range(1, 11))
evens = list(filter(lambda x: x % 2 == 0, ten))
evens = list(map(lambda x: x**2, evens))

def get_object(list = ten):
    while True:
        try:
            index_user = int(input("Введите индекс или q для выхода: "))
            if index_user == 'q':
                break
            print(list[index_user])
        except:
            print(f'Индекс должен быть от 0 до {len(list) - 1}')
get_object()

