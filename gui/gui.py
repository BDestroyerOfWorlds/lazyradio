import sys
import bt
import wifi

from PySide6 import QtWidgets
from PySide6.QtGui import QIcon

class Widgets(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("lazyradio")
        self.setWindowIcon(QIcon("gui/icon.png"))

        self.main_layout = QtWidgets.QHBoxLayout(self)
        bt_layout = QtWidgets.QVBoxLayout()
        wifi_layout = QtWidgets.QVBoxLayout()

        self.main_layout.addLayout(bt_layout)
        self.main_layout.addLayout(wifi_layout)


        self.btrbtn = QtWidgets.QPushButton("Restart Bluetooth")
        self.btrbtn.clicked.connect(bt.bt_restart)
        bt_layout.addWidget(self.btrbtn)

        self.btonbtn = QtWidgets.QPushButton("Turn Bluetooth On")
        self.btonbtn.clicked.connect(bt.bt_on)
        bt_layout.addWidget(self.btonbtn)

        self.btofbtn = QtWidgets.QPushButton("Turn Bluetooth Off")
        self.btofbtn.clicked.connect(bt.bt_off)
        bt_layout.addWidget(self.btofbtn)




        self.wifirbtn = QtWidgets.QPushButton("Restart Wifi")
        self.wifirbtn.clicked.connect(wifi.wifi_restart)
        wifi_layout.addWidget(self.wifirbtn)

        self.wifionbtn = QtWidgets.QPushButton("Turn Wi-Fi On")
        self.wifionbtn.clicked.connect(wifi.wifi_on)
        wifi_layout.addWidget(self.wifionbtn)

        self.wifioffbtn = QtWidgets.QPushButton("Turn Wi-Fi Off")
        self.wifioffbtn.clicked.connect(wifi.wifi_off)
        wifi_layout.addWidget(self.wifioffbtn)




def run_gui():
    app = QtWidgets.QApplication([])

    widget = Widgets()
    widget.show()

    sys.exit(app.exec())



