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

    for index in range(len(allBlocks), -1, -1):
        chars = []
        for i in individualBlocks:
            if i == index:
                chars.append(i)
        if not chars:
            continue

        file_length = len(chars)
        file_start = chars[0]

        free_space_start = 0
        freeLength = 0

        for i in range(len(individualBlocks)):
            if individualBlocks[i] == ".":
                if free_space_start == 0:
                    free_space_start = i
                freeLength += 1
                if freeLength == file_length:
                    break
            else:
                free_space_start = 0
                freeLength = 0

        if freeLength == file_length and free_space_start < file_start:
            for i in range(file_length):
                individualBlocks[free_space_start + i] = index
            for i in chars:
                individualBlocks[i] = "."

    for i in range(len(individualBlocks)):
        if individualBlocks[i] != ".":
            result += i * individualBlocks[i]

end = time.time()
print(result, (end - start) * 1000.0, "ms")
