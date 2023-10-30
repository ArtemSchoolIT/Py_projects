from PyQt5.QtCore import  Qt
from PyQt5.QtWidgets import QApplication, QWidget,  QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QButtonGroup, QLineEdit
from instr import *
from final_win import *


class TextWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.move(win_width,win_height)
        self.resize(win_x,win_y)

    def initUI(self):
        #Labels
        self.txt_name = QLabel(txt_name)
        self.txt_age = QLabel(txt_age)
        #self.txt_timer = QLabel(txt_timer)
        self.txt_test1 = QLabel(txt_test1)
        self.txt_test2 = QLabel(txt_test2)
        self.txt_test3 = QLabel(txt_test3)
        #PushButtons
        self.but_results = QPushButton(txt_sendresults)
        self.but_starttest1 = QPushButton(txt_starttest1)
        self.but_starttest2 = QPushButton(txt_starttest2)
        self.but_starttest3 = QPushButton(txt_starttest3)
        #LineEdits
        self.hintname = QLineEdit(txt_hintname)
        self.hintage = QLineEdit(txt_hintage)
        self.hinttest1 = QLineEdit(txt_hinttest1)
        self.hinttest2 = QLineEdit(txt_hinttest2)
        self.hinttest3 = QLineEdit(txt_hinttest3)

        self.line1y = QVBoxLayout()
        self.line2y = QVBoxLayout()
        self.linex = QHBoxLayout()
        self.line1y.addWidget(self.txt_name,alignment = Qt.AlignLeft)
        self.line1y.addWidget(self.hintname,alignment = Qt.AlignLeft)

        self.line1y.addWidget(self.txt_age,alignment = Qt.AlignLeft)
        self.line1y.addWidget(self.hintage,alignment = Qt.AlignLeft)

        self.line1y.addWidget(self.txt_test1,alignment = Qt.AlignLeft)
        self.line1y.addWidget(self.but_starttest1,alignment = Qt.AlignLeft)
        self.line1y.addWidget(self.hinttest1,alignment = Qt.AlignLeft)

        self.line1y.addWidget(self.txt_test2,alignment = Qt.AlignLeft)
        self.line1y.addWidget(self.but_starttest2,alignment = Qt.AlignLeft)
        self.line1y.addWidget(self.hinttest2,alignment = Qt.AlignLeft)

        self.line1y.addWidget(self.txt_test3,alignment = Qt.AlignLeft)
        self.line1y.addWidget(self.but_starttest3,alignment = Qt.AlignLeft)
        self.line1y.addWidget(self.hinttest3,alignment = Qt.AlignLeft)
        
        self.line1y.addWidget(self.but_results,alignment = Qt.AlignCenter)
        self.linex.addLayout(self.line1y)
        self.linex.addLayout(self.line2y)
        self.setLayout(self.linex)

    def final_click(self):
        self.fw = FinalWin()
        self.hide()

    def connects(self):
        self.but_results.clicked.connect(self.final_click)


