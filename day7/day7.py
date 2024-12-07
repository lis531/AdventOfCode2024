import time
start = time.time()
with open("day7/input.txt", "r") as file:
    content = file.read()
    sections = content.split("\n")
    finalSum = 0

    for line in sections:
        supposedSum = int(line.split(":")[0])
        numbers = line.split(":")[1].strip().split(" ")
        for i in range(len(numbers)):
            numbers[i] = int(numbers[i])

        if sum(numbers) == supposedSum:
            finalSum += supposedSum
            continue

        for i in range(2 ** (len(numbers) - 1)):
            operations = []
            tempSum = numbers[0]

            for j in range(len(numbers) - 1):
                if (i // (2**j)) % 2 == 1:
                    tempSum *= numbers[j + 1]
                else:
                    tempSum += numbers[j + 1]
                if tempSum > supposedSum:
                    break

            if tempSum == supposedSum:
                finalSum += supposedSum
                break

end = time.time()
print(finalSum, (end-start) * 1000.0, "ms")