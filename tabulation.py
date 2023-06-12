# Табуляция и разрывы строк
# \t (это у нас табуляция)
# \n (разрывы строк)


print("Python")
print("\tPython\n")

print("Languages:\nPython\nC\nJavaScript\n")

print("Languages:\n\tPython\n\tC\n\tJavaScript\n")

favorite_language = "python "
favorite_language.rstrip()
print(favorite_language)

favorite_language = " python"
print(favorite_language)
favorite_language = favorite_language.lstrip()
print(favorite_language)
print(favorite_language)
print()

favorite_language = " python "
favorite_language = favorite_language.strip()
print(favorite_language)
print(favorite_language)
print()

login = input("Введите ваш login: ")
login = login.strip() # Это усеченное значение (исходная переменная)
password = input("Введите ваш password: ")
password = password.strip()
print(f"\nВаш login: {login}\nВаш password: {password}")