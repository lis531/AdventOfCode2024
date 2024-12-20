import time
start = time.time()
with open("day8/input.txt", "r") as file:
    content = file.read()
    lines = content.split("\n")
    antinodes = 0

    allLettersAndPositions = {}
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] != ".":
                # save the letter and its position
                allLettersAndPositions[(i, j)] = lines[i][j]
    lengthY = len(lines)
    lengthX = len(lines[0])

    allLettersAndPositionsCopy = allLettersAndPositions.copy()
    for letter in allLettersAndPositions:
        # for each letter type check if there is other letter with the same type
        letterType = allLettersAndPositions[letter]
        for otherLetter in allLettersAndPositions:
            otherLetterType = allLettersAndPositions[otherLetter]
            if letterType == otherLetterType:
                if letter == otherLetter:
                    pass
                else:
                    diffX = otherLetter[0] - letter[0]
                    diffY = otherLetter[1] - letter[1]
                    if letter[0] - (diffX) >= 0 and letter[1] - (diffY) < lengthX and letter[1] - (diffY) >= 0 and letter[0] - (diffX) < lengthY:
                        allLettersAndPositionsCopy[(letter[0] - (diffX), letter[1] - (diffY))] = "#"
                    if otherLetter[1] + (diffY) >= 0 and otherLetter[1] + (diffY) < lengthX and otherLetter[0] + (diffX) >= 0 and otherLetter[0] + (diffX) < lengthY:
                        allLettersAndPositionsCopy[(otherLetter[0] + (diffX), otherLetter[1] + (diffY))] = "#"
    
    for letter in allLettersAndPositionsCopy:
        if allLettersAndPositionsCopy[letter] == "#":
            antinodes += 1

end = time.time()
print(antinodes, (end-start) * 1000.0, "ms")