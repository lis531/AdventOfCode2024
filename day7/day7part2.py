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

        for i in range(3 ** (len(numbers) - 1)):
            shouldBreak = False
            operations = []
            tempSum = numbers[0]

            for j in range(len(numbers) - 1):
                operation = (i // (3**j)) % 3
                if operation == 1:
                    tempSum *= numbers[j + 1]
                elif operation == 2:
                    tempSum += numbers[j + 1]
                else:
                    tempSum = int(str(tempSum) + str(numbers[j + 1]))
                if tempSum > supposedSum:
                    shouldBreak = True
                    break

            if tempSum == supposedSum:
                finalSum += supposedSum
                break

end = time.time()
print(finalSum, (end-start) * 1000.0, "ms")