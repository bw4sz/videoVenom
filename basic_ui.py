# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/basic.ui'
#
# Created: Fri May 13 19:41:55 2016
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(792, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.videoPlayer = phonon.Phonon.VideoPlayer(self.centralwidget)
        self.videoPlayer.setGeometry(QtCore.QRect(281, 11, 439, 281))
        self.videoPlayer.setStyleSheet(_fromUtf8("background-color: rgba(0, 0, 0, 100)"))
        self.videoPlayer.setObjectName(_fromUtf8("videoPlayer"))
        self.seekSlider = phonon.Phonon.SeekSlider(self.centralwidget)
        self.seekSlider.setGeometry(QtCore.QRect(280, 330, 441, 20))
        self.seekSlider.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0)"))
        self.seekSlider.setObjectName(_fromUtf8("seekSlider"))
        self.volumeSlider = phonon.Phonon.VolumeSlider(self.centralwidget)
        self.volumeSlider.setGeometry(QtCore.QRect(610, 300, 109, 21))
        self.volumeSlider.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0)"))
        self.volumeSlider.setObjectName(_fromUtf8("volumeSlider"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(290, 350, 401, 101))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.playButton = QtGui.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.playButton.setFont(font)
        self.playButton.setObjectName(_fromUtf8("playButton"))
        self.horizontalLayout.addWidget(self.playButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pauseButton = QtGui.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.pauseButton.setFont(font)
        self.pauseButton.setObjectName(_fromUtf8("pauseButton"))
        self.horizontalLayout.addWidget(self.pauseButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.stopButton = QtGui.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.stopButton.setFont(font)
        self.stopButton.setObjectName(_fromUtf8("stopButton"))
        self.horizontalLayout.addWidget(self.stopButton)
        self.bannerBox = QtGui.QGroupBox(self.centralwidget)
        self.bannerBox.setGeometry(QtCore.QRect(30, 110, 191, 231))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        self.bannerBox.setFont(font)
        self.bannerBox.setObjectName(_fromUtf8("bannerBox"))
        self.endTimeWidget = QtGui.QTimeEdit(self.bannerBox)
        self.endTimeWidget.setGeometry(QtCore.QRect(10, 130, 121, 21))
        self.endTimeWidget.setObjectName(_fromUtf8("endTimeWidget"))
        self.startTimeLabel = QtGui.QLabel(self.bannerBox)
        self.startTimeLabel.setGeometry(QtCore.QRect(10, 50, 71, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.startTimeLabel.setFont(font)
        self.startTimeLabel.setObjectName(_fromUtf8("startTimeLabel"))
        self.startTimeWidget = QtGui.QTimeEdit(self.bannerBox)
        self.startTimeWidget.setGeometry(QtCore.QRect(10, 70, 121, 21))
        self.startTimeWidget.setObjectName(_fromUtf8("startTimeWidget"))
        self.startTimeLabel_2 = QtGui.QLabel(self.bannerBox)
        self.startTimeLabel_2.setGeometry(QtCore.QRect(10, 110, 61, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.startTimeLabel_2.setFont(font)
        self.startTimeLabel_2.setObjectName(_fromUtf8("startTimeLabel_2"))
        self.progressBox = QtGui.QGroupBox(self.centralwidget)
        self.progressBox.setGeometry(QtCore.QRect(10, 300, 251, 231))
        self.progressBox.setTitle(_fromUtf8(""))
        self.progressBox.setObjectName(_fromUtf8("progressBox"))
        self.nextLabel = QtGui.QLabel(self.progressBox)
        self.nextLabel.setGeometry(QtCore.QRect(10, 140, 81, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.nextLabel.setFont(font)
        self.nextLabel.setAutoFillBackground(False)
        self.nextLabel.setObjectName(_fromUtf8("nextLabel"))
        self.nextBtn = QtGui.QPushButton(self.progressBox)
        self.nextBtn.setGeometry(QtCore.QRect(10, 170, 141, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.nextBtn.setFont(font)
        self.nextBtn.setObjectName(_fromUtf8("nextBtn"))
        self.logoLabel = QtGui.QLabel(self.centralwidget)
        self.logoLabel.setGeometry(QtCore.QRect(10, 20, 241, 241))
        font = QtGui.QFont()
        font.setPointSize(4)
        self.logoLabel.setFont(font)
        self.logoLabel.setAutoFillBackground(False)
        self.logoLabel.setStyleSheet(_fromUtf8(""))
        self.logoLabel.setObjectName(_fromUtf8("logoLabel"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Video Venom", None))
        self.playButton.setText(_translate("MainWindow", "Play/Open", None))
        self.pauseButton.setText(_translate("MainWindow", "Pause", None))
        self.stopButton.setText(_translate("MainWindow", "Stop", None))
        self.bannerBox.setTitle(_translate("MainWindow", "Banner timing", None))
        self.endTimeWidget.setDisplayFormat(_translate("MainWindow", "h:mm:ss", None))
        self.startTimeLabel.setText(_translate("MainWindow", "Start Time", None))
        self.startTimeWidget.setDisplayFormat(_translate("MainWindow", "h:mm:ss", None))
        self.startTimeLabel_2.setText(_translate("MainWindow", "End Time", None))
        self.nextLabel.setText(_translate("MainWindow", "Step 1/5", None))
        self.nextBtn.setText(_translate("MainWindow", "Select a banner", None))
        self.logoLabel.setText(_translate("MainWindow", "Video Venom logo", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))

from PyQt4 import phonon

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

