board = [[" -"]*3 for i in range(3)]

print('----------------------')
print('Игра "Крестики-Нолики"')
print('----------------------')


def draw_board():     # Рисуем доску
    print(' ', ' 0', ' 1', ' 2')
    for i in range(3):
        print(str(i), board[i][0], board[i][1], board[i][2])


def take_input():     # Проверка вводимых координат
    while True:
        coordinates = input("Введите через пробел № строки и столбца: ").split()

        if len(coordinates) != 2:  # Если введено не 2 цифры
            print('Некорректный ввод. Нужно ввести ДВЕ координаты ЧЕРЕЗ ПРОБЕЛ.')
            continue

        if not (coordinates[0].isdigit() and coordinates[1].isdigit()):  # Если координаты не состоят из цифр
            print('Некорректный ввод. Нельзя вводить буквы, можно ТОЛЬКО 0, 1 или 2')
            continue

        x, y = coordinates
        x = int(x)
        y = int(y)

        if 0 <= x <= 2 and 0 <= y <= 2:  # Если координаты 0, 1 или 2
            if board[x][y] == ' -':  # Если клетка еще свободна
                return x, y
            else:
                print('Эта клетка уже занята. Введите координаты пустой клетки.')
                continue
        else:
            print('Некорректный ввод. Нужно вводить ТОЛЬКО 0, 1 или 2.')
            continue


def winner():  # Выигрышные комбинации
    winning_combinations = [((0, 0), (0, 1), (0, 2)),
                            ((1, 0), (1, 1), (1, 2)),
                            ((2, 0), (2, 1), (2, 2)),
                            ((0, 0), (1, 0), (2, 0)),
                            ((0, 1), (1, 1), (2, 1)),
                            ((0, 2), (1, 2), (2, 2)),
                            ((0, 0), (1, 1), (2, 2)),
                            ((0, 2), (1, 1), (2, 0))]

    for i in winning_combinations:  # Проверяем по выигр.комб-ям равны ли ячейки и не являются ли свободными
        i0, i1, i2 = i[0], i[1], i[2]
        if board[i0[0]][i0[1]] == board[i1[0]][i1[1]] == board[i2[0]][i2[1]] != ' -':
            draw_board()
            print(f'Победили {board[i0[0]][i0[1]]} !!!')
            print('----------')
            return True
    return False


def main():
    num = 0  # Счетчик ходов
    while True:
        draw_board()

        if num % 2 == 0:  # Если номер хода четный, то это X.
            print('----------')
            print(f'№{num + 1}. Ход X.')
        else:
            print('----------')
            print(f'№{num + 1}. Ход 0.')  # Если номер хода нечетный, то это 0.
        x, y = take_input()

        if num % 2 == 0:  # Проставляем X или 0.
            board[x][y] = ' X'
        else:
            board[x][y] = ' 0'

        if winner():  # Если выигрышная ситуация
            break

        num += 1

        if num == 9:  # Если ходов 9, то ничья
            draw_board()
            print('Ничья!')
            print('----------')
            break


main()