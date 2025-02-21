# Напишите программу, которая просит пользователя ввести несколько предложений (например, 5, каждое предложение с новой строки).
# Каждое введенное предложение записывается в файл, но:
# Слова во всех предложениях должны быть приведены к верхнему регистру.
# Между словами вместо пробела ставится символ "_".
# После записи откройте этот файл, считайте содержимое и выведите его на экран.
a= [input() for _ in range(5)]
# капсим и заменяем пробелы на "_"
x = [b.upper().replace(" ", "_") for b in a]
# Записываем преобразованные предложения в файл
with open('task4new.txt', 'w', encoding='utf-8') as file:
    file.write('\n'.join(x))
# Читаем содержимое файла и выводим
with open('task4new.txt', 'r', encoding='utf-8') as file:
    print("\n")
    print(file.read())