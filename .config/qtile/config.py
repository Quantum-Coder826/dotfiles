from libqtile import bar, layout
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen, hook
from libqtile.lazy import lazy
from libqtile.dgroups import simple_key_binder

# qtile_extras needed for powerline styling
from qtile_extras.widget.decorations import PowerLineDecoration
from qtile_extras import widget

# import gruvbox dark theme
from gruvbox.gruvbox import *
from gruvbox.dark import *

# import os to send commands to the system
import os, subprocess

# utils
from scripts.utils import *

#* vars
mod = "mod4"
alt = "mod1"
terminal = "konsole"

# decorations
deco_powerline = {
    "decorations": [
        PowerLineDecoration(path="back_slash"),
        ]
    }

#* hooks & related functions
@hook.subscribe.startup_once
def autostart(): # run my startup programs
    home = os.path.expanduser("~/.config/qtile/scripts/startup.sh")
    subprocess.call([home])

@hook.subscribe.startup
def run_every_startup():
    utils.setTrayLayout()

keys = [
    # manager binds
    KeyChord([mod], "z", [ # binds for moving windows around
        Key([mod], "h",
                lazy.layout.swap_left().when(layout="monadtall"),
                lazy.layout.move_left().when(layout="plasma"),
                lazy.layout.integrate_left().when(layout="plasma")),
        Key([mod], "l",
                lazy.layout.swap_right().when(layout="monadtall"),
                lazy.layout.move_right().when(layout="plasma"),
                lazy.layout.integrate_right().when(layout="plasma")),
        Key([mod], "j",
                lazy.layout.shuffle_down().when(layout="monadtall"),
                lazy.layout.move_down().when(layout="plasma"),
                lazy.layout.integrate_down().when(layout="plasma")),
        Key([mod], "k",
                lazy.layout.shuffle_up().when(layout="monadtall"),
                lazy.layout.move_up().when(layout="plasma"),
                lazy.layout.integrate_up().when(layout="plasma")),
    ], mode=True, name="󰆾 "),

    KeyChord([mod], "x", [# binds for resizing windows
        Key([mod], "h",
                lazy.layout.grow().when(layout="monadtall"),
                lazy.layout.grow_width(30).when(layout="plasma")),
        Key([mod], "l",
                lazy.layout.shrink().when(layout="monadtall"),
                lazy.layout.grow_width(-30).when(layout="plasma")),
        Key([mod], "j",
                lazy.layout.reset().when(layout="monadtall"),
                lazy.layout.grow_height(30).when(layout="plasma")),
        Key([mod], "k",
                lazy.layout.maximize().when(layout="monadtall"),
                lazy.layout.grow_height(-30).when(layout="plasma")),
    ], mode=True, name="󰩨 "),
    
    # binds for navigating between windows
    # nav mode is enabled default
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),

    # binds spesific to layout.plasma
    Key([mod], "d", lazy.layout.mode_horizontal().when(layout="plasma")),
    Key([mod], "v", lazy.layout.mode_vertical().when(layout="plasma")),
    Key([mod, "shift"], "d", lazy.layout.mode_horizontal_split().when(layout="plasma")),
    Key([mod, "shift"], "v", lazy.layout.mode_vertical_split().when(layout="plasma")),

    # bind to reset windows size needs to be active at all times
    Key([mod, "shift"], "j", 
            lazy.layout.reset().when(layout="monadtall"),
            lazy.layout.reset_size().when(layout="plasma")),
    
    # control qtile/apps
    Key(["control", alt], "t", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "e", lazy.spawn("dolphin"), desc="Open file explorer"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawn("rofi -show combi"), desc="Spawn a command using a prompt widget"),
    Key([alt, "control"], "l", lazy.spawn("betterlockscreen -l"), desc="Lock the computer"),
    Key([mod], "c", lazy.spawn("rofi -modi 'clipboard:greenclip print' -show clipboard -run-command '{cmd}'")),
    # media keys
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q -D pulse sset Master 5%-"), desc="Lower Volume by 5%"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q -D pulse sset Master 5%+"), desc="Raise Volume by 5%"),
    Key([], "XF86AudioMute", lazy.spawn("pactl -- set-sink-mute 0 toggle"), desc="Toggle mute"),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc="Play/Pause player"),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc="Skip to next"),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc="Skip to previous"),

    # util
    Key(["control", "shift"], "Escape", lazy.spawn(terminal + " -e 'btop -p 0'"), desc="open xfce terminal running btop as a task manager"),
    Key([alt], "Tab", lazy.next_screen(), desc="Switch focus between screens"),
    Key([mod], "b", lazy.spawn("firefox"), desc="Open firefox"),
    Key([], "Print", lazy.spawn("xfce4-screenshooter"), desc="Open screenshotter"),
]

# create all groups
groups = [
    Group("1", position=1),
    Group("2", position=2),
    Group("3", position=3),
    Group("4", position=4),
    Group("5", position=5),
    Group("6", position=6),

    #Group("7", position=7),
    #Group("8", position=8),

    Group(
            name="tray",
            label="󱊖", #nf-md-tray_full
            #layout="ScreenSplit",
            #layouts=[layout.ScreenSplit],
            position=9,
            matches=[
                Match(wm_class=["discord"]),
                Match(wm_class=["steamwebhelper", "steam"]),
                Match(wm_class=["helvum", "helvum"]),
            ]),
    Group(
            name="a/v",
            label="󰤽", #nf-md-audio_video
            position=10, 
            matches=[
                    Match(wm_class=["napster bigscreen electron"]),
                    Match(wm_class=["easyeffects"]),
                    Match(wm_class=["obs"]),
                    Match(wm_class=["qpwgraph", "qpwgraph"])
            ]),
]

