import time
with open("day5/input.txt", "r") as file:
    content = file.read()

sections = content.strip().split("\n\n")
rulesLines = sections[0].split("\n")
numbersLines = sections[1].split("\n")

start = time.time()

suma = 0

for numberLine in numbersLines:
    shouldAdd = True
    numbers = []
    for number in numberLine.split(","):
        numbers.append(int(number))
    for rules in rulesLines:
        if int(rules.split("|")[0]) in numbers and int(rules.split("|")[1]) in numbers:
            if numbers.index(int(rules.split("|")[0])) > numbers.index(int(rules.split("|")[1])):
                shouldAdd = False
                break

    if shouldAdd:
        suma += numbers[len(numbers) // 2]

end = time.time()
print(suma, (end-start) * 1000.0, "ms")
