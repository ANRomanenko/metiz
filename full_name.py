# Использование переменных в строках с помощью f (f-строки (форматированная строка))

first_name = "Andrey"
last_name = "Romanenko"
full_name = f"{first_name} {last_name}"
print(full_name + "\n")

first_name = "andrey"
last_name = "romanenko"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()} \n")

first_name = "andrey"
last_name = "romanenko"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.upper()}"
print(message)