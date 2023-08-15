local blockReader = peripheral.find("blockReader")

redstone.setOutput("back", false) -- turn off the redstone output

while true do
    data = blockReader.getBlockData()
    if data["ateOnce"] == 1 and data["cooldown"] == 0 then
        redstone.setOutput("back", true)
    else 
end
