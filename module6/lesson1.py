# # дз
#
# while True:
#     if 2 + 2 == 4:
#         break
#         continue
#
#     # всі погані випадки краще перевіряти одразу
#     if name == "":
#         continue
#
#     if age < 0:
#         continue
#
#     text = input()


# рядки


# # створення
#
# a = 'Привіт'           # одинарні лапки
# b = "Привіт"           # подвійні лапки
#
# c = """Це рядок
# з кількох
# рядків"""              # потрійні лапки
#
# print(c)


# # об'єднання рядків
#
# name = "Олена"
# hello = "Привіт, " + name + "!"
#
# print(hello)  # Привіт, Олена!
# print(f"Привіт, {name}!")


# # множення на ціле число
#
# text = "ха" * 4  # повторити ха 4 рази
# print(text)
#
# print("-" * 20)
#
# # не можна множити на дробові числа
# "helo" * 3.5


# result = min(3, 7)
# print(result)

# знайти довжину рядка(кількість символів)

# text = "Python! "
#
# length = len(text)
# print(f"в слові {text} рівно {length} символів")


# цикл for
# for number in range(3):
#     print(number)       # 0 1 2
#
# for symbol in "abc":
#     print(symbol)       # a b c

# text = "Hello, world"
#
# for symbol in text:
#     print(symbol)


# print("M" == "m")
# print("Python" == "python")

# text = "Мама мила раму"
#
# if "мама" in text:
#     print("yes")
# else:
#     print("no")
#
#
# # запереченя
# if "зброя" not in text:
#     print("no")
# else:
#     print("yes")


# функції та методи

# [назва іункції](параметри)
# print("hello")
# num = input("введіть число")
# result = min(3, 7)


# # [об'єкт].[назва методу](параметри)
#
# text = "Pythont"
#
# # перевести в нижній регіст
# lower_text = text.lower()
# print(f"{lower_text = }")
#
# # перевести в верхній регіст
# upper_text = text.upper()
# print(f"{upper_text = }")
#
# # порахувати конвретну літеру
# count_t = text.count("t")
# print(f"{count_t = }")

# phrase = "Я люблю каву"
# new = phrase.replace("каву", "чай")
#
# print(new) # Я люблю чай
# print("banana".replace("a", "o"))
# # bonono

# text = "Python 3.12"
#
# # знайти цифри в тексті
# for ch in text:
#     if ch.isdigit():
#         print(f"{ch} -- цифра")
#     else:
#         print(f"{ch} -- щось інше")


# позбутись білих символів
user_text = input("Введіть текст: ")

# позбутись пропусків по краях
user_text = user_text.strip()

if user_text:  # user_text != ""
    print(user_text)
else:
    print("ви нічого не ввели")
