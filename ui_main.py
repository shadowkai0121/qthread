# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QListWidget,
    QListWidgetItem, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(459, 716)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.ports_combobox = QComboBox(self.centralwidget)
        self.ports_combobox.setObjectName(u"ports_combobox")
        self.ports_combobox.setGeometry(QRect(30, 20, 121, 22))
        self.start_button = QPushButton(self.centralwidget)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setGeometry(QRect(270, 170, 61, 24))
        self.log_list = QListWidget(self.centralwidget)
        self.log_list.setObjectName(u"log_list")
        self.log_list.setGeometry(QRect(30, 210, 401, 401))
        self.command_list = QListWidget(self.centralwidget)
        QListWidgetItem(self.command_list)
        QListWidgetItem(self.command_list)
        QListWidgetItem(self.command_list)
        self.command_list.setObjectName(u"command_list")
        self.command_list.setGeometry(QRect(30, 60, 201, 131))
        self.refresh_comports_button = QPushButton(self.centralwidget)
        self.refresh_comports_button.setObjectName(u"refresh_comports_button")
        self.refresh_comports_button.setGeometry(QRect(230, 20, 61, 24))
        self.open_comports_button = QPushButton(self.centralwidget)
        self.open_comports_button.setObjectName(u"open_comports_button")
        self.open_comports_button.setGeometry(QRect(160, 20, 61, 24))
        self.home_button = QPushButton(self.centralwidget)
        self.home_button.setObjectName(u"home_button")
        self.home_button.setGeometry(QRect(270, 60, 61, 24))
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(270, 100, 160, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.move_button = QPushButton(self.horizontalLayoutWidget)
        self.move_button.setObjectName(u"move_button")

        self.horizontalLayout.addWidget(self.move_button)

        self.terminate_button = QPushButton(self.horizontalLayoutWidget)
        self.terminate_button.setObjectName(u"terminate_button")

        self.horizontalLayout.addWidget(self.terminate_button)

        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(270, 140, 160, 31))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.suspend_button = QPushButton(self.horizontalLayoutWidget_2)
        self.suspend_button.setObjectName(u"suspend_button")

        self.horizontalLayout_2.addWidget(self.suspend_button)

        self.continue_button = QPushButton(self.horizontalLayoutWidget_2)
        self.continue_button.setObjectName(u"continue_button")

        self.horizontalLayout_2.addWidget(self.continue_button)

        self.clear_button = QPushButton(self.centralwidget)
        self.clear_button.setObjectName(u"clear_button")
        self.clear_button.setGeometry(QRect(40, 620, 381, 41))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 459, 18))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.clear_button.released.connect(self.log_list.clear)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"Start", None))

        __sortingEnabled = self.command_list.isSortingEnabled()
        self.command_list.setSortingEnabled(False)
        ___qlistwidgetitem = self.command_list.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"home", None));
        ___qlistwidgetitem1 = self.command_list.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"MoveStnX	20	x	x	x	x	x	x	x	x	x	x	x	x	x	x	x", None));
        ___qlistwidgetitem2 = self.command_list.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"home", None));
        self.command_list.setSortingEnabled(__sortingEnabled)

        self.refresh_comports_button.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.open_comports_button.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.home_button.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.move_button.setText(QCoreApplication.translate("MainWindow", u"Move", None))
        self.terminate_button.setText(QCoreApplication.translate("MainWindow", u"Terminate", None))
        self.suspend_button.setText(QCoreApplication.translate("MainWindow", u"Suspend", None))
        self.continue_button.setText(QCoreApplication.translate("MainWindow", u"Continue", None))
        self.clear_button.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
    # retranslateUi

