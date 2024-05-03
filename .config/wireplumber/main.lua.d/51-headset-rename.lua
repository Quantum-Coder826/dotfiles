rule = {
  matches = {
    {
      { "node.name", "equals",  "alsa_output.usb-Kingston_HyperX_Virtual_Surround_Sound_00000000-00.iec958-stereo" },
    },
  },
  apply_properties = {
    ["node.description"] = "Headset",
  },
}

table.insert(alsa_monitor.rules, rule)
