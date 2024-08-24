'''
 ________   ________  ________  ________  ___          
|\   ___  \|\   __  \|\   __  \|\   __  \|\  \         
\ \  \\ \  \ \  \|\  \ \  \|\  \ \  \|\  \ \  \        
 \ \  \\ \  \ \  \\\  \ \   ____\ \   __  \ \  \       
  \ \  \\ \  \ \  \\\  \ \  \___|\ \  \ \  \ \  \____  
   \ \__\\ \__\ \_______\ \__\    \ \__\ \__\ \_______\
    \|__| \|__|\|_______|\|__|     \|__|\|__|\|_______|
'''

import os
import re
import socket
import subprocess
from typing import List  # noqa: F401
from libqtile import layout, bar, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen, Rule, ScratchPad, DropDown
from libqtile.command import lazy
#from liqtile import hook

#mod4 or mod = super key
mod = "mod4"
mod1 = "alt"
mod2 = "control"
home = os.path.expanduser('~')
#Prefered terminal
myTerm = "kitty"  

@lazy.function
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

@lazy.function
def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)


keys = [

# SUPER + FUNCTION KEYS
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod], "q", lazy.window.kill()),
    Key([mod], "t", lazy.spawn('thunar')),
    Key([mod], "e", lazy.spawn('thunar')),
    Key([mod], "v", lazy.spawn('virtualbox')),
    Key([mod], "d", lazy.spawn('nwggrid -p -o 0.4')),
    Key([mod], "Escape", lazy.spawn('xkill')),
    Key([mod], "Return", lazy.spawn(myTerm)),
    Key([mod], "KP_Enter", lazy.spawn('alacritty')),
    Key([mod], "x<D-a>", lazy.shutdown()),
    Key([mod], "r", lazy.spawncmd()),
    Key([mod], "m", lazy.spawn('thunderbird')),
    Key([mod], "u", lazy.spawn('unityhub')),
    Key([mod], "b", lazy.spawn('blender')),
    Key([mod], "s", lazy.spawn('inkscape')),
    Key([mod], "g", lazy.spawn('gimp')),

# SUPER + SHIFT KEYS
    Key([mod, "shift"], "Return", lazy.spawn('pcmanfm')),
    Key([mod, "shift"], "d", lazy.spawn("dmenu_run -i -nb '#191919' -nf '#ff1493' -sb '#ff1493' -sf '#191919' -fn 'NotoMonoRegular:bold:pixelsize=15'")),
#    Key([mod, "shift"], "d", lazy.spawn(home + '/.config/qtile/scripts/dmenu.sh')),
    Key([mod, "shift"], "q", lazy.window.kill()),
    Key([mod, "shift"], "r", lazy.restart()),
    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "shift"], "x", lazy.shutdown()),

# CONTROL + ALT KEYS
    Key(["mod1", "control"], "o", lazy.spawn(home + '/.config/qtile/scripts/picom-toggle.sh')),
    Key(["mod1", "control"], "t", lazy.spawn('xterm')),
    Key(["mod1", "control"], "u", lazy.spawn('pavucontrol')),
    Key(["mod1", "control"], "f", lazy.spawn('firefox')),


# ALT + ... KEYS
    Key(["mod1"], "p", lazy.spawn('pamac-manager')),
    Key(["mod1"], "f", lazy.spawn('firefox')),
    Key(["mod1"], "m", lazy.spawn('pcmanfm')),
    Key(["mod1"], "w", lazy.spawn('garuda-welcome')),

# CONTROL + SHIFT KEYS
    Key([mod2, "shift"], "Escape", lazy.spawn('lxtask')),


# SCREENSHOTS
    Key([], "Print", lazy.spawn('flameshot full -p ' + home + '/Pictures')),
    Key([mod2], "Print", lazy.spawn('flameshot full -p ' + home + '/Pictures')),
#    Key([mod2, "shift"], "Print", lazy.spawn('gnome-screenshot -i')),

# MULTIMEDIA KEYS

