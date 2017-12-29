# -*- coding:utf-8 -*-
import sys
import time
from lsw_form import *
from PyQt4 import QtCore, QtGui

class Thread_CountDown(QtCore.QThread):
    Thread_CountDownSin = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(Thread_CountDown, self).__init__(parent)
        self.__oldtime = 0
        self.__newtime = 0
        self.__ss = 'stop'

    def run(self):
        while 1:
            self.__oldtime = time.time()
            self.__newtime = time.time()
            while self.__ss == 'start':
                self.__newtime = time.time()
                if abs(self.__newtime - self.__oldtime) >= 1:
                    #发送信号到主线程
                    self.__oldtime = self.__newtime
                    self.Thread_CountDownSin.emit()

    def start_stop(self, temstr):
            self.__ss = temstr

class MainWindow(QtGui.QWidget):
    MW2CountDownSin = QtCore.pyqtSignal(str)
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.__ui = Ui_Warn()
        self.__ui.setupUi(self)
        self.__popwarncount = 0
        self.__timecount = 0
        #创建连接
        self.connect(self.__ui.about, QtCore.SIGNAL("clicked()"), self.__click_about)
        self.connect(self.__ui.start, QtCore.SIGNAL("clicked()"), self.__click_start)
        self.connect(self.__ui.stop, QtCore.SIGNAL("clicked()"), self.__click_stop)

        #tray不可以用槽直接连接
        #self.connect(self.__ui.tray, QtCore.SIGNAL("clicked()"), self.__click_tray)
        #self.__ui.tray.activated.connect(self.__click_tray)#直接点击弹出主界面

        #创建体统托盘图标,可以看出也算是一个插件
        self.__ui.tray = QtGui.QSystemTrayIcon(self)
        trayicon = QtGui.QIcon(QtCore.QString.fromUtf8(":/img/image2.png"))
        self.__ui.tray.setIcon(trayicon)
        self.__ui.tray.setToolTip(u"Up~Down~请注意休息")
        self.__ui.tray.show()
        # 创建右击菜单
        traymenu = QtGui.QMenu()
        traymenu_reply = traymenu.addAction(u"恢复主界面")
        traymenu_exit = traymenu.addAction(u"退出")
        traymenu_reply.triggered.connect(self.__click_show)
        traymenu_exit.triggered.connect(self.__click_end)
        self.__ui.tray.setContextMenu(traymenu)

        #创建线程
        self.__thread_countdown = Thread_CountDown()
        self.__thread_countdown.Thread_CountDownSin.connect(self.__pop_warn)
        self.MW2CountDownSin.connect(self.__thread_countdown.start_stop)
        self.__thread_countdown.start()

    def __click_end(self):
        self.close()

    def __click_show(self):
        self.show()

    def __click_about(self):
        QtGui.QMessageBox.about(self, u"关于", u"Up~Down~：60分钟提醒一次\r\n"
                                             u"                                  by:lz")
    def __click_stop(self):
        self.__timecount = 0
        self.__ui.lcd.setProperty("intValue", 3600)
        self.__ui.start.setDisabled(False)
        self.MW2CountDownSin.emit('stop')

    def __click_start(self):
        self.__ui.start.setDisabled(True)
        self.MW2CountDownSin.emit('start')
        pass

    def __click_tray(self):
        self.show()

    def __pop_warn(self):
        self.__timecount += 1
        timecount = 3600 - self.__timecount
        self.__ui.lcd.setProperty("intValue", timecount)
        if timecount == 0:
            self.__timecount = 0
            self.show()
            self.__popwarncount += 1
            self.__winsta = self.isHidden()
            self.__warnbox = QtGui.QMessageBox.warning(self, u"休息", u"请休息5分钟")
            if self.__warnbox == 1024 and self.__popwarncount > 0:
                self.__popwarncount -= 1
                if self.__popwarncount == 0 and self.__winsta:
                    self.hide()


    def closeEvent(self, QCloseEvent):
        if self.isActiveWindow() == True:#是否是当前活动窗口
            self.hide()
            QCloseEvent.ignore()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp=MainWindow()

    #窗口最大化按键无效
    myapp.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)

    #锁定窗口大小
    myapp.setFixedSize(myapp.width(), myapp.height())
    myapp.show()
    app.exec_()