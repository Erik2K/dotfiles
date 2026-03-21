import subprocess

from libqtile.bar import Bar
from libqtile import widget
from libqtile.lazy import lazy

from network import network_status

bar = Bar(
    [
        widget.Spacer(
            length=15,
            background="#0F1212"
        ),
        widget.Image(
            filename="~/.config/qtile/Assets/arch-logo.png",
            margin=4,
            background="#0F1212"
        ),
        widget.Image(
            filename="~/.config/qtile/Assets/6.png",
        ),
        widget.GroupBox(
            font="Hack Nerd Font Mono",
            fontsize=24,
            borderwidth=3,
            highlight_method="text",
            active="#ebdbb2",
            inactive="#0f1212",
            background="#202222",
            this_current_screen_border="#ac2531",
            rounded=True,
            disable_drag=True,
        ),
        widget.Spacer(
            length=8,
            background="#202222"
        ),
        widget.Image(
            filename="~/.config/qtile/Assets/1.png",
        ),
        widget.CurrentLayout(
            mode="icon",
            custom_icon_paths=["~/.config/qtile/Assets/layout"],
            background="#202222",
            scale=0.50,
        ),
        widget.Image(
            filename="~/.config/qtile/Assets/5.png",
        ),
        widget.Spacer(
            length=25,
            background="#0f1212"
        ),
        widget.Image(
            filename="~/.config/qtile/Assets/4.png",
        ),
        widget.WindowName(
            background="#202222",
            font="JetBrainsMono Nerd Font Bold",
            fontsize=13,
            empty_group_string="Desktop",
            max_chars=130,
            foreground="#ebdbb2",
        ),
        widget.Image(
            filename="~/.config/qtile/Assets/3.png",
        ),
        widget.Spacer(
            length=25,
            background="#0f1212"
        ),
        widget.Image(
            filename="~/.config/qtile/Assets/6.png",
            background="#202222",
        ),
        widget.GenPollText(
            func=network_status,
            background="#202222",
            foreground="#ebdbb2",
            font="Hack Nerd Font",
            fontsize=13,
            update_interval=5,
            width=100,
            max_chars=12,
            text_alignment="center",
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn("/home/erik/.config/rofi/wifi.sh")
            }
        ),
        widget.Image(
            filename="~/.config/qtile/Assets/2.png",
        ),
        widget.Spacer(
            length=8,
            background="#202222",
        ),
        widget.TextBox(
            text=" ",
            font="Font Awesome 6 Free Solid",
            fontsize=13,
            width=18,
            background="#202222",
            foreground="#ebdbb2",
        ),
        widget.Battery(
            font="JetBrainsMono Nerd Font Bold",
            fontsize=13,
            width=32,
            background="#202222",
            foreground="#ebdbb2",
            format="{percent:2.0%}",
        ),
        widget.Image(
            filename="~/.config/qtile/Assets/2.png",
        ),
        widget.Spacer(
            length=8,
            background="#202222",
        ),
        widget.TextBox(
            text="󰎆 ",
            font="JetBrainsMono Nerd Font Bold",
            fontsize=15,
            background="#202222",
            foreground="#ebdbb2",
        ),
        widget.GenPollText(
            func=lambda: (
                subprocess.check_output([
                    "playerctl", "-i", "brave", "-p", "chromium", "metadata", 
                    "--format", "{{title}} - {{artist}}"
                ])
                .decode("utf-8")
                .strip() 
                if subprocess.run(
                    ["playerctl", "-i", "brave", "-p", "chromium", "status"], 
                    capture_output=True
                ).returncode == 0 
                else "YouTube Music"
            ),
            update_interval=2,
            font="JetBrainsMono Nerd Font Bold",
            fontsize=13,
            background="#202222",
            foreground="#ebdbb2",
            width=120,
            scroll_chars=None,
            max_chars=16,
            mouse_callbacks={
                'Button1': lazy.spawn("playerctl play-pause"),
                'Button3': lazy.spawn("playerctl next"),
            },
        ),
        widget.Image(
            filename="~/.config/qtile/Assets/5.png",
            background="#202222",
        ),
        widget.TextBox(
            text=" ",
            font="Font Awesome 6 Free Solid",
            fontsize=13,
            width=12,
            background="#0f1212",
            foreground="#ebdbb2",
        ),
        widget.Clock(
            format="%H:%M",
            background="#0f1212",
            foreground="#ebdbb2",
            font="JetBrainsMono Nerd Font Bold",
            fontsize=13,
        ),
        widget.Spacer(
            length=18,
            background="#0f1212",
        ),
    ],
    30,
    border_width=[0, 0, 0, 0],
    margin=[15, 60, 6, 60],
)
