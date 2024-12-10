import time
start = time.time()

with open("day9/input.txt", "r") as file:
    result = 0
    individualBlocks = []
    allBlocks = []

    for line in file:
        for char in line.strip():
            allBlocks.append(int(char))

    for i in range(len(allBlocks)):
        for j in range(allBlocks[i]):
            if i % 2 == 0:
                individualBlocks.append(i // 2)
            else:
                individualBlocks.append(".")

index = 0
while index < len(individualBlocks):
    if individualBlocks[index] == ".":
        if individualBlocks[-1] == ".":
            individualBlocks.pop()
        else:
            individualBlocks[index] = individualBlocks[-1]
            individualBlocks.pop()
    else:
        index += 1

for i in range(len(individualBlocks)):
    result += i * individualBlocks[i]

end = time.time()
print(result, (end - start) * 1000.0, "ms")
