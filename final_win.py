from PyQt5.QtCore import  Qt
from PyQt5.QtWidgets import QApplication, QWidget,  QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QButtonGroup
from instr import *


class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.move(win_width,win_height)
        self.resize(win_x,win_y)


    def initUI(self):
        self.hello_text = QLabel(txt_hello)
    #     self.but_next = QPushButton(txt_next)
    #     self.txt_instruction = QLabel(txt_instruction)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text,alignment = Qt.AlignLeft)
    #     self.layout.addWidget(self.txt_instruction,alignment = Qt.AlignLeft)
    #     self.layout.addWidget(self.but_next,alignment = Qt.AlignLeft)
        self.setLayout(self.layout)