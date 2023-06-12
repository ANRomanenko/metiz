import this


# Упражнение (2.3) Личное сообщение:
name = "eric"
print(f"Hello {name.title()}, would you like to learn some Python today?")
print()

# Упражнение (2.4) Регистр символов в именах:
name = "Enrice iglesias"
print(name.lower()) # нижний регистр
print(name.upper()) # верхний регистр
print(name.title()) # вывод с начальных букв
print()

# Упражнение (2.5) Знаменитая цитата:
msg = '\tAlbert Einstein once said, "A person who never made\n\ta mistake never tried anything new."'
print(msg)
print()

# Упражнение (2.6) Знаменитая цитата 2:
famous_person = 'Albert Einstein'
message = f'\t{famous_person} once said, "A person who never made\n\ta mistake never tried anything new."'
print(message)
print()

# Упражнение (2.7) удаление пропусков:
name_person = '     \tAlbert Einstein\n   '
print(name_person)
print(name_person.lstrip())
print(name_person.rstrip())
print(name_person.strip())
print()
# ---------------

universe_age = 14_000_000_000
print(universe_age)
print()

x, y, z = 0, 0, 0 # множественное присваивание переменных
print(x, y, z)
print()

# Упражнение (2.8) Число 8: (Все числа в примере будут равняться числу "8")
print(5 + 3) # сложение
print(10 - 2) # вычитание
print(16 / 2) # деление
print(2 * 4) # умножение
print()

number = 15
text = f"Моё любимое число {number}!"
print(text)