# INCREASE/DECREASE BRIGHTNESS
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl s +5%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl s 5%- ")),

# INCREASE/DECREASE/MUTE VOLUME
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 5%-")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 5%+")),

    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),

#    Key([], "XF86AudioPlay", lazy.spawn("mpc toggle")),
#    Key([], "XF86AudioNext", lazy.spawn("mpc next")),
#    Key([], "XF86AudioPrev", lazy.spawn("mpc prev")),
#    Key([], "XF86AudioStop", lazy.spawn("mpc stop")),

# QTILE LAYOUT KEYS
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "space", lazy.next_layout()),

# CHANGE FOCUS
    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),


# RESIZE UP, DOWN, LEFT, RIGHT
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


# FLIP LAYOUT FOR MONADTALL/MONADWIDE
    Key([mod, "shift"], "f", lazy.layout.flip()),

# FLIP LAYOUT FOR BSP
    Key([mod, "mod1"], "k", lazy.layout.flip_up()),
    Key([mod, "mod1"], "j", lazy.layout.flip_down()),
    Key([mod, "mod1"], "l", lazy.layout.flip_right()),
    Key([mod, "mod1"], "h", lazy.layout.flip_left()),

# MOVE WINDOWS UP OR DOWN BSP LAYOUT
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),

         ### Treetab controls
    Key([mod, "control"], "k",
        lazy.layout.section_up(),
        desc='Move up a section in treetab'
        ),
    Key([mod, "control"], "j",
        lazy.layout.section_down(),
        desc='Move down a section in treetab'
        ),



# MOVE WINDOWS UP OR DOWN MONADTALL/MONADWIDE LAYOUT
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Left", lazy.layout.swap_left()),
    Key([mod, "shift"], "Right", lazy.layout.swap_right()),

# TOGGLE FLOATING LAYOUT
    Key([mod, "shift"], "space", lazy.window.toggle_floating()),]

groups = []
group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0",]
group_labels = ["", "", "", "", "", "", "", "", "", "",]
group_layouts = ["monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "treetab", "floating"]

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


def init_layout_theme():
    return {"margin":6,
            "border_width":1,
            "border_focus": "#7dcfff",
            "border_normal": "#bb9af7"
            }

layout_theme = init_layout_theme()

layouts = [
    layout.MonadTall(margin=6, border_width=1, border_focus="#7dcfff", border_normal="#bb9af7"),
    layout.MonadWide(margin=6, border_width=1, border_focus="#7dcfff", border_normal="#bb9af7"),
    layout.Matrix(**layout_theme),
    layout.Bsp(**layout_theme),
    layout.Floating(**layout_theme),
    layout.RatioTile(**layout_theme),
    layout.Max(**layout_theme),
    layout.Columns(**layout_theme),
    layout.Stack(**layout_theme),
    layout.Tile(**layout_theme),
    layout.TreeTab(
        sections=['FIRST', 'SECOND'],
        bg_color = '#141414',
        active_bg = '#7dcfff',
        inactive_bg = '#bb9af7',
        padding_y =5,
        section_top =10,
        panel_width = 280),
    layout.VerticalTile(**layout_theme),
    layout.Zoomy(**layout_theme)
]

# ScratchPads
groups.append(
        ScratchPad(
            'scratchpad', [
                DropDown('term', 'kitty', width=0.8, height=0.7, x=0.1, y=0.1, opacity=1.0),
                DropDown('fm', 'pcmanfm', width=0.4, height=0.5, x=0.3, y=0.1, opacity=0.5),
                ]
            )
        )

# Extend keys for scratchPad
keys.extend(
        [
            Key(["control"], "Return", lazy.group['scratchpad'].dropdown_toggle('term')),
            # Key(["control"], "s", lazy.group['scratchpad'].dropdown_toggle('fm')),
            ]
        )

# COLORS FOR THE BAR
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
            ["#1a1b26", "#1a1b26"]] # color 9

colors = init_colors()

def base(fg='text', bg='dark'):
    return {'foreground': colors[9],'background': colors[0]}


