rule = {
  matches = {
    {
      { "node.name", "equals", "alsa_input.usb-Kingston_HyperX_Virtual_Surround_Sound_00000000-00.analog-stereo"},
    },
  },
  apply_properties = {
    ["node.description"] = "Headset mic",
  },
}

table.insert(alsa_monitor.rules, rule)
