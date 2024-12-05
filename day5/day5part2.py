with open("day5/input.txt", "r") as file:
    content = file.read()

sections = content.strip().split("\n\n")
rulesLines = sections[0].split("\n")
numbersLines = sections[1].split("\n")

suma = 0

for numberLine in numbersLines:
    shouldAdd = False
    numbers = []
    for number in numberLine.split(","):
        numbers.append(int(number))
    for number in numbers:
        for rules in rulesLines:
            if int(rules.split("|")[0]) in numbers and int(rules.split("|")[1]) in numbers:
                if numbers.index(int(rules.split("|")[0])) > numbers.index(int(rules.split("|")[1])):
                    temp = numbers[numbers.index(int(rules.split("|")[0]))]
                    numbers[numbers.index(int(rules.split("|")[0]))] = numbers[numbers.index(int(rules.split("|")[1]))]
                    numbers[numbers.index(int(rules.split("|")[1]))] = temp
                    shouldAdd = True

    if shouldAdd:
        suma += numbers[len(numbers) // 2]
print(suma)
