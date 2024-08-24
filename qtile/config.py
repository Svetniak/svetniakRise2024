import os
from libqtile import bar, layout, qtile, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

mod = "mod4"
myterm = "wezterm"

keys = [
#-------SPAWN APPS----------------------------------------------------------------------
    Key([mod, "control"], "f", lazy.spawn("brave"), desc="Launch Firefox Web browser"),
    Key([mod, "control"], "e", lazy.spawn("chromium"), desc="Launch Chromium Web browser"),
    Key([mod], "e", lazy.spawn("thunar"), desc="Launch Thunar File browser"),
    Key([mod, "control"], "t", lazy.spawn("thunderbird"), desc="Launch Thunderbird email app"),
    Key([mod, "control"], "b", lazy.spawn("blender"), desc="Launch Thunar 3D modeling"),
    Key([mod, "control"], "i", lazy.spawn("inkscape"), desc="Launch Inkscape Graphics editor"),
    Key([mod, "control"], "g", lazy.spawn("gimp"), desc="Launch GIMP Image Editor"),
    Key([mod, "control"], "v", lazy.spawn("virtualbox"), desc="Launch Virtua Box Image Editor"),
    Key([mod, "control"], "z", lazy.spawn("filezilla"), desc="Launch Filezilla file manager"),

    Key([mod, "control"], "w", lazy.spawn("libreoffice --writer"), desc="Launch Writer word processing"),
    Key([mod, "control"], "c", lazy.spawn("libreoffice --calc"), desc="Launch Calc Spread Sheets"),
    Key([mod, "control"], "i", lazy.spawn("libreoffice --impress"), desc="Launch Impress presentation"),

    Key([mod], "Escape", lazy.spawn('xkill')),
    Key([mod], "Return", lazy.spawn(myterm), desc="Launch myterm"),
    Key([mod, "control"], "Return", lazy.spawn("wezterm"), desc="Launch myterm"),

    Key([mod], "space", lazy.spawn("rofi -show drun"), desc="App Launcher"),
    Key([mod, "control"], "p", lazy.spawn("/home/ikki/.config/rofi/powermenu.sh"), desc="Log out"),
#-------ACTIONS-------------------------------------------------------------------------
     Key([mod, "shift"], "p", lazy.spawn("pactl set-sink-volume bluez_output.74_2A_8A_10_6D_FC.1 +5%"), desc="Volume Up"),
     Key([mod, "shift"], "o", lazy.spawn("pactl set-sink-volume bluez_output.74_2A_8A_10_6D_FC.1 -5%"), desc="Volume Down"),
     Key([mod, "shift"], "s", lazy.spawn("flameshot gui"), desc="Volume Down"),

#-------SCREEN--------------------------------------------------------------------------------
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
#    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    Key([mod, "control"], "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),
    Key([mod, "control"], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),


    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack",),
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

for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )

groups = []
group_names = ["1", "2", "3", "4", "5", "6",]
group_labels = ["", "", "", "", "", "",]
group_layouts = ["monadtall", "Columns", "Columns", "monadtall", "monadtall", "monadtall",]

for i in groups:
    keys.extend(
        [
            # mod1 + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + group number = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + group number = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))

for i in groups:
    keys.extend([

#CHANGE WORKSPACES
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key([mod], "Tab", lazy.screen.next_group()),
        Key([mod, "shift" ], "Tab", lazy.screen.prev_group()),
        Key(["mod1"], "Tab", lazy.screen.next_group()),
        Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),

# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
        #Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND FOLLOW MOVED WINDOW TO WORKSPACE
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name) , lazy.group[i.name].toscreen()),
    ])


def init_colors():
    return [["#414868", "#414868"], # color 0
            ["#f7768e", "#f7768e"], # color 1
            ["#9ece6a", "#9ece6a"], # color 2
            ["#e0af68", "#e0af68"], # color 3
            ["#7aa2f7", "#7aa2f7"], # color 4
            ["#bb9af7", "#bb9af7"], # color 5
            ["#7dcfff", "#7dcfff"], # color 6
            ["#a9b1d6", "#a9b1d6"], # color 7
            ["#c0caf5", "#c0caf5"], # color 8
            ["#1a1b26", "#1a1b26"], # color 9
            ["#0a0d12", "#0a0d12"]] # color 10

