local manaFlower = peripheral.find("manaFlower")
local blockReader = peripheral.find("blockReader")

redstone.setOutput("top", false) -- turn off the redstone output

while true do
    if string.find(blockReader.getBlockName(), "log") then -- check if tree has grown
        -- count over a duration to enshure the plant is empty
        zeroCount = 0
        for i = 1, 10 do
            if manaFlower.getMana() == 0 then
                zeroCount = zeroCount + 1
            else
                zeroCount = 0
            end
            sleep(1) -- wait for 1 second
        end

        if zeroCount == 10 then
            redstone.setOutput("top", true) -- turn on the redstone output
            print("trigger")
        end
    else
        redstone.setOutput("top", false) -- turn off the redstone output
    end
end