# WIDGETS FOR THE BAR

def init_widgets_defaults():
    return dict(font="Noto Sans",
                fontsize = 9,
                padding = 2,
                background=colors[1])

widget_defaults = init_widgets_defaults()

def init_widgets_list():
    prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
    widgets_list = [
        widget.Sep(
            linewidth = 1,
            padding = 10,
            foreground = colors[0],
            background = colors[0]
            ),
        widget.TextBox(
            text = '󱩊 ',
            fontsize = 16,
            background = colors [0],
            foreground = colors [4],
            padding_y = -2,
            mouse_callbacks =
                {'Button1': lambda : qtile.cmd_spawn('rofi -show combi')},
            ),
        widget.Sep(
            linewidth = 1,
            padding = 10,
            foreground = colors[0],
            background = colors[0]
            ),
        widget.TextBox(
            text = '',
            fontsize = 20,
            background = colors [9],
            foreground = colors [0],
            padding = 0,
            ),
        widget.GroupBox(
            background = colors [9],
            font='UbuntuMono Nerd Font',
             fontsize = 10,
             margin_y = 3,
             margin_x = 2,
             padding_y = 5,
             padding_x = 4,
             borderwidth = 3,
            active=colors[4],
            inactive=colors[5],
            rounded= True,
            highlight_method='text',
            urgent_alert_method='text',
            urgent_border=colors[6],
            this_current_screen_border=colors[1],
            this_screen_border=colors[7],
            other_current_screen_border=colors[3],
            other_screen_border=colors[7],
            disable_drag=True
            ),
        widget.TextBox(
            text = '',
            fontsize = 20,
            background = colors [9],
            foreground = colors [1],
            padding = 0,
            ),
        widget.Prompt(
            font = "Noto Sans",
            fontsize = 10,
            background = colors [9],
            foreground = colors [1],
            prompt = ' 󰀻 :',
            ),
        widget.TextBox(
            text = '',
            fontsize = 20,
            background = colors [9],
            foreground = colors [1],
            padding = 0,
            ),
        widget.WindowName(
            font = "Noto Sans",
            fontsize = 10,
            background = colors [9],
            foreground = colors [5],
            max_char = 150,
            ),
        widget.TextBox(
            text = '',
            fontsize = 18,
            background = colors [9],
            foreground = colors [4],
            padding = 0,
            ),

#        widget.TextBox(
#           text = '',
#           fontsize = 20,
#           background = colors [1],
#           foreground = colors [5],
#           padding = 0,
#           ),
#        widget.TextBox(
#           text = '󰔫 ',
#           fontsize = 18,
#           background = colors [5],
#           foreground = colors [1],
#           padding = 0,
#           ),
#        widget.Net(
#           font="Noto Sans",
#           fontsize=10,
#           interface=["wlan0"],
#           format = '{down} ↓↑ {up}',
#           foreground=colors[1],
#           background=colors[7],
#           padding = 0,
#           ),
#        widget.TextBox(
#           text = '',
#           fontsize = 20,
#           background = colors [0],
#           foreground = colors [1],
#           padding = 0,
#           ),
#        widget.TextBox(
#           text = ' ',
#           fontsize = 16,
#           background = colors [0],
#           foreground = colors [2],
#           padding = 0,
#           ),
#        widget.CPU(
#           font="Noto Sans",
#           update_interval = 1,
#           fontsize = 10,
#           foreground = colors[3],
#           background = colors[0],
#           mouse_callbacks = {'Button1': lambda : qtile.cmd_spawn(myTerm + ' -e btop')},
#           ),
#        widget.TextBox(
#           text = '',
#           fontsize = 20,
#           background = colors [0],
#           foreground = colors [3],
#           padding = 0,
#           ),
#        widget.TextBox(
#           text = '󰍛 ',
#           fontsize = 18,
#           background = colors [0],
#           foreground = colors [6],
#           padding = 0,
#           ),
#        widget.Memory(
#           font="Noto Sans",
#           format = '{MemUsed: .0f}M/{MemTotal: .0f}M',
#           update_interval = 1,
#           fontsize = 10,
#           measure_mem = 'M',
#           foreground = colors[6],
#           background = colors[1],
#           mouse_callbacks = {'Button1': lambda : qtile.cmd_spawn(myTerm + ' -e htop')},
#           ),
#        widget.TextBox(
#           text = '',
#           fontsize = 20,
#           background = colors [0],
#           foreground = colors [8],
#           padding = 0,
#           ),

        widget.TextBox(
            text = '󰸗 ',
            fontsize = 16,
            background = colors [4],
            foreground = colors [0],
            padding = 1,
            ),
        widget.Clock(
            foreground = colors[0],
            background = colors[4],
            fontsize = 10,
            format="%Y-%m-%d %H:%M"
            ),
        widget.TextBox(
            text = '',
            fontsize = 20,
            background = colors [4],
            foreground = colors [0],
            padding = 0,
            ),
        widget.CurrentLayoutIcon(
            custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
            foreground = colors[9],
            background = colors[0],
            padding = 0,
            margin=0,
            scale = 0.7
            ),
        widget.TextBox(
            text = '',
            fontsize = 20,
            background = colors [0],
            foreground = colors [9],
            padding = 0,
            ),
        widget.Volume(
            background = colors[9],
            foreground = colors[6],
            fontsize = 14,
            cardid = 'CARD=PCH',
            channel='Master',
            emoji = False,
            theme_path = '~/.config/qtile/volume'
            ),
        widget.Battery(
            background = colors [9],
            foreground = colors [2],
            format = '{char}  {percent:1.0%}',
            low_background= colors[1],
            low_foreground= colors[8],
            battery = 0,
            charge_char = '󰂄',
            discharge_char = '󰁹',
            empty_char = '󰢜 ',
            full_char = '󱟢 ',
            unknown_char = '󱉝 ',
            fontsize = 9, 
            update_interval = 10,
            show_short_text = False,
            ),
        widget.TextBox(
            text = '',
            fontsize= 20,
            background= colors [9],
            foreground= colors [3],
            padding =  0,
            ),
        widget.CheckUpdates(
            background = colors [9],
            foreground = colors [5],
            display_format = '󰝧 ',
            no_udate_string = '󰞑 ',
            restart_indicator = '󰛹 ',
            colour_have_updates = colors [1],
            colour_no_updates = colors [4],
            update_interval = 5,
            ),
        widget.TextBox(
            text = ' ',
            foreground = colors [2],
            background = colors [9],
            fontsize = 14,
            padding = 2,
            mouse_callbacks= {'Button1': lambda: qtile.cmd_spawn(os.path.expanduser('~/.config/rofi/powermenu.sh'))},
            ),
        widget.Systray(
            background = colors [9],
            foreground = colors [3],
            icon_size = 10,
            padding = 0,
            ),
        widget.Sep(
            linewidth = 0,
            padding = 10,
            foreground = colors[0],
            background = colors[9]
            ),
             ]
    return widgets_list

