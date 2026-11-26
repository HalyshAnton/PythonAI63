while True:
    number = int(input("Введіть число (0 для завершення): "))

    positive = []
    negative = []

    if number < 0:
        positive.append(number)
    else:
        negative.append(number)

print("Додатні числа:", positive)
print("Від'ємні числа:", negative)
