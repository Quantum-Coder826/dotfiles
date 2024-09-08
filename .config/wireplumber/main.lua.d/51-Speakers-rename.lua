rule = {
  matches = {
    {
      { "node.name", "equals",  "alsa_output.pci-0000_0c_00.4.analog-stereo" },
    },
  },
  apply_properties = {
    ["node.description"] = "Speakers",
    ["node.nick"] = "Logi Z702",
  },
}

table.insert(alsa_monitor.rules, rule)