widgets_list = init_widgets_list()


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2

def init_widgets_screen3():
    widgets_screen3 = init_widgets_list()
    return widgets_screen3

widgets_screen1 = init_widgets_screen1()
widgets_screen2 = init_widgets_screen2()
widgets_screen2 = init_widgets_screen3()

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), size=16, opacity=0.99, background= "000000")),
        ]

screens = init_screens()


# MOUSE CONFIGURATION
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size())
]

dgroups_key_binder = None
dgroups_app_rules = []

# ASSIGN APPLICATIONS TO A SPECIFIC GROUPNAME
# BEGIN

#########################################################
################ assgin apps to groups ##################
#########################################################
# @hook.subscribe.client_new
# def assign_app_group(client):
#     d = {}
#     #########################################################
#     ################ assgin apps to groups ##################
#     #########################################################
#     d["1"] = ["Navigator", "Firefox", "Vivaldi-stable", "Vivaldi-snapshot", "Chromium", "Google-chrome", "Brave", "Brave-browser",
#               "navigator", "firefox", "vivaldi-stable", "vivaldi-snapshot", "chromium", "google-chrome", "brave", "brave-browser", ]
#     d["2"] = [ "Atom", "Subl3", "Geany", "Brackets", "Code-oss", "Code", "TelegramDesktop", "Discord",
#                "atom", "subl3", "geany", "brackets", "code-oss", "code", "telegramDesktop", "discord", ]
#     d["3"] = ["Inkscape", "Nomacs", "Ristretto", "Nitrogen", "Feh",
#               "inkscape", "nomacs", "ristretto", "nitrogen", "feh", ]
#     d["4"] = ["Gimp", "gimp" ]
#     d["5"] = ["Meld", "meld", "org.gnome.meld" "org.gnome.Meld" ]
#     d["6"] = ["Vlc","vlc", "Mpv", "mpv" ]
#     d["7"] = ["VirtualBox Manager", "VirtualBox Machine", "Vmplayer",
#               "virtualbox manager", "virtualbox machine", "vmplayer", ]
#     d["8"] = ["pcmanfm", "Nemo", "Caja", "Nautilus", "org.gnome.Nautilus", "Pcmanfm", "Pcmanfm-qt",
#               "pcmanfm", "nemo", "caja", "nautilus", "org.gnome.nautilus", "pcmanfm", "pcmanfm-qt", ]
#     d["9"] = ["Evolution", "Geary", "Mail", "Thunderbird",
#               "evolution", "geary", "mail", "thunderbird" ]
#     d["0"] = ["Spotify", "Pragha", "Clementine", "Deadbeef", "Audacious",
#               "spotify", "pragha", "clementine", "deadbeef", "audacious" ]
#     ##########################################################
#     wm_class = client.window.get_wm_class()[0]
#
#     for i in range(len(d)):
#         if wm_class in list(d.values())[i]:
#             group = list(d.keys())[i]
#             client.togroup(group)
#             client.group.cmd_toscreen()

