# списки

# створення через list

# num_str = "34"
# num_int = int(num_str)
#
# print(num_int * 10)


# послідовністі -- range, str, list

# num = "123456"
# num_list = list(num)
#
# print(num_list)


# nums = list(range(10, 20))
# print(nums)


# порожній список

# users = []

animals = ["кіт", "пес", "миша"]
ages = [24, 48, 67]

# for animal in animals:
#     print(animal)


# print("кіт" in animals)
# print("хом'як" in animals)
# print("Кіт" in animals)
# print("к" in animals)

# print(48 in ages)
# print(47 in ages)
# print("кіт" in ages)
#
# print("кіт" not in ages)

# інлексація

colors = ["червоний", "зелений", "синій", "жовтий"]
#              0           1         2        3
#             -4          -3        -2       -1

# print(colors[1])
# print(colors[1:3])

# word = "зелений"
# word[0] = "t"

# colors[0] = "фіолетовий"
# print(colors)


# colors_copy = colors.copy()
#
# colors[0] = "фіолетовий"
# print(f"{colors = }")
#
# print(f"{colors_copy = }")


# є список зарплат, треба всім зробити надбавку 200 доларів

salaries = [800, 1000, 1500]

# проходимось по кожній зарплаті і збільшуємо її на 200
# for salary in salaries:
#     salary += 200
#     print(salary)
#
# print(f"{salaries = }")

# for i in range(len(salaries)):
#     salaries[i] += 200
#
# print(f"{salaries = }")

names = ["Оля", "Іван", "Маша", "Іван"]


# if "Іван" in names:
#     names.remove("Іван")
#
# print(names)


names.append("Богдан")

print(names)

masha = names.pop(2)

print(masha)
print(names)
