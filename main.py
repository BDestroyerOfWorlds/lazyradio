import sys
import time
import wifi
import bt
from gui import gui

if len(sys.argv) > 1 and sys.argv[1] == '--legacy':
    while True:
        print("""
        lazyctl - quick and easy wifi/bluetooth control

        Commands:
            bluetooth -r    Restart bluetooth
            bluetooth -on   Turn bluetooth on
            bluetooth -off  Turn bluetooth off
            wifi -r         Restart wifi
            wifi -on        Turn wifi on
            wifi -off       Turn wifi off
            exit            exit application
        """)
        choice = input(">")

        if choice == "bluetooth -r":
            bt.bt_restart()

        elif choice == "bluetooth -on":
            bt.bt_on()

        elif choice == "bluetooth -off":
            bt.bt_off()

        elif choice == "wifi -r":
            wifi.wifi_restart()

        elif choice == "wifi -on":
            wifi.wifi_on()

        elif choice == "wifi -off":
            wifi.wifi_off()

        elif choice == "exit":
            break

        else:
            print("Invalid command")
            time.sleep(1)

elif len(sys.argv) == 1:
    gui.run_gui()

else:
    print("Invalid Argument")

