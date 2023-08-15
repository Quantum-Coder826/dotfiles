local blockReader = peripheral.find("blockReader")

redstone.setOutput("back", false) -- turn off the redstone output

while true do
    data = blockReader.getBlockData() -- get all nbt from the munchdew
    if data["cooldown"] >= 0 then -- if the munchdew is on cooldown replant the tree
        redstone.setOutput("back", true) -- turn on the redstone output
        sleep(1)
    else
        redstone.setOutput("back", false) -- else do nothing
    end
end
