import time

start = time.time()
with open("day11/input.txt", "r") as file:
    numbersString = file.read().split()

numbers = {}
for num_str in numbersString:
    numbers[int(num_str)] = numbers.get(int(num_str), 0) + 1

for _ in range(10000):
    new_numbers = {}
    for number, count in numbers.items():
        if number == 0:
            new_numbers[1] = new_numbers.get(1, 0) + count
        else:
            length = len(str(number))
            if length % 2 == 0:
                mid = 10 ** (length // 2)
                first_half = number // mid
                second_half = number % mid
                new_numbers[first_half] = new_numbers.get(first_half, 0) + count
                new_numbers[second_half] = new_numbers.get(second_half, 0) + count
            else:
                new_num = number * 2024
                new_numbers[new_num] = new_numbers.get(new_num, 0) + count
    numbers = new_numbers

result = sum(numbers.values())

end = time.time()
print(result, (end - start) * 1000.0, "ms")