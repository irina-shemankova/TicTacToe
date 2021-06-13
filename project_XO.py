def welcome():
    print('**************************************************')
    print('     Добро пожаловать в игру крестики-нолики')
    print('***************************************************')
    print('Цель игры - поставить три одинаковых символа в ряд.')
    print('Игровое поле перед вами. Первым ходит крестик.')
    print()
    print('Вводите координаты клетки через пробел.')
    print('Сначала вводится номер строки, потом номер столбца.')
    print()


# Функция будет показывать игровое поле после каждого хода,
# заменяя пробелы на Х или 0.
def show_playing_field():
    print("  0 1 2")
    for i in range(3):
        row = " ".join(playing_field[i])
        print(f"{i} {row}")


# Ввод координат пользователем
def input_coordinates():
    while True:
        coordinates = input("Ваш ход: ").split()

        if len(coordinates) != 2:  # проверка того, что вводятся ровно 2 координаты
            print("Введите 2 координаты через пробел!")
            continue

        _x, _y = coordinates
        if not (_x.isdigit()) or not (_y.isdigit()):  # проверка того, что координаты заданы целыми числами
            print(" Введите целые числа через пробел! ")
            continue

        _x, _y = int(_x), int(_y)

        if _x < 0 or _x > 2 or _y < 0 or _y > 2:
            print("Координаты вне диапазона!")
            continue

        if playing_field[_x][_y] != " ":
            print("Клетка занята!")
            continue

        return _x, _y


# Функция, которая проверяет, не появилась ли выигрышная комбинация
def check_win():
    win_coordinates = (((0, 0), (0, 1), (0, 2)),
                       ((1, 0), (1, 1), (1, 2)),
                       ((2, 0), (2, 1), (2, 2)),
                       ((0, 2), (1, 1), (2, 0)),
                       ((0, 0), (1, 1), (2, 2)),
                       ((0, 0), (1, 0), (2, 0)),
                       ((0, 1), (1, 1), (2, 1)),
                       ((0, 2), (1, 2), (2, 2)))

    # После каждого хода будем проверять, не появился ли у нас выигрышный ряд
    for coordinates in win_coordinates:
        symbols = []
        for c in coordinates:
            symbols.append(playing_field[c[0]][c[1]])  # Здесь смотрим, какая комбинация у нас

        # Оцениваем, не появилось ли три одинаковых символа на месте выигрышных кортежей из win_coordinate
        if symbols == ["X", "X", "X"]:
            show_playing_field()
            print("Выиграл X!!!")
            return True

        if symbols == ["0", "0", "0"]:
            show_playing_field()
            print("Выиграл 0!!!")
            return True
    return False


welcome()

# Игровое поле представим в виде матрицы 3*3.
# Первоначально заполняем его пробелами
playing_field = [[" "] * 3 for i in range(3)]

count = 0
while True:
    count += 1
    show_playing_field()

    if count % 2 == 1:  # Крестик ходит первым и далее в нечетный ход
        print()
        print(" Ходит крестик")
        print()
        x, y = input_coordinates()
        playing_field[x][y] = "X"
    else:
        print()
        print(" Ходит нолик")  # Нолик ходит в четный ход
        print()
        x, y = input_coordinates()
        print()
        playing_field[x][y] = "0"

    if check_win():
        break

    if count == 9:  # Максимально можно сделать 9 ходов (9 клеток на поле)
        print(" Ничья!")
        break
