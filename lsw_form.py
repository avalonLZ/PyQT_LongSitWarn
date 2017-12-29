# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lsw.ui'
#
# Created: Mon Nov 06 22:34:40 2017
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Warn(object):
    def setupUi(self, Warn):
        Warn.setObjectName(_fromUtf8("Warn"))
        Warn.resize(224, 73)
        Warn.setMinimumSize(QtCore.QSize(224, 64))
        Warn.setSizeIncrement(QtCore.QSize(224, 64))
        Warn.setBaseSize(QtCore.QSize(224, 64))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/img/image2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Warn.setWindowIcon(icon)
        self.start = QtGui.QPushButton(Warn)
        self.start.setGeometry(QtCore.QRect(0, 50, 81, 23))
        self.start.setObjectName(_fromUtf8("start"))
        self.stop = QtGui.QPushButton(Warn)
        self.stop.setGeometry(QtCore.QRect(90, 50, 81, 23))
        self.stop.setObjectName(_fromUtf8("stop"))
        self.about = QtGui.QPushButton(Warn)
        self.about.setGeometry(QtCore.QRect(180, 50, 41, 23))
        self.about.setObjectName(_fromUtf8("about"))
        self.label = QtGui.QLabel(Warn)
        self.label.setGeometry(QtCore.QRect(80, 40, 31, 16))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.lcd = QtGui.QLCDNumber(Warn)
        self.lcd.setGeometry(QtCore.QRect(70, 10, 91, 31))
        self.lcd.setSmallDecimalPoint(False)
        self.lcd.setNumDigits(4)
        self.lcd.setMode(QtGui.QLCDNumber.Dec)
        self.lcd.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcd.setProperty("intValue", 3600)
        self.lcd.setObjectName(_fromUtf8("lcd"))

        self.retranslateUi(Warn)
        QtCore.QMetaObject.connectSlotsByName(Warn)
        Warn.setTabOrder(self.about, self.start)
        Warn.setTabOrder(self.start, self.stop)

    def retranslateUi(self, Warn):
        Warn.setWindowTitle(_translate("Warn", "Up~Down~", None))
        self.start.setText(_translate("Warn", "Start", None))
        self.stop.setText(_translate("Warn", "Stop", None))
        self.about.setText(_translate("Warn", "About", None))

import lst_rc
