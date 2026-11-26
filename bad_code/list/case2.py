days = int(input("Введіть кількість днів: "))

for i in range(days):
    temperatures = []
    temperature = float(input(f"Введіть температуру за {i + 1}-й день: "))
    temperatures.append(temperature)

print("Температури:", temperatures)

for i in range(days):
    difference = temperatures[i] - temperatures[i - 1]
    print(f"Різниця температур за {i + 1}-й день: {difference}")
