monitor.alsa.rules = [
  {
    matches = [
      {
        device.name = "alsa_card.pci-0000_0a_00.1" 
      }
    ]
    actions = {
      update-props = {
	 node.description = "GTX 1660 HDMI"
         device.disabled = true
      }
    }
  }
]
