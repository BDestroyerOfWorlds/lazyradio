import subprocess

def wifi_restart():
    try:
        subprocess.run(["nmcli", "radio", "wifi", "off"], check=True)
        subprocess.run(["nmcli", "radio", "wifi", "on"], check=True)
        subprocess.run(["systemctl", "restart", "NetworkManager.service"], check=True)
    except:
        print("nmcli and systemctl failed, using rfkill instead.")
        subprocess.run(["rfkill", "block", "wifi"])
        subprocess.run(["rfkill", "unblock", "wifi"])


# BUG HERE, IF NMCLI WIFI OFF WORKS AND SOMEHOW NMCLI WIFI ON DOESNT USER IS LEFT WITH NO WIFI

def wifi_on():
    subprocess.run(["rfkill", "unblock", "wifi"])
    subprocess.run(["systemctl", "start", "NetworkManager.service"], check=True)
    subprocess.run(["nmcli", "radio", "wifi", "on"], check=True)

def wifi_off():
    subprocess.run(["rfkill", "block", "wifi"])
    subprocess.run(["nmcli", "radio", "wifi", "off"], check=True)
    subprocess.run(["systemctl", "stop", "NetworkManager.service"], check=True)