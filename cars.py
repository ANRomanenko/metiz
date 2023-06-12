
# Упорядочение списка

# Постоянная сортировка списка методом sort()
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() # теперь название машин распологается в алфавитном порядке
print(cars)
print()

# Список также можно отсортировать в обратном алфавитном порядке
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True) # Сортируем список в обратном порядке с помощью reverse=True!
print(cars) # Выводим результат на экран!
print()

# Временная сортировка списка функцией sorted()

# Оригинальный список!
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)

# Временно отсортированный список!
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the sorted list:")
print(sorted(cars))

# Временно отсортированный список в обратном порядке!
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the sorted reverse list:")
print(sorted(cars, reverse=True))

# Снова оригинальный список хранится в исходном порядке!
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the original list again:")
print(cars)
print()

# Вывод списка в обратном порядке при помощи метода reverse()!
# reverse()
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse() # метод reverse() выводит наш список в обратном порядке!
print(cars)
cars.reverse() # можно также вернутся к обратному списку снова применив метод reverse()!
print(cars)
print()

# Определение длины списка при помощи функции len()!
# len()
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars)) # мы получили ответ что в нашем списке находится 4 элемента!
print()

# Упражнения (3.8) Повидать мир: --------------------
# Обычный список
countries = ['spain', 'italy', 'brazilia', 'usa', 'singapur']
print("Обычный список!")
print(countries)

# Изменённый список!
# С помощью функции sorted()
countries = ['spain', 'italy', 'brazilia', 'usa', 'singapur']
print("\nВывожу список при помощи функции sorted() без постоянного изменения списка!")
print(sorted(countries))

# Список по-прежнему хранится в исходном порядке!
countries = ['spain', 'italy', 'brazilia', 'usa', 'singapur']
print("\nСписок по-прежнему хранится в исходном порядке!")
print(countries)

# Вывод списка в обратном алфавитном порядке без изменения порядка исходного списка!
# При помощи функции sorted(countries, reverse=True)
countries = ['spain', 'italy', 'brazilia', 'usa', 'singapur']
print("\nВывод списка в обратном порядке без изменения порядка исходного списка!")
print(sorted(countries, reverse=True))

# Список по-прежнему хранится в исходном порядке!
countries = ['spain', 'italy', 'brazilia', 'usa', 'singapur']
print("\nСписок по-прежнему хранится в исходном порядке!")
print(countries)

# Изменения порядка элементов вызовом reverse()
countries = ['spain', 'italy', 'brazilia', 'usa', 'singapur']
countries.reverse()
print("\nИзменение порядка элементов вызовом reverse() - элементы следуют в другом порядке!")
print(countries)
countries.reverse()
print("\nСписок вернулся к исходному порядку!")
print(countries)

# Отсортируем список в алфавитном порядке при помощи вызоват sort()
countries = ['spain', 'italy', 'brazilia', 'usa', 'singapur']
countries.sort()
print("\nЭлементы следуют в алфавитном порядке!")
print(countries)
countries.sort(reverse=True)
print("\nСортировка списка в обратно алфавитном порядке - порядок элементов изменился")
print(countries)