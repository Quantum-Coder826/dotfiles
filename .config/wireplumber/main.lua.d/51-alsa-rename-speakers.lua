rule = {
  matches = {
    {
      { "node.name", "equals", "alsa_output.usb-harman_kardon_SoundSticks-00.analog-stereo" },
    },
  },
  apply_properties = {
    ["node.description"] = "Speakers",
  },
}

table.insert(alsa_monitor.rules, rule)
