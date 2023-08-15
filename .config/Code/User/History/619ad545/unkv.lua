local blockReader = peripheral.find("blockReader")

redstone.setOutput("back", false) -- turn off the redstone output

while true do
    data = blockReader.getBlockData() -- get all nbt from the munchdew
    if data["cooldown"] >= 0 then
        redstone.setOutput("back", true)
    else
        redstone.setOutput("back", false)
    end
end
