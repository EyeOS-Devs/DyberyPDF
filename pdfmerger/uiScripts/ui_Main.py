# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QListView, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        self.actionAbout_DyberyPDF_Merger = QAction(MainWindow)
        self.actionAbout_DyberyPDF_Merger.setObjectName(u"actionAbout_DyberyPDF_Merger")
        self.actionAbout_Qt = QAction(MainWindow)
        self.actionAbout_Qt.setObjectName(u"actionAbout_Qt")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 781, 531))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.removeFileBtn = QPushButton(self.gridLayoutWidget)
        self.removeFileBtn.setObjectName(u"removeFileBtn")

        self.gridLayout.addWidget(self.removeFileBtn, 1, 1, 1, 1)

        self.addFileBtn = QPushButton(self.gridLayoutWidget)
        self.addFileBtn.setObjectName(u"addFileBtn")

        self.gridLayout.addWidget(self.addFileBtn, 1, 0, 1, 1)

        self.mergeBtn = QPushButton(self.gridLayoutWidget)
        self.mergeBtn.setObjectName(u"mergeBtn")

        self.gridLayout.addWidget(self.mergeBtn, 1, 2, 1, 1)

        self.pdfList = QListView(self.gridLayoutWidget)
        self.pdfList.setObjectName(u"pdfList")

        self.gridLayout.addWidget(self.pdfList, 0, 0, 1, 3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuMore_stuff = QMenu(self.menubar)
        self.menuMore_stuff.setObjectName(u"menuMore_stuff")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMore_stuff.menuAction())
        self.menuMore_stuff.addAction(self.actionClose)
        self.menuMore_stuff.addAction(self.actionAbout_DyberyPDF_Merger)
        self.menuMore_stuff.addAction(self.actionAbout_Qt)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"DyberyPDF Merger", None))
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.actionAbout_DyberyPDF_Merger.setText(QCoreApplication.translate("MainWindow", u"About DyberyPDF Merger", None))
        self.actionAbout_Qt.setText(QCoreApplication.translate("MainWindow", u"About Qt", None))
        self.removeFileBtn.setText(QCoreApplication.translate("MainWindow", u"Remove selected file", None))
        self.addFileBtn.setText(QCoreApplication.translate("MainWindow", u"Add files", None))
        self.mergeBtn.setText(QCoreApplication.translate("MainWindow", u"Merge files into one", None))
        self.menuMore_stuff.setTitle(QCoreApplication.translate("MainWindow", u"More stuff", None))
    # retranslateUi

