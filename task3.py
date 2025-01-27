# Откройте текстовый файл task3.txt для чтения.
# Извлеките все уникальные слова из файла (слова разделяются пробелами и знаками пунктуации).
# Подсчитайте, сколько раз каждое уникальное слово встречается в тексте.
# Запишите результаты в новый файл в формате:
# слово1: количество
# слово2: количество
#
# Убедитесь, что слова записаны в алфавитном порядке.
from collections import Counter
with open('task3.txt', 'r', encoding='utf-8') as f:
    x = f.read()
y = x.replace(".", " ").replace(",", " ")
b = y.lower().split()
a = Counter(b)
with open('task3new.txt', 'w', encoding='utf-8') as new_file:
    for word in sorted(a):
        new_file.write(f"{word}: {a[word]}\n")