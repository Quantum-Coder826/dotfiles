rule = {
  matches = {
    {
      { "device.name", "equals", "alsa_card.pci-0000_0a_00.1" },
    },
  },
  apply_properties = {
    ["node.description"] = "Front Input",
    ["device.disabled"] = true,
  },
}

table.insert(alsa_monitor.rules, rule)
