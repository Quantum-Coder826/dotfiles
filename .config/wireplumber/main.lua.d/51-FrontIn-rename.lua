rule = {
  matches = {
    {
      { "node.name", "equals", "alsa_input.pci-0000_0c_00.4.analog-stereo" },
    },
  },
  apply_properties = {
    ["node.description"] = "Front Input",
  },
}

table.insert(alsa_monitor.rules, rule)
