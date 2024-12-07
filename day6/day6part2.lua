local blockadeIndex = {}
local guardPosition = nil
local possibleReplacements = {}

local lines = {}
for line in io.lines("E:\\AdventOfCode2024\\day6\\input.txt") do
    table.insert(lines, line)
end

local lineLength = #lines[1]

for row, line in ipairs(lines) do
    for col = 1, #line do
        local char = line:sub(col, col)
        if char == "#" then
            table.insert(blockadeIndex, {row = row, col = col})
        elseif char == "^" then
            guardPosition = {row = row, col = col}
        elseif char == "." then
            table.insert(possibleReplacements, {row = row, col = col})
        end
    end
end

local directions = {
    {dx = -1, dy = 0},  -- Up
    {dx = 0, dy = 1},   -- Right
    {dx = 1, dy = 0},   -- Down
    {dx = 0, dy = -1}   -- Left
}

local possibleLoops = 0

for _, replacement in ipairs(possibleReplacements) do
    local grid = {}
    for i, line in ipairs(lines) do
        grid[i] = line
    end
    
    grid[replacement.row] = grid[replacement.row]:sub(1, replacement.col - 1) .. "#" .. grid[replacement.row]:sub(replacement.col + 1)

    local guardRow = guardPosition.row
    local guardCol = guardPosition.col
    local directionIndex = 1

    local visited = {}
    local loopDetected = false

    while true do
        local key = guardRow .. "," .. guardCol .. "," .. directionIndex
        if visited[key] then
            loopDetected = true
            break
        else
            visited[key] = true
        end

        local dir = directions[directionIndex]
        local nextRow = guardRow + dir.dx
        local nextCol = guardCol + dir.dy

        -- Check bounds
        if nextRow < 1 or nextRow > #grid or nextCol < 1 or nextCol > lineLength then
            break
        end

        local nextChar = grid[nextRow]:sub(nextCol, nextCol)
        if nextChar == "#" then
            -- Blocked
            directionIndex = (directionIndex % 4) + 1
        else
            -- Move forward
            guardRow = nextRow
            guardCol = nextCol
        end
    end

    if loopDetected then
        possibleLoops = possibleLoops + 1
    end
end

print("Guard could fall in infinite loop " .. possibleLoops .. " times.")
