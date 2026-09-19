import argparse

# Объявление парсера для аргументов командной строки
parser = argparse.ArgumentParser()

# Добавление аргумента
parser.add_argument("numbers")

# Парсинг аргументов командной строки
args = parser.parse_args()

# Открытие файла numbers
file = open(args.numbers)

# Инициализация массива
nums = []

# Пока не конец файла
while (line := file.readline()):
    # Добавление числа в массив
    nums.append(int(line))

# Закрытие файла numbers
file.close()

# Сортировка массива
sortedArray = sorted(nums)

# Вычисление оптимального числа для приведения — медианы
target = sortedArray[len(sortedArray) // 2]

# Инициализация числа шагов
result = 0
# Для каждого числа
for num in nums:
    # Вычисляем модуль разницы между целевым числом и текущим и прибавляем эту разницу к количеству шагов
    result += abs(target - num)

# Проверка ограничения по максимальному количеству ходов
if result > 20:
    print("«20 ходов недостаточно для приведения всех элементов массива к одному числу»")
else:
    print(result)