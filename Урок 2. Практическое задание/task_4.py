"""
4. Пользователь вводит строку из нескольких слов,
разделённых пробелами. Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если слово длинное,
выводить только первые 10 букв в слове.

Пример:
Введите слова через пробел: раз два три
1. раз
2. два
3. три

Введите слова через пробел: раз перерефрижерированность
1. раз
2. перерефриж
"""

ls = input("Введите слова: ").split()
a = 1
for text in ls:
    if len(text) > 10:
        print(f"{a} - {text[:10]}")
    else:
        print(a, "-", text)
    a += 1
