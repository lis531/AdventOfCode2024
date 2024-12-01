file = open("day1/example.txt", "r")
arr1 = []
arr2 = []
similarityScore = 0

for line in file:
    arr1.append(int(line.strip().split("   ")[0]))
    arr2.append(int(line.strip().split("   ")[1]))

arr1.sort()
arr2.sort()

for i in range(len(arr1)):
    similarityScore += arr1[i] * arr2.count(arr1[i])

print(similarityScore)