colors = init_colors()

layouts = [
    layout.Columns(margin=4, border_focus=colors[7],border_normal=colors[0]),
    # layout.Max(),
    # layout.Stack(num_stacks=1),
    layout.Bsp(margin=6, border_focus=colors[7],border_normal=colors[0]),
    # layout.Matrix(),
    layout.MonadTall(margin=6, border_focus=colors[7],border_normal=colors[0]),
    # lzyout.MonadWide(margin=6, border_focus=colors[7],border_normal=colors[0]),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(margin=6, border_focus=colors[7],border_normal=colors[0]),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="SauceCodePro",
    fontsize=14,
    foreground=colors[8],
    background=colors[9],
    padding=3,
)
extension_defaults = widget_defaults.copy()


#screen1 ----------------------------------------------------------------
screens = [
    Screen(
        wallpaper='~/Pictures/skullWall.jpg',
        wallpaper_mode='fill',

        top=bar.Bar(
            [
            widget.Sep(
                linewidth = 0,
                padding = 8,
                ),
            widget.CurrentLayoutIcon(
                    custom_icon_paths=['~/.config/qtile/icons'],
                    scale=0.7,
                    background = colors[10],
                ),
            widget.WindowName(),
            widget.TextBox(
                    text="",
                    foreground=colors[10],
                    background=colors[9],
                    fontsize=24,
                    padding=0,
                ),
            widget.TextBox(
                    text = '  ',
                    fontsize = 16,
                    background = colors [10],
                    foreground = colors [4],
                    padding_y = -2,
                    mouse_callbacks =
                        {'Button1': lambda : qtile.cmd_spawn('rofi -show drun')},
                ),
            widget.GroupBox(
                    background=colors[10],
                    highlight_method='text',
                    urgent_alert_method='text',
                    #------------------------------
                    active=colors[5], #Color for active non viewed screen
                    inactive=colors[9],
                    highlight_color=colors[3],
                    this_current_screen_border=colors[6],
                    this_screen_border=colors[2],
                    urgent_text=colors[1],
                    other_current_screen_border=colors[7],
                    other_screen_border=colors[8],
                ),
            widget.TextBox(
                    text=" 󱑀 ",
                    foreground=colors[4],
                    background=colors[10],
                    fontsize=16,
                    padding=0,
                     mouse_callbacks =
                        {'Button1' : lambda : qtile.cmd_spawn('morgen')},
                ),
            widget.Clock(
                    fontsize = 12,
                    background=colors[10],
                ),
            widget.TextBox(
                    text="",
                    foreground=colors[10],
                    background=colors[9],
                    fontsize=24,
                    padding=0,
                ),
            widget.Spacer(),
            widget.TextBox(
                    text="",
                    foreground=colors[10],
                    background=colors[9],
                    fontsize=24,
                    padding=0,
                ),
            widget.TextBox(
                    text=" ",
                    foreground=colors[5],
                    background=colors[10],
                    fontsize=16,
                    padding=0,
                    mouse_callbacks =
                        {'Button1' : lambda : qtile.cmd_spawn('godot')},
                ),
            widget.Sep(
                    padding=10,
                    background=colors[10],
                    linewidth=0,
                    ),
            widget.TextBox(
                    text="󱜆 ",
                    foreground=colors[5],
                    background=colors[10],
                    fontsize=16,
                    padding=0,
                    mouse_callbacks =
                        {'Button1' : lambda : qtile.cmd_spawn('obs')},
                ),
            widget.Sep(
                    padding=10,
                    background=colors[10],
                    linewidth=0,
                    ),
            widget.TextBox(
                    text="󰠥 ",
                    foreground=colors[2],
                    background=colors[10],
                    fontsize=16,
                    padding=0,
                    mouse_callbacks =
                        {'Button1' : lambda : qtile.cmd_spawn('virtualbox')},
                ),
            widget.Sep(
                    padding=10,
                    background=colors[10],
                    linewidth=0,
                    ),
            widget.TextBox(
                    text="󰂯 ",
                    foreground=colors[4],
                    background=colors[10],
                    fontsize=16,
                    padding=0,
                     mouse_callbacks =
                        {'Button1' : lambda : qtile.cmd_spawn('blueman-manager')},
                ),
            widget.Sep(
                    padding=10,
                    background=colors[10],
                    linewidth=0,
                    ),
            widget.TextBox(
                    text="󰈸",
                    foreground=colors[3],
                    background=colors[10],
                    fontsize=16,
                    padding=0,
                    mouse_callbacks =
                        {'Button1' : lambda : qtile.cmd_spawn('flameshot gui')},
                ),
            widget.TextBox(
                    text="",
                    foreground=colors[10],
                    background=colors[9],
                    fontsize=24,
                    padding=0,
                ),
            widget.Sep(
                    linewidth=0,
                    padding=10,
                    ),
            widget.Battery(
                    background = colors [9],
                    foreground = colors [6],
                    format = '{char}', #  {percent:1.0%}',
                    low_background= colors[1],
                    low_foreground= colors[8],
                    battery = 0,
                    charge_char = '󰂄',
                    discharge_char = '󰁹',
                    empty_char = '󰢜 ',
                    full_char = '󱟢 ',
                    unknown_char = '󱉝 ',
                    fontsize = 18, 
                    update_interval = 10,
                    show_short_text = False,
                ),
            widget.TextBox(
                    text=" ",
                    foreground=colors[1],
                    background=colors[9],
                    fontsize=18,
                    padding=0,
                    mouse_callbacks =
                        {'Button1' : lambda : qtile.cmd_spawn(os.path.expanduser('~/.config/rofi/powermenu.sh'))},
                ),
            widget.Sep(
                    linewidth=0,
                    padding=8,
                    ),
            ],
            24,
            background = '#0a0d1288',
            opacity = 0.7,
            margin=[6, 8, 6, 8],
            border_width=[3, 3, 3, 3],
            border_color=colors[9],
        ),
        bottom=bar.Gap(8),
        left=bar.Gap(8),
        right=bar.Gap(8),
    ),
#screen2___________________________________________________________
    Screen(
        wallpaper='~/Pictures/skullWall.jpg',
        wallpaper_mode='fill',

        top=bar.Bar(
             [
            widget.Sep(
                linewidth = 0,
                padding = 8,
                ),
            widget.CurrentLayoutIcon(
                    custom_icon_paths=['~/.config/qtile/icons'],
                    scale=0.7,
                    background = colors[10],
                ),
            widget.WindowName(),
            widget.TextBox(
                    text="",
                    foreground=colors[10],
                    background=colors[9],
                    fontsize=24,
                    padding=0,
                ),
            widget.TextBox(
                    text = '  ',
                    fontsize = 16,
                    background = colors [10],
                    foreground = colors [4],
                    padding_y = -2,
                    mouse_callbacks =
                        {'Button1': lambda : qtile.cmd_spawn('rofi -show drun')},
                ),
            widget.GroupBox(
                    background=colors[10],
                    highlight_method='text',
                    urgent_alert_method='text',
                    #------------------------------
                    active=colors[5], #Color for active non viewed screen
                    inactive=colors[9],
                    highlight_color=colors[3],
                    this_current_screen_border=colors[6],
                    this_screen_border=colors[2],
                    urgent_text=colors[1],
                    other_current_screen_border=colors[7],
                    other_screen_border=colors[8],
                ),
            widget.TextBox(
                    text=" 󱑁 ",
                    foreground=colors[4],
                    background=colors[10],
                    fontsize=16,
                    padding=0,
                     mouse_callbacks =
                        {'Button1' : lambda : qtile.cmd_spawn('morgen')},
                ),
            widget.Clock(
                    fontsize = 12,
                    background=colors[10],
                ),
            widget.TextBox(
                    text="",
                    foreground=colors[10],
                    background=colors[9],
                    fontsize=24,
                    padding=0,
                ),
            widget.Spacer(),
            widget.TextBox(
                    text="",
                    foreground=colors[10],
                    background=colors[9],
                    fontsize=24,
                    padding=0,
                ),
            widget.TextBox(
                    text=" ",
                    foreground=colors[5],
                    background=colors[10],
                    fontsize=16,
                    padding=0,
                    mouse_callbacks =
                        {'Button1' : lambda : qtile.cmd_spawn('godot')},
                ),
            widget.Sep(
                    padding=10,
                    background=colors[10],
                    linewidth=0,
                    ),
            widget.TextBox(
                    text="󱜆 ",
                    foreground=colors[5],
                    background=colors[10],
                    fontsize=16,
                    padding=0,
                    mouse_callbacks =
                        {'Button1' : lambda : qtile.cmd_spawn('obs')},
                ),
            widget.Sep(
                    padding=10,
                    background=colors[10],
                    linewidth=0,
                    ),
            widget.TextBox(
                    text="󰠥 ",
                    foreground=colors[2],
                    background=colors[10],
                    fontsize=16,
                    padding=0,
                    mouse_callbacks =
                        {'Button1' : lambda : qtile.cmd_spawn('virtualbox')},
                ),
            widget.Sep(
                    padding=10,
                    background=colors[10],
                    linewidth=0,
                    ),
            widget.TextBox(
                    text="󰂯 ",
                    foreground=colors[4],
                    background=colors[10],
                    fontsize=16,
                    padding=0,
                     mouse_callbacks =
                        {'Button1' : lambda : qtile.cmd_spawn('blueman-manager')},
                ),
            widget.Sep(
                    padding=10,
                    background=colors[10],
                    linewidth=0,
                    ),
            widget.TextBox(
                    text="󰈸",
                    foreground=colors[3],
                    background=colors[10],
                    fontsize=16,
                    padding=0,
                    mouse_callbacks =
                        {'Button1' : lambda : qtile.cmd_spawn('flameshot gui')},
                ),
            widget.TextBox(
                    text="",
                    foreground=colors[10],
                    background=colors[9],
                    fontsize=24,
                    padding=0,
                ),
            widget.Sep(
                    linewidth=0,
                    padding=10,
                    ),
            widget.Battery(
                    background = colors [9],
                    foreground = colors [6],
                    format = '{char}', #  {percent:1.0%}',
                    low_background= colors[1],
                    low_foreground= colors[8],
                    battery = 0,
                    charge_char = '󰂄',
                    discharge_char = '󰁹',
                    empty_char = '󰢜 ',
                    full_char = '󱟢 ',
                    unknown_char = '󱉝 ',
                    fontsize = 18, 
                    update_interval = 10,
                    show_short_text = False,
                ),
            widget.TextBox(
                    text=" ",
                    foreground=colors[1],
                    background=colors[9],
                    fontsize=18,
                    padding=0,
                    mouse_callbacks =
                        {'Button1' : lambda : qtile.cmd_spawn(os.path.expanduser('~/.config/rofi/powermenu.sh'))},
                ),
            widget.Sep(
                    linewidth=0,
                    padding=8,
                    ),
            ],
            24,
            background='#0a0d1288',
            opacity= 0.7,
            margin=[4,8,4,8],
            border_width=[2, 0, 2, 0],
            border_color=[colors[8]],
        ),
        bottom=bar.Gap(8),
        left=bar.Gap(8),
        right=bar.Gap(8),
   ),
#screen3___________________________________________________________
    Screen(
        wallpaper='~/Pictures/skullWall.jpg',
        wallpaper_mode='fill',

        top=bar.Bar(
             [
            widget.Sep(
                linewidth = 0,
                padding = 8,
                ),
            widget.CurrentLayoutIcon(
                    custom_icon_paths=['~/.config/qtile/icons'],
                    scale=0.7,
                    background = colors[10],
                ),
            widget.WindowName(),
            widget.TextBox(
                    text="",
                    foreground=colors[10],
                    background=colors[9],
                    fontsize=24,
                    padding=0,
                ),
            widget.TextBox(
                    text = '  ',
                    fontsize = 16,
                    background = colors [10],
                    foreground = colors [4],
                    padding_y = -2,
                    mouse_callbacks =
                        {'Button1': lambda : qtile.cmd_spawn('rofi -show drun')},
                ),
            widget.GroupBox(
                    background=colors[10],
                    highlight_method='text',
                    urgent_alert_method='text',
                    #------------------------------
                    active=colors[5], #Color for active non viewed screen
                    inactive=colors[9],
                    highlight_color=colors[3],
                    this_current_screen_border=colors[6],
                    this_screen_border=colors[2],
                    urgent_text=colors[1],
                    other_current_screen_border=colors[7],
                    other_screen_border=colors[8],
                ),
            widget.TextBox(
                    text=" 󱐿 ",
                    foreground=colors[4],
                    background=colors[10],
                    fontsize=16,
                    padding=0,
                     mouse_callbacks =
                        {'Button1' : lambda : qtile.cmd_spawn('morgen')},
                ),
            widget.Clock(
                    fontsize = 12,
                    background=colors[10],
                ),
            widget.TextBox(
                    text="",
                    foreground=colors[10],
                    background=colors[9],
                    fontsize=24,
                    padding=0,
                ),
            widget.Spacer(),
            widget.TextBox(
                    text="",
                    foreground=colors[10],
                    background=colors[9],
                    fontsize=24,
                    padding=0,
                ),
            widget.TextBox(
                    text=" ",
                    foreground=colors[5],
                    background=colors[10],
                    fontsize=16,
                    padding=0,
                    mouse_callbacks =
                        {'Button1' : lambda : qtile.cmd_spawn('godot')},
                ),
            widget.Sep(
                    padding=10,
                    background=colors[10],
                    linewidth=0,
                    ),
            widget.TextBox(
                    text="󱜆 ",
                    foreground=colors[5],
                    background=colors[10],
                    fontsize=16,
                    padding=0,
                    mouse_callbacks =
                        {'Button1' : lambda : qtile.cmd_spawn('obs')},
                ),
            widget.Sep(
                    padding=10,
                    background=colors[10],
                    linewidth=0,
                    ),
            widget.TextBox(
                    text="󰠥 ",
                    foreground=colors[2],
                    background=colors[10],
                    fontsize=16,
                    padding=0,
                    mouse_callbacks =
                        {'Button1' : lambda : qtile.cmd_spawn('virtualbox')},
                ),
            widget.Sep(
                    padding=10,
                    background=colors[10],
                    linewidth=0,
                    ),
            widget.TextBox(
                    text="󰂯 ",
                    foreground=colors[4],
                    background=colors[10],
                    fontsize=16,
                    padding=0,
                     mouse_callbacks =
                        {'Button1' : lambda : qtile.cmd_spawn('blueman-manager')},
                ),
            widget.Sep(
                    padding=10,
                    background=colors[10],
                    linewidth=0,
                    ),
            widget.TextBox(
                    text="󰈸",
                    foreground=colors[3],
                    background=colors[10],
                    fontsize=16,
                    padding=0,
                    mouse_callbacks =
                        {'Button1' : lambda : qtile.cmd_spawn('flameshot gui')},
                ),
            widget.TextBox(
                    text="",
                    foreground=colors[10],
                    background=colors[9],
                    fontsize=24,
                    padding=0,
                ),
            widget.Sep(
                    linewidth=0,
                    padding=10,
                    ),
            widget.Battery(
                    background = colors [9],
                    foreground = colors [6],
                    format = '{char}', #  {percent:1.0%}',
                    low_background= colors[1],
                    low_foreground= colors[8],
                    battery = 0,
                    charge_char = '󰂄',
                    discharge_char = '󰁹',
                    empty_char = '󰢜 ',
                    full_char = '󱟢 ',
                    unknown_char = '󱉝 ',
                    fontsize = 18, 
                    update_interval = 10,
                    show_short_text = False,
                ),
            widget.TextBox(
                    text=" ",
                    foreground=colors[1],
                    background=colors[9],
                    fontsize=18,
                    padding=0,
                    mouse_callbacks =
                        {'Button1' : lambda : qtile.cmd_spawn(os.path.expanduser('~/.config/rofi/powermenu.sh'))},
                ),
            widget.Sep(
                    linewidth=0,
                    padding=8,
                    ),
            ],
            24,
            background='#0a0d1288',
            opacity= 0.7,
            margin=[4,8,4,8],
            border_width=[2, 0, 2, 0],
            border_color=[colors[8]],
        ),
        bottom=bar.Gap(8),
        left=bar.Gap(8),
        right=bar.Gap(8),
   ),

]


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

@hook.subscribe.startup_once
def autostart():
    home = '/home/agaho/.config/qtile/autostart.sh'
    subprocess.call([home])

@hook.subscribe.client_new
def set_floating(window):
    if (window.window.get_wm_transient_for()
            or window.window.get_wm_type() in floating_types):
        window.floating = True

floating_types = ["notification", "toolbar", "splash", "dialog","tkinter"]

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