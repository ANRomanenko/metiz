# Перебор всего списка

magicians = ['alice', 'davice', 'carolina'] # определяем наш список фокусников
for magician in magicians: # с помощью цикла for мы проходимся по всем элементам списка и выводим его по очередно в столбец!
    print(magician) # выводим имена фокусников
print()
# Стоит выбирать осмысленное имя описывающее отдельный элемент списка!
# for cat in cats:
# for dog in dogs:
# for item in list_of_items:

# Более сложные действия в циклах for
magicians = ['alice', 'davice', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!") # здесь мы выводим для всех фокусников одинаковое сообщение
    print(f"I can't wait to see your next trick, {magician.title()}.\n") # а здесь выводим для каждого фокусника своё сообщение

# Выполнение действий после цикла for
magicians = ['alice', 'davice', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great magic show!") # Первые две команды print повторяются по одному разу для каждого фокусника в списке, как было показано ранее. Но поскольку строка  отступа не имеет, это сообщение выводится только один раз:
print()

# Предотвращение ошибок с отступами