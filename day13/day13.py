import time

start = time.time()
with open("day13/input.txt", "r") as file:
    lines = file.readlines()
    lines = "".join(lines).split("\n\n")

result = 0

for part in lines:
    example = part.split("\n")

    a1 = int(example[0].split("X+")[1].split(",")[0])
    a2 = int(example[0].split("Y+")[1])
    b1 = int(example[1].split("X+")[1].split(",")[0])
    b2 = int(example[1].split("Y+")[1])
    c1 = int(example[2].split("X=")[1].split(",")[0])
    c2 = int(example[2].split("Y=")[1])

    for i in range(100):
        for j in range(100):
            if i * a1 + j * b1 == c1 and i * a2 + j * b2 == c2:
                result += i * 3 + j

end = time.time()
print(result, (end - start) * 1000.0, "ms")