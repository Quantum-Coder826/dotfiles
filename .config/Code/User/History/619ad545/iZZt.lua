local manaFlower = peripheral.find("manaFlower")

redstone.setOutput("back", false) -- turn off the redstone output

function checkValue(value)
    local zeroCount = 0
    
    for i = 1, 5 do
        if value == 0 then
            zeroCount = zeroCount + 1
        else
            zeroCount = 0
        end
        
        sleep(1) -- wait for 1 second
    end
    
    if zeroCount == 5 then
        redstone.setOutput("back", true)
        zeroCount = 0
    else
        redstone.setOutput("back", false) -- turn off the redstone output
        zeroCount = 0
    end
end


while true do 
    checkValue(manaFlower.getMana())
end