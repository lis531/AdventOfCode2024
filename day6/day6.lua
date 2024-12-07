local blockadeIndex = {}
local guardIndex = {}

local lines = {}
for line in io.lines("E:\\AdventOfCode2024\\day6\\input.txt") do
  table.insert(lines, line)
end

local lineLength = #lines[1]

-- Find blockades and guard positions
for row, line in ipairs(lines) do
    for col = 1, #line do
        local char = line:sub(col, col)
        if char == "#" then
            table.insert(blockadeIndex, {index = row, position = col})
        elseif char == "^" then
            table.insert(guardIndex, {index = row, position = col})
        end
    end
end

local direction = {-1, 0, 1}  -- {row, col, index}
local allPositions = {}

while true do
    local guard = guardIndex[1]
    local guardRow = guard.index
    local guardCol = guard.position

    -- Check if the guard is within bounds
    if guardRow > 0 and guardRow <= #lines and guardCol > 0 and guardCol <= lineLength then
        local alreadyVisited = false
        for _, pos in ipairs(allPositions) do
            if pos.index == guardRow and pos.position == guardCol then
                alreadyVisited = true
                break
            end
        end

        -- Only add the position if it hasn't been visited already
        if not alreadyVisited then
            table.insert(allPositions, {index = guardRow, position = guardCol})
        end

        -- Check if the guard encounters a blockade at its future position
        local blocked = false
        local futureRow = guardRow + direction[1]
        local futureCol = guardCol + direction[2]
        for _, blockade in ipairs(blockadeIndex) do
            if blockade.index == futureRow and blockade.position == futureCol then
                blocked = true
                break
            end
        end

        if blocked then
            if direction[3] == 1 then
                direction = {0, 1, 2} -- Right
            elseif direction[3] == 2 then
                direction = {1, 0, 3} -- Down
            elseif direction[3] == 3 then
                direction = {0, -1, 4} -- Left
            elseif direction[3] == 4 then
                direction = {-1, 0, 1} -- Up
            end
        else
            -- Move the guard
            guard.index = guardRow + direction[1]
            guard.position = guardCol + direction[2]
        end
    else
        break
    end
end

print("Guard visited " .. #allPositions .. " positions.")