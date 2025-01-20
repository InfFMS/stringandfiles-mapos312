# Откройте текстовый файл task2.txt для чтения.
# Считайте его содержимое в строку.
# Найдите и замените все вхождения слова "Python" на слово "Питон" (регистр учитывать).
# Запишите обновленный текст в новый файл с другим именем.
# Выведите на экран сообщение о количестве произведённых замен.
with open ('task2.txt', 'r', encoding='utf-8') as f:
    x = f.read()
with open ('task2new.txt', 'w', encoding='utf-8') as new_file:
    new_file.write(x.replace("Python","Питон" ))
z=x.count("Python")
print(z)