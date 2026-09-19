import argparse

# Объявление парсера для аргументов командной строки
parser = argparse.ArgumentParser()

# Добавление аргументов
parser.add_argument("ellipse")
parser.add_argument("dot")

# Парсинг аргументов командной строки
args = parser.parse_args()

# Открытие файла ellipse
ellipse = open(args.ellipse)
# Считывание координат центра эллипса
x, y = (float(i) for i in ellipse.readline().split())
# Считывание радиусов эллипса (rx ry)
rx, ry = (float(i) for i in ellipse.readline().split())
# Закрытие файла ellipse
ellipse.close()

# Открытие файла dot
dot = open(args.dot)

# Пока не конец файла
while (line := dot.readline()):
    # Считывание координат точки
    a, b = (float(i) for i in line.split())

    # Значение уравнения эллипса для точки
    # (a - x)^2 / rx^2 + (b - y)^2 / ry^2
    value = ((a - x) ** 2) / (rx ** 2) + ((b - y) ** 2) / (ry ** 2)

    # Определение положения точки относительно эллипса
    if value < 1:
        print(1)
    elif value == 1:
        print(0)
    else:
        print(2)

# Закрытие файла dot
dot.close()