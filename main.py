import sys

import pyautogui

from PyQt5 import uic
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5 import QtWidgets

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtGui import QFont


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        QMainWindow.__init__(self)
        screen_size = pyautogui.size()
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint | QtCore.Qt.X11BypassWindowManagerHint)
        self.width = int(screen_size[0] * .7)
        self.height = 50
        self.font_size = self.height // 2
        self.setGeometry(screen_size[0] // 2 - self.width // 2, self.height, self.width, self.height)
        self.setStyleSheet("background-color: rgb(75, 75, 75);")
        self.label = QLabel(">", self)
        self.label.move(10, (self.height - self.font_size) // 2)
        self.label.setFont(QFont("Arial", self.font_size))
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        
        self.command = QLineEdit(self)
        self.command.move(self.font_size + 10, (self.height - self.font_size) // 2)
        self.command.setFont(QFont("Arial", self.font_size))
        self.command.setStyleSheet("color: rgb(255, 255, 255); border: none; qproperty-frame: false; QLineEdit::selected {border: none;};")
        self.command.resize(QSize(self.width - 2 * (self.font_size), self.font_size))
        self.command.returnPressed = self.returnPressed
    
    def returnPressed(self):
        data = self.command.text()
        if data == "quit" or data == "exit":
            QtWidgets.qApp.quit()
        else:
            self.command.clear()
    
    def keyPressEvent(self, event):
        if event.key() == 16777220:
            self.returnPressed()
    
    def mousePressEvent(self, event):
        QtWidgets.qApp.quit()


def start_app() -> None:
    app = QApplication(sys.argv)
    mywindow = MainWindow()
    mywindow.show()
    app.exec_()


if __name__ == '__main__':
    start_app()

