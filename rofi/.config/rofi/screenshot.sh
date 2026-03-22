#!/usr/bin/env bash

options="󰹑  Full (All)\n󰍹  Select Area or Screen\n󱣴  Active Window"

chosen=$(echo -e "$options" | rofi -dmenu -i -p "Screenshot" -theme-str 'window {width: 350px;}')

[ -z "$chosen" ] && exit 0

DIR="$HOME/Pictures/Screenshots"
mkdir -p "$DIR"
FILE="$DIR/screenshot_$(date +%Y%m%d_%H%M%S).png"

case "$chosen" in
    "󰹑  Full (All)")
        sleep 1 && maim "$FILE"
        ;;
    "󰍹  Select Area or Screen")
        maim -s "$FILE"
        ;;
    "󱣴  Active Window")
        maim -i $(xdotool getactivewindow) "$FILE"
        ;;
esac

