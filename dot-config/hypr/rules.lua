--------------
--- WINDOW ---
--------------
--- See https://wiki.hypr.land/Configuring/Basics/Window-Rules/

local suppressMaximizeRule = hl.window_rule({
  -- Ignore maximize requests from all apps. You'll probably like this.
  name  = "suppress-maximize-events",
  match = { class = ".*" },

  suppress_event = "maximize",
})
suppressMaximizeRule:set_enabled(true)

hl.window_rule({
  -- Fix some dragging issues with XWayland
  name  = "fix-xwayland-drags",
  match = {
    class      = "^$",
    title      = "^$",
    xwayland   = true,
    float      = true,
    fullscreen = false,
    pin        = false,
  },

  no_focus = true,
})

hl.window_rule({
  name = "polkits",
  match = {
    class = "qt-sudo",
  },
  float = true,
  center = true,
})

hl.window_rule({
  name = "keepass",
  match = {class = "org.keepassxc.KeePassXC"},
  float = true,
  size = {600, 600},
})

--- System tray ---
hl.workspace_rule({
  workspace = "7",
  layout = "dwindle",
})
hl.window_rule({
  name = "steam",
  match = {
    initial_title = "Steam Games List"
  },
  workspace = "7 silent",
})
hl.window_rule({
  name = "Distord",
  match = {
    class = "discord"
  },
  workspace = "7 silent",
})
hl.window_rule({
  name = "sound",
  match = {
    class = "com.github.wwmm.easyeffects",
  },
  workspace = "8 silent",
})

--- Steam games ---
hl.window_rule({
  name = "Fullscreen games",
  match = {
    initial_class = "steam_app_\\d+",
    },
  fullscreen = true,
  fullscreen_state = "3",
  monitor = "DP-2",
  workspace = "1",
})

-----------------
--- WORKSPACE ---
-----------------
--- and https://wiki.hypr.land/Configuring/Basics/Workspace-Rules/

--- Special workspace ---
hl.workspace_rule({
  workspace = "s[true]",
  gaps_out = 25,
})

hl.window_rule({
  name = "Styling for special",
  match = {
    workspace = "s[true]",
  },
  border_size = 5,
})

------------------
--- Layer Rule ---
------------------
--- See https://wiki.hypr.land/Configuring/Basics/Window-Rules/#layer-rules
hl.layer_rule({
  name = "waybar",
  match = { namespace = "waybar" },
  blur = false,
})
hl.layer_rule({
  name = "vicinae",
  match = {namespace = "vicinae"},
  blur = true,
  ignore_alpha = 0,
  no_anim = true,
})
