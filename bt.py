import subprocess

def bt_restart():
    subprocess.run(["systemctl", "restart", "bluetooth"], check=True)

def bt_on():
    subprocess.run(["systemctl", "enable","--now", "bluetooth"], check=True)

def bt_off():
    subprocess.run(["systemctl", "disable", "--now", "bluetooth"], check=True)


