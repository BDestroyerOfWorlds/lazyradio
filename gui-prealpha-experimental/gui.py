import sys
import bt
from PySide6 import QtCore, QtWidgets, QtGui
#WORK IN PROGRESS#
class Widgets(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QtWidgets.QVBoxLayout(self)

        self.btrbtn = QtWidgets.QPushButton("Restart Bluetooth")
        self.btrbtn.clicked.connect(bt.bt_restart)
        self.layout.addWidget(self.btrbtn)

        self.btonbtn = QtWidgets.QPushButton("Turn Bluetooth On")
        self.btonbtn.clicked.connect(bt.bt_on)
        self.layout.addWidget(self.btonbtn)

        self.btofbtn = QtWidgets.QPushButton("Turn Bluetooth Off")
        self.btofbtn.clicked.connect(bt.bt_off)
        self.layout.addWidget(self.btofbtn)

#WORK IN PROGRESS#

app = QtWidgets.QApplication([])

widget = Widgets()
widget.show()

sys.exit(app.exec_())

#WORK IN PROGRESS#