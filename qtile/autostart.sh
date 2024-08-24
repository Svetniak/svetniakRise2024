#!/bin/bash

xrandr --output eDP-1 --off
xrandr --output DP-1 --mode 2560x1440 --primary --pos 0x0 
xrandr --output HDMI-1 --mode 2560x1440 --pos 2560x0 
picom & disown
