items = input("Введіть ваші речі: ")
items = items.lower

if "ніж" or "гроші" or "отрута" in items:
    print("У вас є речі які заборонено перевозити")
else:
    print("Оформлено доставку")
