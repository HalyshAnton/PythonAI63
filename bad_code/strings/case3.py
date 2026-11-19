text = input("Введіть рядок англійською мовою: ")

count = 0
for letter in text:
    if "aeiou" in letter:
        count += 1

print(f"Кількість голосних літер: {count}")
