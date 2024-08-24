from libqtile import bar, layout, qtile, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
#terminal = guess_terminal()
terminal="kitty"

keys = [

    #---------------------------------------------------
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod, "control"],"f", lazy.spawn("firefox"), desc="Launch Firefox"),
    Key([mod, "control"],"t", lazy.spawn("thunderbird"), desc="Launch thunderbird"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]

# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )


#groups = [Group(i) for i in "123456789"]
groups = []
group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
group_labels = ["", "", "", "", "", "", "", "", "", ""]
group_layouts = ["monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall"]

for i in range(len(group_names)):
    groups.append(
            Group(
                name=group_names[i],
                layout=group_layouts[i].lower(),
                label=group_labels[i],
            ))

colors = [
    ["#2e3440", "#2e3440"],  # 0 background
    ["#d8dee9", "#d8dee9"],  # 1 foreground
    ["#3b4252", "#3b4252"],  # 2 background lighter
    ["#bf616a", "#bf616a"],  # 3 red
    ["#a3be8c", "#a3be8c"],  # 4 green
    ["#ebcb8b", "#ebcb8b"],  # 5 yellow
    ["#81a1c1", "#81a1c1"],  # 6 blue
    ["#b48ead", "#b48ead"],  # 7 magenta
    ["#88c0d0", "#88c0d0"],  # 8 cyan
    ["#e5e9f0", "#e5e9f0"],  # 9 white
    ["#4c566a", "#4c566a"],  # 10 grey
    ["#d08770", "#d08770"],  # 11 orange
    ["#8fbcbb", "#8fbcbb"],  # 12 super cyan
    ["#5e81ac", "#5e81ac"],  # 13 super blue
    ["#242831", "#242831"] # 14 super dark background
]

for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name), lazy.group[i.name].toscreen()),
    ])

def init_layout_theme():
    return{"margin": 3,
           "border_width": 1,
           "border_focus": "#7dcfff",
           "border_normal":"#bb9af7"
           }

layout_theme=init_layout_theme()

layouts = [
    layout.MonadTall(margin=6, border_width=2, border_focus=colors[10], border_normal=colors[14]),
    layout.MonadWide(margin=6, border_width=2, border_focus=colors[10], border_normal=colors[14]),
    #layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

def dunst():
    return subprocess.check_output(["./.config/qtile/dunst.sh"]).decode("utf-8").strip()

def toggle_dunst():
    qtile.cmd_spawn("./.config/qtile/dunst.sh --toggle")

def toggle_notif_center():
    qtile.cmd_spawn("./.config/qtile/dunst.sh --notif-center")

# Mouse_callback functions
def open_launcher():
    qtile.cmd_spawn("rofi -show drun")

#def kill_window():
#    qtile.cmd_spawn("xdotool getwindowfocus windowkill")

def open_calendar():
    qtile.cmd_spawn("gnome-calendar")

def open_pavu():
    qtile.cmd_spawn("pavucontrol")

def open_powermenu():
    qtile.cmd_spawn("power")


widget_defaults = dict(
    font="sans",
    fontsize=12,
    background=colors[0],
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        wallpaper="/home/agaho/Pictures/minimalist-space-z8.jpg",
        wallpaper_mode="fill",
        top=bar.Bar(
            [
                widget.TextBox(
                    text="  ",
                    foreground=colors[13],
                    background=colors[0],
                    font="Font Awesome 6 Free Solid",
                    fontsize=28,
                    padding=20,
                    mouse_callbacks={"Button1": open_launcher},
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=20,
                    padding=0,
                ),
                widget.GroupBox(
                    highlight_method='text',
                    background=colors[14],
                    padding=4,
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=20,
                    padding=0,
                ),
                widget.Sep(
                    linewidth=0,
                    foreground=colors[2],
                    background=colors[0],
                    padding=10,
                    size_percent=40,
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=20,
                    padding=0,
                ),
                widget.WindowCount(
                    background=colors[14],
                ),
                widget.CurrentLayoutIcon(
                    background=colors[14],
                    foreground=colors[2],
                    custom_icon_paths=["~/.config/qtile/icons"],
                    scale=0.75,
                    padding=0,
                    margin=0,
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=20,
                    padding=0,
                ),
                widget.Sep(
                    linewidth=0,
                    foreground=colors[2],
                    padding=10,
                    size_percent=50,
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=20,
                    padding=0,
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[6],
                    background=colors[14],
                    fontsize=18,
                    padding=0,
                ),
               widget.Prompt(
                    background=colors[14],
                    foreground=colors[6],
                    fontsize=10,
                    prompt=' :'
                        ),
                widget.TextBox(
                    text="",
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=20,
                    padding=0,
                ),
                widget.Spacer(),
                widget.TextBox(
                    text=" ",
                    foreground=colors[12],
                    background=colors[0],
                    fontsize=20,
                    font="Font Awesome 6 Free Solid",
                ),
                widget.WindowName(
                    background=colors[0],
                    foreground=colors[12],
                    width=bar.CALCULATED,
                    empty_group_string="Desktop",
                    max_chars=130,
                    #                    mouse_callbacks={"Button2": kill_window},
                ),
                widget.Spacer(),
                widget.Systray(
                    icon_size=26,
                    background=colors[0],
                    padding=7,
                ),
                widget.Sep(
                    linewidth=0,
                    foreground=colors[2],
                    padding=10,
                    size_percent=50,
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=20,
                    padding=0,
                ),
                widget.TextBox(
                    text="󰖩 ",
                    fontsize=18,
                    foreground=colors[7],
                    background=colors[14],
                ),
                widget.Net(
                    interface="eno1",
                    format="{down} ↓↑ {up}",
                    foreground=colors[7],
                    background=colors[14],
                    prefix="k",
                    padding=5,
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=20,
                    padding=0,
                ),
                widget.Sep(
                    linewidth=0,
                    foreground=colors[2],
                    padding=10,
                    size_percent=50,
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=20,
                    padding=0,
                ),
                widget.TextBox(
                    text=" ",
                    fontsize=18,
                    foreground=colors[5],
                    background=colors[14],
                    mouse_callbacks={"Button1":open_calendar},
                ),
                widget.Clock(
                    format="%a, %b %d",
                    background=colors[14],
                    foreground=colors[5],
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=20,
                    padding=0,
                ),
                widget.Sep(
                    linewidth=0,
                    foreground=colors[2],
                    padding=10,
                    size_percent=50,
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=20,
                    padding=0,
                ),
                widget.TextBox(
                    text=" ",
                    fontsize=18,
                    foreground=colors[4],
                    background=colors[14],
                ),
                widget.Clock(
                    format="%I:%M %p",
                    foreground=colors[4],
                    background=colors[14],
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=20,
                    padding=0,
                ),
                widget.Systray(
                    background=colors[0],
                    icon_size=10,
                ),
                widget.TextBox(
                    text="⏻",
                    foreground=colors[13],
                    font="Font Awesome 6 Free Solid",
                    fontsize=20,
                    padding=20,
                    mouse_callbacks={"Button1":open_control},
                ),
            ],
            24,
            margin=[2, 12, 2, 12],
            border_color=colors[0],
            border_width=[4, 4, 4, 4],
        ),
        bottom=bar.Gap(0),
        left=bar.Gap(6),
        right=bar.Gap(6),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser("~")
    subprocess.call([home + "/.config/qtile/autostart.sh"])

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
