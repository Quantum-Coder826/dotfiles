rule = {
  matches = {
    {
      { "node.name", "equals",  "alsa_input.pci-0000_00_1f.3-platform-skl_hda_dsp_generic.HiFi__hw_sofhdadsp_6__source"},
    },
  },
  apply_properties = {
    ["node.description"] = "Laptop Mono Mic",
  },
}

table.insert(alsa_monitor.rules, rule)