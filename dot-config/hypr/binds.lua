---------------------
--- Hypr Keybinds ---
---------------------
local Mod = "SUPER"

--- Navigation and Windowmanagment ---
hl.bind(Mod .. " + H", hl.dsp.focus({ direction = "left" }))
hl.bind(Mod .. " + J", hl.dsp.focus({ direction = "down" }))
hl.bind(Mod .. " + K", hl.dsp.focus({ direction = "up" }))
hl.bind(Mod .. " + L", hl.dsp.focus({ direction = "right" }))

hl.bind(Mod .. " + Z", hl.dsp.submap("move"))
hl.define_submap("move", function()
  hl.bind(Mod .. " + H", hl.dsp.window.move({ direction = "left" }))
  hl.bind(Mod .. " + J", hl.dsp.window.move({ direction = "down" }))
  hl.bind(Mod .. " + K", hl.dsp.window.move({ direction = "up" }))
  hl.bind(Mod .. " + L", hl.dsp.window.move({ direction = "right" }))

  -- layout.scrolling specific
  hl.bind(Mod .. " + SHIFT + H", hl.dsp.layout("swapcol l"))
  hl.bind(Mod .. " + SHIFT + L", hl.dsp.layout("swapcol r"))

  hl.bind("escape", hl.dsp.submap("reset"))
end)

hl.bind(Mod .. " + X", hl.dsp.submap("resize"))
hl.define_submap("resize", function()
  hl.bind(Mod .. " + H", hl.dsp.window.resize({ x = -20, y = 0, relative = true }), { repeating = true })
  hl.bind(Mod .. " + J", hl.dsp.window.resize({ x = 0, y = -20, relative = true }), { repeating = true })
  hl.bind(Mod .. " + K", hl.dsp.window.resize({ x = 0, y = 20, relative = true }), { repeating = true })
  hl.bind(Mod .. " + L", hl.dsp.window.resize({ x = 20, y = 0, relative = true }), { repeating = true })

  -- layout.scrolling specific
  hl.bind(Mod .. " + SHIFT + H", hl.dsp.layout("colresize -0.02"),  { repeating = true })
  hl.bind(Mod .. " + SHIFT + L", hl.dsp.layout("colresize +0.02"),  { repeating = true })
  hl.bind(Mod .. " + Q", hl.dsp.layout("colresize +conf"),          { repeating = true })
  hl.bind(Mod .. " + SHIFT + Q", hl.dsp.layout("colresize -conf"),  { repeating = true })
  hl.bind(Mod .. " + 0", hl.dsp.layout("fit all"))
  hl.bind(Mod .. " + 2", hl.dsp.layout("colresize all 0.5"))
  hl.bind(Mod .. " + 3", hl.dsp.layout("colresize all 0.333"))

  hl.bind("escape", hl.dsp.submap("reset"))
end)

--- General binds ---
hl.bind(Mod .. " + T", hl.dsp.exec_cmd("alacritty"))
hl.bind(Mod .. " + W", hl.dsp.window.close())
hl.bind(Mod .. " + R", hl.dsp.exec_cmd("rofi -show combi"))
hl.bind(Mod .. " + E", hl.dsp.exec_cmd("dolphin"))
hl.bind(Mod .. " + F", hl.dsp.window.float())
hl.bind("CONTROL + SHIFT + escape", hl.dsp.exec_cmd("alacritty -e btop -p 0"))
hl.bind("CONTROL + ALT + L", hl.dsp.exec_cmd("hyprlock -c $XDG_CONFIG_HOME/hypr/lock/normal.conf"))
hl.bind("ALT + TAB", hl.dsp.focus({ monitor = "+1" }))

hl.bind(Mod .. " + C", hl.dsp.exec_cmd("cliphist list | rofi -dmenu | cliphist decode | wl-copy"))
hl.bind(Mod .. " + B", hl.dsp.exec_cmd("firefox"))

--- Workspace Managment ---
for i = 1, 10 do
  local key = i % 10
  hl.bind(Mod .. " + " .. key, hl.dsp.focus({ workspace = i , on_current_monitor = true}))
  hl.bind(Mod .. " + SHIFT + " .. key, hl.dsp.window.move({ workspace = i }))
end

hl.bind(Mod .. " + S", hl.dsp.workspace.toggle_special("magick"))
hl.bind(Mod .. " + SHIFT + S ", hl.dsp.window.move({ workspace = "special:magick" }))

--- mouse ---
hl.bind(Mod .. " + mouse:272", hl.dsp.window.drag(), { mouse = true })
hl.bind(Mod .. " + mouse:273", hl.dsp.window.resize(), { mouse = true })

-- Laptop multimedia keys for volume and LCD brightness
hl.bind("XF86AudioRaiseVolume", hl.dsp.exec_cmd("wpctl set-volume -l 1 @DEFAULT_AUDIO_SINK@ 5%+"), { locked = true, repeating = true })
hl.bind("XF86AudioLowerVolume", hl.dsp.exec_cmd("wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%-"),      { locked = true, repeating = true })
hl.bind("XF86AudioMute",        hl.dsp.exec_cmd("wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle"),     { locked = true, repeating = true })
hl.bind("XF86AudioMicMute",     hl.dsp.exec_cmd("wpctl set-mute @DEFAULT_AUDIO_SOURCE@ toggle"),   { locked = true, repeating = true })
hl.bind("XF86MonBrightnessUp",  hl.dsp.exec_cmd("brightnessctl -e4 -n2 set 5%+"),                  { locked = true, repeating = true })
hl.bind("XF86MonBrightnessDown",hl.dsp.exec_cmd("brightnessctl -e4 -n2 set 5%-"),                  { locked = true, repeating = true })
hl.bind("XF86PowerOff"         ,hl.dsp.exec_cmd("~/.config/qtile/scripts/shutdown.sh"))

-- Requires playerctl
hl.bind("XF86AudioNext",  hl.dsp.exec_cmd("playerctl next"),       { locked = true })
hl.bind("XF86AudioPause", hl.dsp.exec_cmd("playerctl play-pause"), { locked = true })
hl.bind("XF86AudioPlay",  hl.dsp.exec_cmd("playerctl play-pause"), { locked = true })
hl.bind("XF86AudioPrev",  hl.dsp.exec_cmd("playerctl previous"),   { locked = true })

hl.bind("switch:Lid Switch", hl.dsp.exec_cmd("hyprlock"),       { locked = true })
