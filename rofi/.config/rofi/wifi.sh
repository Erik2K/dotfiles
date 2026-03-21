#!/bin/bash

# Lista redes WiFi disponibles
SSID=$(nmcli -t -f SSID dev wifi | sort -u | rofi -dmenu -i -p "Select WiFi")

if [ -n "$SSID" ]; then
    # Intenta conectarse
    nmcli dev wifi connect "$SSID" || \
    # Si falla (normalmente por contraseña), pide la contraseña
    PASSWORD=$(rofi -dmenu -password -p "Password for $SSID")
    if [ -n "$PASSWORD" ]; then
        nmcli dev wifi connect "$SSID" password "$PASSWORD"
    fi
fi
