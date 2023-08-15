from libqtile import bar, layout
from libqtile.config import Click, Drag, Group, Key, Match, Screen, hook
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.dgroups import simple_key_binder

# qtile_extras widget needed for styling
from qtile_extras.widget.decorations import PowerLineDecoration
from qtile_extras import widget

# import gruvbox dark theme
from gruvbox.gruvbox import *
from gruvbox.dark import *

import os, subprocess

# vars
mod = "mod4"
alt = "mod1"
terminal = guess_terminal()

# vars for mode switching
mode = {"current": 0, "modes": ["nav", "size", "move"]}

# decorations
deco_powerline = {
    "decorations": [
        PowerLineDecoration(path="back_slash"),
        ]
    }

# hooks
@hook.subscribe.startup_once
def autostart(): # run my startup programs
    home = os.path.expanduser("~/.config/qtile/scripts/autostart.sh")
    subprocess.call([home])

#

keys = [
    # manager binds
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod, "shift"], "h", lazy.layout.swap_left()),
    Key([mod, "shift"], "l", lazy.layout.swap_right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, alt], "h", lazy.layout.grow()),
    Key([mod, alt], "l", lazy.layout.shrink()),
    Key([mod, alt], "j", lazy.layout.reset()),
    Key([mod, alt], "k", lazy.layout.maximize()),
    Key([mod, "shift"], "space", lazy.layout.flip()),
    Key([mod], "m", lazy.window.toggle_minimize(), desc="Toggle maximize"),

    # control qtile/apps
    Key(["control", alt], "t", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "e", lazy.spawn("nemo")),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawn("rofi -show combi"), desc="Spawn a command using a prompt widget"),
    Key([alt, "control"], "l", lazy.spawn("betterlockscreen -l"), desc="Lock the computer"),

    # mode switches

    #media keys
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl -- set-sink-volume 0 -5%"), desc="Lower Volume by 5%"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl -- set-sink-volume 0 +5%"), desc="Raise Volume by 5%"),
    Key([], "XF86AudioMute", lazy.spawn("pactl -- set-sink-mute 0 toggle")),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc="Play/Pause player"),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc="Skip to next"),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc="Skip to previous"),

    # util
    Key([], "Print", lazy.spawn("/home/berend/.config/qtile/scripts/screenshot.py")), # take screenshot off currenty active screen
    Key([alt], "Print", lazy.spawn("/home/berend/.config/qtile/scripts/screenshot.py -1")), # take screenshot off all screens
    #Key([mod], "c", lazy.spawn("rofi -show calc"), desc="Spawn rofi in calculator mode"),
    Key(["control", "shift"], "Escape", lazy.spawn("gnome-system-monitor"), desc="open the system monitor"),
    Key([alt], "Tab", lazy.next_screen(), desc="Swicht to next screen"),
]

# create all groups
groups = [
    Group("1", position=1),
    Group("2", position=2),
    Group("3", position=3),
    Group("4", position=4),
    
    #Group("5", position=5),
    #Group("6", position=6),
    #Group("7", position=7),
    #Group("8", position=8),

    Group("tray", layout="monadtall", position=9, matches=[Match(wm_class=["discord"]), Match(title=["Steam Games List"])]),
    Group("audio/video", position=10, matches=[Match(wm_class=["napster bigscreen electron"]), Match(wm_class=["easyeffects"]), Match(wm_class=["obs"])]),
]

# easy snippet to use mod key + <number> to switch groups
# also does mod + shift + <umber> to move window to group and focus that group
dgroups_key_binder = simple_key_binder(mod)

layouts = [
    layout.MonadTall(
        inactive_bg=focus_f,
        margin=6,
        border_width=2,
        border_focus=focus_t,
        border_normal=normal_t,
    ),
    layout.TreeTab(
        active_bg=focus_t,
        active_fg=foreground,
        inactive_bg=normal_t,
        inactive_fg=foreground,
        bg_color=background,
        section_fg=foreground,
        border_focus=focus_t,
        border_normal=normal_t,
        previous_on_rm=True,
    ),
    layout.Max(
        margin=0,
        border_width=0,
        border_focus=focus_t,
        border_normal=normal_t,
    ),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
    foreground=foreground,
    background=background,
)
extension_defaults = widget_defaults.copy()

