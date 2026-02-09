#!/bin/bash
caps_state=$(hyprctl devices -j | jq '.keyboards[] | select(.name=="keychron-keychron-q11") 
                                     | .capsLock')
if [[ $caps_state == "true" ]]; then
  echo "󰪛 "
else
  echo ""
fi
