#!/usr/bin/python3
#-*- coding: utf-8 -*-
"""
Welcomescreen for Revolution Os by Simon Helmut Erich Kirsch
"""
import sys
import webbrowser
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDesktopWidget, QLabel,QCheckBox

from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import QCoreApplication, QSize

class window(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.pic(0, 0, 'background.jpg')
        self.lbl2()
        self.qtbn()
        self.lbl3()
        self.chbx()
        self.pic(0, 0, 'banner.png')
        self.pic(400, 0, 'Crown.png')
        self.qbn('website.png', 50, 300, ' Website', 'http://google.com')
        self.qbn('features.png', 200, 300, ' Features', 'http://google.com')
        self.qbn('help.png', 350, 300, '    Help', 'http://google.com')
        self.qbn('involve.png', 50, 500, 'Get Involved', 'http://google.com')
        self.qbn('donate.png', 200, 500, '  Donate', 'http://google.com')
        self.qbn('bugs.png', 350, 500, 'Report Bugs', 'http://google.com')

        self.setFixedSize(1000, 700)
        self.center()

        self.setWindowTitle('                 Welcome')
        self.setWindowIcon(QIcon('icon.png'))

        self.show()

    def pic(self, x, y, p):
        lbl1 = QLabel(self)
        lbl1.setPixmap(QPixmap(p))
        lbl1.move(x, y)

    def lbl2(self):
        font = QFont()
        font.setFamily("Quicksand")
        font.setBold(True)
        font.setPointSize(19)
        lbl2 = QLabel('Welcome to Revolution OS, under this text you find usefull Links  to get started.',self)
        lbl2.setFont(font)
        lbl2.setStyleSheet("QLabel { color : white; }")
        lbl2.move(15, 200)

    def lbl3(self):
        font = QFont()
        font.setFamily("Quicksand")
        font.setBold(True)
        font.setPointSize(15)
        lbl3 = QLabel('Don\'t show this at start up' ,self)
        lbl3.setFont(font)
        lbl3.setStyleSheet("QLabel { color : white; }")
        lbl3.move(580, 650)

    def chbx(self):
        chbx = QCheckBox(self)
        chbx.move(850, 655)
        chbx.clicked.connect(QCoreApplication.instance().quit)

    def qtbn(self):
        qtbn = QPushButton('Quit', self)
        qtbn.clicked.connect(QCoreApplication.instance().quit)
        qtbn.resize(qtbn.sizeHint())
        qtbn.move(900, 650)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def qbn(self, s, x, y, l, u):
        qbn = QPushButton(self)
        qbn.setIcon(QIcon(s))
        qbn.setIconSize(QSize(100, 100))
        qbn.resize(100, 100)
        qbn.move(x, y)
        font = QFont()
        font.setFamily("Quicksand")
        font.setBold(True)
        font.setPointSize(15)
        lbl = QLabel(l, self)
        lbl.setFont(font)
        lbl.setStyleSheet("QLabel { color : white; }")
        lbl.move(x, (y + 110))
        def web(self):
            webbrowser.open_new(u)
        qbn.clicked.connect(web)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    w = window()
    sys.exit(app.exec_())


