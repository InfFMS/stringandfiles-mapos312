# Откройте текстовый файл для чтения task1.txt.
# Подсчитайте:
# Общее количество строк в файле.
# Общее количество слов во всем тексте файла.
# Общее количество символов (включая пробелы).
# Выведите полученную статистику на экран.
# Открываем файл для чтения
with open('task1.txt', 'r', encoding='utf-8') as f:
    x = f.read()

# считаю количество строк a
lines = x.splitlines()
a = len(lines)

with open('task1new.txt', 'w', encoding='utf-8') as new_file:
    new_file.write(x.replace("—", " "))

# Считаем количество слов b в новом файле
with open('task1new.txt', 'r', encoding='utf-8') as new_file:
    y = new_file.read()
b = len(y.split())

# количество символов c в исходном файле
c = len(x)

print(a)
print(b)
print(c)
