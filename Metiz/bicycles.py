# Что такое список?


# создаём список велосипедов
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles) # (распечатываем) выводим наш список велосипедов
print()

# Обращение к элементам списка
bicycles = ['trek', 'cannondale', 'redline', 'specialize']
print(bicycles[0].title()) # обращаемся к первому элементу в списке (Python начинает отсчёт с нуля)
print(bicycles[1].title())
print(bicycles[3].title())
print(bicycles[-1].title())
print()

# Использование отдельных элементов из списка
bicycles = ['trek', 'cannondale', 'redline', 'specialize']
message = f"My first bicycles was a {bicycles[0].title()}."
print(message)
print()

# Упражнения (3.1) Имена:
names = ['maxim', 'shasa', 'sergey', 'ivan']
print(names[0].title())
print(names[1].title())
print(names[-2].title())
print(names[-1].title())
print()
# Улучшения упражнения 3.1 с применением цикла for:
names = ['maxim', 'shasa', 'sergey', 'ivan']
for name in names:
    print(name.title())

print()
# Упражнения (3.2) Сообщения:
names = ['maxim', 'shasa', 'sergey', 'ivan']
print(f"Приезжай сегодня на шашлык {names[0].title()}")
print(f"Приезжай сегодня на шашлык {names[1].title()}")
print(f"Приезжай сегодня на шашлык {names[-2].title()}")
print(f"Приезжай сегодня на шашлык {names[-1].title()}")
print()

# Упражнения (3.3) Собственный список:
cars = ['audi', 'toyota', 'ford', 'volkswagen']
for msg in cars:  # Здесь я использовал цикл for для выводы всех элементов в списке!
    print(f"Я бы хотел купить автомобиль: {msg.title()}")