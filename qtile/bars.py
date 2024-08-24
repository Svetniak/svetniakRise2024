def widgetList():
    widget_list =[
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
                    text="󰥔 ",
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
            ]
    return widget_list
