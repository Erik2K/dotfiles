from libqtile import qtile
import subprocess

def network_status():
    try:
        # Obtener todas las conexiones activas
        output = subprocess.check_output(
            "nmcli -t -f NAME,TYPE con show --active",
            shell=True
        ).decode("utf-8").strip().splitlines()

        if not output:
            return "󰤮  Offline"

        # Tomamos la primera conexión activa
        name, con_type = output[0].split(":")
        
        # Detectar tipo correctamente según la salida real
        if con_type in ("802-11-wireless", "wifi"):
            return f"󰖩  {name}"  # icono WiFi
        elif con_type in ("ethernet", "802-3-ethernet"):
            return f"󰛳  {name}"  # icono cable
        else:
            return f"󰤬  {name}"

    except Exception:
        return "󰤫  Error"
