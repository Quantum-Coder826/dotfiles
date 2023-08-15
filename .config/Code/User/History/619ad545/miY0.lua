local blockReader = peripheral.find("blockReader")
local justFed = false

redstone.setOutput("back", false) -- turn off the redstone output

while true do
    data = blockReader.getBlockData() -- get all nbt from the munchdew
    if data["cooldown"] > 0 and not justFed then -- if the munchdew is on cooldown replant the tree
        redstone.setOutput("back", true) -- turn on the redstone output
        print("triggerd")
        justFed = true
    elseif data["cooldown"] == 0
        redstone.setOutput("back", false) -- 
    end
end