screens = [
    # main monitor
    Screen(
        wallpaper="~/Pictures/background/spaceman.jpg",
        wallpaper_mode="fill",
        top=bar.Bar(
            [
                # bar contents
                widget.CurrentLayout(
                    background=blue,
                    foreground=foreground,
                    **deco_powerline,
                ),
                
                #widget.TextBox(
                #    text=mode.current(),
                #    background=purple,
                #    foreground=foreground,
                #    update_interval=0.04,
                #    **deco_powerline,
                #),

                widget.GroupBox(
                    disable_drag=True,
                    active=active,
                    inactive=background,
                    urgent_border=warning,
                    highlight_method="block",
                    **deco_powerline,
                ),
                widget.WindowName(),
                widget.Systray(
                    background=background,
                    foreground=foreground,
                    **deco_powerline,
                ),
                widget.CheckUpdates(
                    distro="Ubuntu",
                    background=yellow,
                    foreground=foreground,
                    **deco_powerline,
                ),
                widget.PulseVolume(
                    background=purple,
                    foreground=foreground,
                    fmt=" {}",
                    update_interval=0.04,
                    **deco_powerline,
                ),
                widget.Clock(
                    format="%Y-%m-%d %a %H:%M",
                    background=blue,
                    foreground=foreground,
                ),
            ],
            24,
        ),
        x=0,
        y=0,
        width=1920,
        height=1080,
    ),

    # secondary monitor
    Screen (
        wallpaper="~/Pictures/background/spaceman.jpg",
        wallpaper_mode="fill",
        top=bar.Bar(
            [
                # bar contents
                widget.CurrentLayout(
                    background=blue,
                    foreground=foreground,
                    **deco_powerline,
                ),
                widget.GroupBox(
                    disable_drag=True,
                    active=active,
                    inactive=background,
                    urgent_border=warning,
                    highlight_method="block",
                    **deco_powerline,
                ),
                widget.WindowName(
                    **deco_powerline,
                ),
                widget.CPU(
                    format="󰻠 {load_percent}%",
                    background=yellow,
                    foreground=foreground,
                    **deco_powerline,
                ),
                widget.Memory(
                    format="󰍛 {MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}",
                    measure_mem="G",
                    background=purple,
                    foreground=foreground,
                    **deco_powerline,
                ),
                widget.NvidiaSensors(
                    format="GPU: {temp}󰔄",
                    background=aqua,
                    foreground=foreground,
                    foreground_alert=warning,
                    **deco_powerline,
                ),
                widget.Clock(
                    format="%H:%M",
                    background=blue,
                    foreground=foreground,
                ),
            ],
            24,
        ),
        x=1920,
        y=0,
        width=1920,
        height=1080,
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

floating_types = ["notification", "toolbar", "splash", "dialog"]


follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[ # Match chases to make window
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class="confirmreset"),  # gitk
    Match(wm_class="makebranch"),  # gitk
    Match(wm_class="maketag"),  # gitk
    Match(wm_class="ssh-askpass"),  # ssh-askpass
    Match(title="branchdialog"),  # gitk
    Match(title="pinentry"),  # GPG key password entry
    Match(wm_class="keepassxc"), # password manager
    Match(wm_class="file-roller"), # archive extractor
    Match(wm_class="gnome-calculator"),
    # Match(wm_class="helvum"),
    Match(wm_class="gnome-screenshot"),
    Match(wm_class="edmarketconnector"),
],  
fullscreen_border_width = 0,
border_width = 2,
border_focus=focus_t,
border_normal=normal_t,)

auto_fullscreen = True

focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = False

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

wmname = "LG3D"
