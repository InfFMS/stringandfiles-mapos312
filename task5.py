# Откройте текстовый файл task5.txt для чтения.
# Найдите самое длинное слово в тексте. Если таких слов несколько, выберите первое из них.
# Запишите это слово и его длину в новый файл в формате:
# Самое длинное слово: слово
# Его длина: длина
#
# Выведите это слово и длину в консоль.
with open('task5.txt', 'r', encoding='utf-8') as f:
    x = f.read()
y = x.replace(".", "").replace(",", "").replace("!", "").split()
print(y)
a = ''
for b in y:
    if len(b) > len(a):
        a = b
l=len(a)
with open('task5new', 'w', encoding='utf-8') as new_file:
    new_file.write(f"{a}\n")
    new_file.write(f"{l}\n")
print(a)
print(l)
