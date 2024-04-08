rule = {
  matches = {
    {
      { "node.name", "equals", "alsa_output.pci-0000_0c_00.4.iec958-stereo" },
    },
  },
  apply_properties = {
    ["node.description"] = "Front Output",
  },
}

table.insert(alsa_monitor.rules, rule)