# easy snippet to use mod key + <number> to switch groups
# also does mod + shift + <number> to move window to group and focus that group
dgroups_key_binder = simple_key_binder(mod)

layouts = [
    layout.MonadTall(
        inactive_bg=focus_f,
        margin=6,
        border_width=2,
        border_focus=focus_t,
        border_normal=normal_t,
    ),
    layout.Plasma(
        border_focus=focus_t,
        border_focus_fixed=focus_t,
        border_normal=normal_t,
        border_normal_fixed=normal_t,
        border_width=2,
        border_width_single=0,
        margin=6,
    ),
    layout.TreeTab(
        sections=[""],
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
    font="DroidSansM Nerd Font",
    fontsize=14,
    padding=4,
    foreground=foreground,
    background=background,
)
extension_defaults = widget_defaults.copy()

wallpaper = "~/Pictures/background/pacman-ghosts.jpg"

screens = [
    #main monitor
    Screen(
        wallpaper=wallpaper,
        wallpaper_mode="fill",
        top=bar.Bar(
            [
                #*bar contents
                widget.CurrentLayoutIcon(
                    custom_icon_paths = ["~/.config/qtile/gruvbox/gruvbox-dark0-icons"],
                    background=blue,
                    foreground=foreground,
                    **deco_powerline,
                ),
                widget.Sep(
                    linewidth=0,
                    padding=1,
                    size_percent=0,
                    background=blue,
                    foreground=foreground,
                    **deco_powerline,
                ),
                #widget.CapsNumLockIndicator(
                #    background=green,
                #    foreground=foreground,
                #    **deco_powerline,
                #),
                widget.Chord(
                    background=green,
                    foreground=foreground,
                    **deco_powerline,
                ),
                widget.Plasma(
                    horizontal=" ",
                    vertical=" ",
                    split="󰃻",
                    format="{mode}",
                    background=purple,
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
                widget.Sep(
                    linewidth=0,
                    padding=1,
                    size_percent=0,
                    background=blue,
                    foreground=foreground,
                    **deco_powerline,
                ),
                widget.WindowName(
                    max_chars=160,
                    **deco_powerline,
                ),
                widget.Systray(
                    background=black0,
                    foreground=foreground,
                    **deco_powerline,
                ),
                widget.CheckUpdates(
                    distro="Debian",
                    display_format="󰚰 {updates}", #nf-md-update
                    restart_indicator="󱄌", #nf-md-restart_alert
                    background=red,
                    foreground=foreground,
                    **deco_powerline,
                ),
                widget.Volume(
                    device = "pulse",
                    check_mute_string = "[off]",
                    fmt=" {}",
                    background=purple,
                    foreground=foreground,
                    **deco_powerline,
                ),
                widget.Clock(
                    format="%d-%m-%y %a %H:%M:%S",
                    background=blue,
                    foreground=foreground,
                ),
            ],
            24,
        ),
    ),

    #*secondary monitor
    Screen (
        wallpaper=wallpaper,
        wallpaper_mode="fill",
        top=bar.Bar(
            [
                #*bar contents
                widget.TextBox(
                    text="",
                    background=background,
                    foreground=foreground,
                    **deco_powerline,
                ),
                widget.Clock(
                    format="%H:%M",
                    background=blue,
                    foreground=foreground,
                    **deco_powerline,
                ),
                widget.NvidiaSensors(
                    format="󰾲  {temp}󰔄",
                    mouse_callbacks={"Button1": lazy.spawn(terminal + " -e 'nvtop'")},
                    update_interval=1.0,
                    background=aqua,
                    foreground=foreground,
                    foreground_alert=warning,
                    **deco_powerline,
                ),
                widget.Memory(
                    format="󰍛 {MemUsed:.0f}{mm}󰿟{MemTotal:.0f}{mm}",
                    measure_mem="G",
                    mouse_callbacks={"Button1": lazy.spawn("plasma-systemmonitor")},
                    update_interval=1.0,
                    background=purple,
                    foreground=foreground,
                    **deco_powerline,
                ),
                widget.CPU(
                    format="󰻠 {load_percent}󰏰",
                    mouse_callbacks={"Button1": lazy.spawn("plasma-systemmonitor")},
                    update_interval=1.0,
                    background=yellow,
                    foreground=foreground,
                    **deco_powerline,
                ),
                widget.WindowName(
                    max_chars=160,
                    **deco_powerline,
                ),
                widget.Sep(
                    linewidth = 0,
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
                widget.Plasma(
                    horizontal=" ",
                    vertical=" ",
                    split="󰃻",
                    format="{mode}",
                    background=purple,
                    foreground=foreground,
                    **deco_powerline,
                ),
                widget.Chord(
                    background=green,
                    foreground=foreground,
                    **deco_powerline,
                ),
                widget.CurrentLayoutIcon(
                    custom_icon_paths = ["~/.config/qtile/gruvbox/gruvbox-dark0-icons"],
                    background=blue,
                    foreground=foreground,
                ),
            ],
            24,
        ),
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
    Match(title="branchdialog"),  # gitk
    Match(wm_class="ssh-askpass"),  # ssh-askpass
    Match(title="pinentry"),  # GPG key password entry
    Match(wm_class="keepassxc"), # password manager
    Match(wm_class="file-roller"), # archive extractor
    Match(wm_class="xfce4-screenshooter"),
    Match(wm_class="edmarketconnector"),
    Match(wm_class="megasync"),
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

floats_kept_above=True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

wmname = "LG3D"
