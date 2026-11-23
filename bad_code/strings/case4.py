text = input("Введіть рядок: ")

start = float(input("Введіть початковий індекс: "))
end = float(input("Введіть кінцевий індекс: "))

segment = text[start, end]

print(segment)