# END
# ASSIGN APPLICATIONS TO A SPECIFIC GROUPNAME



main = None

@hook.subscribe.startup_once
def autostart():
    #    home = os.path.expanduser('~/.config/qtile/scripts/autostart.sh')
    home = os.path.expanduser('/home/ikki/.config/qtile/autostart.sh')
    subprocess.call([home])

@hook.subscribe.startup
def start_always():
    # Set the cursor to something sane in X
    subprocess.Popen(['xsetroot', '-cursor_name', 'left_ptr'])

@hook.subscribe.client_new
def set_floating(window):
    if (window.window.get_wm_transient_for()
            or window.window.get_wm_type() in floating_types):
        window.floating = True

floating_types = ["notification", "toolbar", "splash", "dialog"]


follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    *layout.Floating.default_float_rules,
    Match(wm_class='confirm'),
    Match(wm_class='dialog'),
    Match(wm_class='download'),
    Match(wm_class='error'),
    Match(wm_class='file_progress'),
    Match(wm_class='notification'),
    Match(wm_class='splash'),
    Match(wm_class='toolbar'),
    Match(wm_class='confirmreset'),
    Match(wm_class='makebranch'),
    Match(wm_class='maketag'),
    Match(wm_class='Arandr'),
    Match(wm_class='feh'),
    Match(wm_class='Galculator'),
    Match(title='branchdialog'),
    Match(title='Open File'),
    Match(title='pinentry'),
    Match(wm_class='ssh-askpass'),
    Match(wm_class='lxpolkit'),
    Match(wm_class='Lxpolkit'),
    Match(wm_class='yad'),
    Match(wm_class='Yad'),
    Match(wm_class='Cairo-dock'),
    Match(wm_class='cairo-dock'),


],  fullscreen_border_width = 0, border_width = 0)
auto_fullscreen = True

focus_on_window_activation = "focus" # or smart

wmname = "LG3D"
