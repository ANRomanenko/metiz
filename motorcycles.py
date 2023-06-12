# Изменение, добавление и удаление элементов
# Изменение элементов в списке

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati' # здесь мы меняем новое значение элемента honda на ducati
print(motorcycles) # теперь первым в списке стоит у нас ducati
print()


# Добавления элементов в список
# Присоединение элементов в конец списка
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati') # метод append добавляет новый элемент в конец списка!
print(motorcycles)
print()

newlist = []
newlist.append('honda')
newlist.append('yamaha')
newlist.append('suzuki')
print(newlist)
print()

# Вставка элементов в список
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati') # Добавляем новый элемент в произвольную позицию списка (указуем идекс и значение нового элемента)
print(motorcycles)
print()

# Удаление элементов из списка
# В обоих примерах значение, удаленное из списка после использования команды del, становится недоступным.
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)
print()

# Удаление элемента с использованием метода pop()
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles) # весь список
popped_motorcycles = motorcycles.pop() # метод pop, удаляет последний элемент из списка!
print(motorcycles) # в списке отсутствует "suzuki"
print(popped_motorcycles) # выводит "suzuki"
print()

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}")
print(last_owned.upper())
print()

# Извлечение элементов из произвольной позиции списка
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0) # для этого следует указать индекс удаляемого элемента в круглых скобках.
print(f"The last motorcycle I owned was a {first_owned.title()}")
print(first_owned.title())
print()

# Удаление элементов по значению
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
print()

# Следующая программа удаляет значение 'ducati' и выводит причину удаления:
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.\n")

# Упражнения (3.4) Список гостей:
guests = ['maxim', 'sergey', 'kolia'] # Это пример вывода сообщеия через цикл!
for msg in guests:
    print(f"Привет {msg.title()}, приглашаю тебя сегодня на шашлыки!")
print()

guests = ['maxim', 'sergey', 'kolia'] # Это пример вывода сообщения через элемент индекса
print(f"Привет {guests[0].title()}, приглашаю тебя сегодня на шашлыки!")
print(f"Привет {guests[1].title()}, приглашаю тебя сегодня на шашлыки!")
print(f"Привет {guests[2].title()}, приглашаю тебя сегодня на шашлыки!\n")

# Упражнения (3.5) Изменение списка гостей:
guests = ['maxim', 'sergey', 'kolia']
print(f"Привет {guests[0].title()}, приглашаю тебя сегодня на шашлыки!")
print(f"Привет {guests[1].title()}, приглашаю тебя сегодня на шашлыки!")
print(f"Привет {guests[2].title()}, приглашаю тебя сегодня на шашлыки!")
print(f"{guests[1].title()} придти сегодня не сможет!")
guests[1] = 'valera'
valera = f"Новый приглашаемый {guests[1].title()}!\n"
print(valera)
print(f"Привет {guests[0].title()}, приглашаю тебя сегодня на шашлыки!")
print(f"Привет {guests[1].title()}, приглашаю тебя сегодня на шашлыки!")
print(f"Привет {guests[2].title()}, приглашаю тебя сегодня на шашлыки!\n")

# Упражнения (3.6) Больше гостей::
guests = ['maxim', 'sergey', 'kolia']
print(f"Привет {guests[0].title()}, приглашаю тебя сегодня на шашлыки!")
print(f"Привет {guests[1].title()}, приглашаю тебя сегодня на шашлыки!")
print(f"Привет {guests[2].title()}, приглашаю тебя сегодня на шашлыки!")
print("Наш список гостей будет расширен!")
guests.insert(0, 'dima')
guests.insert(2, 'vlad')
guests.insert(-1, 'vitaliy')
print()
print(f"Привет {guests[0].title()}, приглашаю тебя сегодня на шашлыки!")
print(f"Привет {guests[1].title()}, приглашаю тебя сегодня на шашлыки!")
print(f"Привет {guests[2].title()}, приглашаю тебя сегодня на шашлыки!")
print(f"Привет {guests[3].title()}, приглашаю тебя сегодня на шашлыки!")
print(f"Привет {guests[4].title()}, приглашаю тебя сегодня на шашлыки!")
print(f"Привет {guests[5].title()}, приглашаю тебя сегодня на шашлыки!\n")

# Упражнения (3.7) Сокращение списка гостей:
guests = ['maxim', 'sergey', 'kolia']
# выбираем имя по элементу из нашего списка приглашённых гостей
print(f"Привет {guests[0].title()}, приглашаю тебя сегодня на шашлыки!")
print(f"Привет {guests[1].title()}, приглашаю тебя сегодня на шашлыки!")
print(f"Привет {guests[2].title()}, приглашаю тебя сегодня на шашлыки!")
print("Наш список гостей будет расширен!")
guests.insert(0, 'dima')
guests.insert(2, 'vlad')
guests.insert(-1, 'vitaliy')
print()
print(f"Привет {guests[0].title()}, приглашаю тебя сегодня на шашлыки!")
print(f"Привет {guests[1].title()}, приглашаю тебя сегодня на шашлыки!")
print(f"Привет {guests[2].title()}, приглашаю тебя сегодня на шашлыки!")
print(f"Привет {guests[3].title()}, приглашаю тебя сегодня на шашлыки!")
print(f"Привет {guests[4].title()}, приглашаю тебя сегодня на шашлыки!")
print(f"Привет {guests[5].title()}, приглашаю тебя сегодня на шашлыки!\n")
print("На обед приглашаются только 2 гостя! Так как новый стол для гостей не успевают привезти вовремя!\n")
kolia = guests.pop()
print(f"{kolia.title()} я сожаленю об отменене приглашения!")
vitaliy = guests.pop()
print(f"{vitaliy.title()} я сожаленю об отменене приглашения!")
sergey = guests.pop()
print(f"{sergey.title()} я сожаленю об отменене приглашения!")
vlad = guests.pop()
print(f"{vlad.title()} я сожаленю об отменене приглашения!\n")
print(f'{guests[0].title()} более ранне приглашение остаётся в силе!')
print(f'{guests[1].title()} более ранне приглашение остаётся в силе!')
del guests[0:2]
print(guests)
