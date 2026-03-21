import os
import subprocess

from libqtile import bar, hook, extension, layout

from libqtile.layout.columns import Columns
from libqtile.layout.floating import Floating
from libqtile.config import (
    Click,
    Match,
    Drag,
    DropDown,
    Group,
    Key,
    ScratchPad,
    Screen
)

from libqtile.lazy import lazy
from libqtile.layout.max import Max

from colors import gruvbox
from custom_bar import bar

mod = "mod4"
terminal = "kitty"

# ██╗  ██╗███████╗██╗   ██╗██████╗ ██╗███╗   ██╗██████╗ ███████╗
# ██║ ██╔╝██╔════╝╚██╗ ██╔╝██╔══██╗██║████╗  ██║██╔══██╗██╔════╝
# █████╔╝ █████╗   ╚████╔╝ ██████╔╝██║██╔██╗ ██║██║  ██║███████╗
# ██╔═██╗ ██╔══╝    ╚██╔╝  ██╔══██╗██║██║╚██╗██║██║  ██║╚════██║
# ██║  ██╗███████╗   ██║   ██████╔╝██║██║ ╚████║██████╔╝███████║
# ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═════╝ ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝

keys = [
    # Move window focus
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "space", lazy.layout.next()),
    
    # Move window
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    
    # Grow window
    Key([mod, "control"], "h", lazy.layout.grow_left()),
    Key([mod, "control"], "l", lazy.layout.grow_right()),
    Key([mod, "control"], "j", lazy.layout.grow_down()),
    Key([mod, "control"], "k", lazy.layout.grouw_up()),
    
    # Reset all window sizes
    Key([mod], "n", lazy.layout.normalize()),
    
    # Toggle fullscreen window
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    
    # Toggle floating window
    Key([mod, "shift"], "space", lazy.window.toggle_floating()),
    
    # Kill focused window
    Key([mod], "w", lazy.window.kill()),
    
    # Move screen focus
    Key([mod], "Right", lazy.next_screen()),
    
    # Split stack layout
    Key([mod, "shift"], "Return", lazy.layout.toggle_split()),

    # Toggle layouts
    Key([mod], "Tab", lazy.next_layout()),

    # Launch terminal
    Key([mod], "Return", lazy.spawn(terminal)),

    # Launch rofi
    Key([mod], "p", lazy.spawn("rofi -show drun")),    

    # Lock screen
    Key([mod], "l", lazy.spawn("i3lock-fancy -p")),

    # Audio
    Key([], "XF86AudioPlay", lazy.spawn("playerctl -p chromium play-pause"), desc="Toggle Play/Pause"),
    Key([], "XF86AudioNext", lazy.spawn("playerctl -p chromium next"), desc="Siguiente canción"),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl -p chromium previous"), desc="Anterior canción"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%"), desc="Subir Volumen"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%"), desc="Bajar Volumen"),

    # Reload qtile config
    Key([mod, "control"], "r", lazy.reload_config()),
]

#  ██████╗ ██████╗  ██████╗ ██╗   ██╗██████╗ ███████╗
# ██╔════╝ ██╔══██╗██╔═══██╗██║   ██║██╔══██╗██╔════╝
# ██║  ███╗██████╔╝██║   ██║██║   ██║██████╔╝███████╗
# ██║   ██║██╔══██╗██║   ██║██║   ██║██╔═══╝ ╚════██║
# ╚██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║     ███████║
#  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝     ╚══════╝                                            

groups = [Group(f"{i + 1}", label="") for i in range(8)]

for i in groups:
    keys.extend(
        [
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
    )

        
# ██╗      █████╗ ██╗   ██╗ ██████╗ ██╗   ██╗████████╗███████╗
# ██║     ██╔══██╗╚██╗ ██╔╝██╔═══██╗██║   ██║╚══██╔══╝██╔════╝
# ██║     ███████║ ╚████╔╝ ██║   ██║██║   ██║   ██║   ███████╗
# ██║     ██╔══██║  ╚██╔╝  ██║   ██║██║   ██║   ██║   ╚════██║
# ███████╗██║  ██║   ██║   ╚██████╔╝╚██████╔╝   ██║   ███████║
# ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝  ╚═════╝    ╚═╝   ╚══════╝

layouts = [
    Columns(
        border_normal=gruvbox['bg'],
        border_focus=gruvbox['bg3'],
        border_width=2,
        border_normal_stack=gruvbox['bg'],
        border_focus_stack=gruvbox['bg3'],
        border_on_single=2,
        margin=10,
        margin_on_single=20,
    ),
    Max(
        border_normal=gruvbox['bg'],
        border_focus=gruvbox['bg3'],
        border_width=2,
        num_stacks=1,
        margin=20,
    ),
]

floating_layout = Floating(
    border_normal=gruvbox['bg1'],
    border_focus=gruvbox['red'],
    border_width=2,
    float_rules=[
        *Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)

mouse = [
    Drag(
        [mod], 
        "Button1", 
        lazy.window.set_position_floating(), 
        start=lazy.window.get_position()
    ),
    Drag(
        [mod], 
        "Button3", 
        lazy.window.set_size_floating(), 
        start=lazy.window.get_size()
    ),
    Click(
        [mod], 
        "Button2", 
        lazy.window.bring_to_front()
    ),
]

widget_defaults = dict(
    font='Hack Nerd Font Mono',
    fontsize=12,
    padding=10,
    background=gruvbox['bg'],
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar,
        wallpaper='~/.config/qtile/wallpapers/red-samurai-wallpaper.png',
        wallpaper_mode='stretch',
    ),
    Screen(
        wallpaper='~/.config/qtile/wallpapers/red-samurai-wallpaper.png',
        wallpaper_mode='stretch',
    ),
    Screen(
        wallpaper='~/.config/qtile/wallpapers/red-samurai-wallpaper.png',
        wallpaper_mode='stretch',
    ),
]

dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = False
bring_front_click = ''
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wmname = "LG3D"


# ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗███████╗
# ██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝██╔════╝
# ███████║██║   ██║██║   ██║█████╔╝ ███████╗
# ██╔══██║██║   ██║██║   ██║██╔═██╗ ╚════██║
# ██║  ██║╚██████╔╝╚██████╔╝██║  ██╗███████║
# ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝

# Runs the autostart script
@hook.subscribe.startup_once
def autostart():
    import os
    import subprocess

    autostart_script = os.path.expanduser('~/.config/qtile/autostart.sh')
    env = os.environ.copy()
    env['DISPLAY'] = ':0'  # O el display correcto, normalmente :0

    # Llamar con shell=False usando sh
    subprocess.Popen(['/bin/sh', autostart_script], env=env)
