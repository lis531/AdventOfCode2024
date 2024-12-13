import time

start = time.time()

with open("day11/input.txt", "r") as file:
    result = 0
    numbers = []
    for line in file:
        numbers.extend(line.strip().split(" "))

for _ in range(25):
    new_numbers = []
    for number in numbers:
        if number == "0":
            new_numbers.append("1")
        elif len(number) % 2 == 0:
            mid = len(number) // 2
            new_numbers.append(number[:mid])
            new_numbers.append(str(int(number[mid:])))
        else:
            new_numbers.append(str(int(number) * 2024))
    numbers = new_numbers

result = len(numbers)

end = time.time()
print(result, (end - start) * 1000.0, "ms")
