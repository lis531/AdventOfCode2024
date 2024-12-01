file = open("day1/example.txt", "r")
arr1 = []
arr2 = []
distanceSum = 0

for line in file:
    arr1.append(int(line.split("   ")[0]))
    arr2.append(int(line.split("   ")[1]))

arr1.sort()
arr2.sort()

for i in range(len(arr1)):
    distanceSum += arr2[i] - arr1[i] if arr2[i] > arr1[i] else arr1[i] - arr2[i]

print(distanceSum)