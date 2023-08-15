local blockReader = peripheral.find("blockReader")
local eating = false

redstone.setOutput("back", false) -- turn off the redstone output

while true do
    data = blockReader.getBlockData()
    if data["ateOnce"] == 1 and data["cooldown"] >= 0 and not eating then
        
    end
end
