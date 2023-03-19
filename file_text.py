passwords_list = ['qwerty', '12345', 'xxxxxx', 'I was here']

# Запись в текстовый файл, Вариант 1. ПРАВИЛЬНЫЙ
with open(file='secret_file.txt', mode='a', encoding='utf-8') as file:
    file.writelines([line + '\n' for line in passwords_list])

# Запись в текстовый файл, Вариант 2. Обычный
file = open(file='hello.txt', mode='a', encoding='utf-8')
# file = open(file=r'C:\\User\Roman\hello.txt', mode='rt', encoding='utf-8')
# file=
#      '/Folder/file.txt'              # относительный путь к файлу
#      r'C:\\User\Roman\hello.txt'     # абстолютный путь к файлу, r - сырая строка (нивелирует \ )
# mode=
#     'r' - Открывает файл на чтение. (Значение по умолчанию)
#     'w' - Открывает файл на запись. Если файла нет, то будет создан новый.
#           Если файл существует, данные в нем будут перезаписаны.
#     'x' - Открывает файл на запись. Если файл уже существует, операция завершится ошибкой.
#     'a' - Открывает файл и дозаписывает в него данные, не стирая предыдущие.
#           Создает новый файл, если он не существует.
#     't' - Открывает файл как текстовый. (Значение по умолчанию)
#     'b' - Открывает файл в бинарном/двоичном режиме.
#     '+' - Позволяет работать с файлом как для записи так и для чтения.
# encoding=
#     'utf-8'   # русский уникод
#     'cp1251'  # русский WINDOWS
for passwd in passwords_list:
    file.write(f'{passwd}\n')
file.close()          # закрывем файл


print('# Чтение из файла, Вариант 1')
# Чтение из файла, Вариант 1
with open(file='secret_file.txt', mode='rt') as file:
    text = file.read()
    print(text)

print('# Чтение из файла, Вариант 2')
# Чтение из файла, Вариант 2
file = open(file='hello.txt', mode='rt')
# print(file.readlines())         # чтение всех строк из файла, получаем списко строк, который можно перебрать через цикл
for line in file.readlines():
    print(line.strip())         # разделяет строки, убирает символ конец строки (\n)


# for line in file:
#     print(line.strip())         # разделяет строки, убирает символ конец строки (\n)


# print(file.read(8))             # чтение 8 символов из файла


# print(file.readline())          # чтение одной строки из файла
