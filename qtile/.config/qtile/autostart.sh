#!/bin/sh

# Cursor
export XCURSOR_THEME=Bibata-Modern-Classic
export XCURSOR_SIZE=24
xsetroot -cursor_name left_ptr

# screensaver and DPMS
xset s off
xset s noblank
xset -dpms

# Idle + lock
xidlehook \
  --not-when-fullscreen \
  --not-when-audio \
  --timer 300 '~/.local/bin/lock.sh' '' \
  --timer 600 'xset dpms force off' '' &

# Display configutation
~/.config/qtile/displays/triple-monitor-layout.sh

# Programs
picom &
