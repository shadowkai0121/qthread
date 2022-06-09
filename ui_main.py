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
    QListWidgetItem, QMainWindow, QMenuBar, QProgressBar,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(460, 664)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.ports_combobox = QComboBox(self.centralwidget)
        self.ports_combobox.setObjectName(u"ports_combobox")
        self.ports_combobox.setGeometry(QRect(32, 16, 225, 33))
        font = QFont()
        font.setFamilies([u"\u5fae\u8edf\u6b63\u9ed1\u9ad4"])
        font.setPointSize(16)
        self.ports_combobox.setFont(font)
        self.command_list = QListWidget(self.centralwidget)
        QListWidgetItem(self.command_list)
        QListWidgetItem(self.command_list)
        QListWidgetItem(self.command_list)
        self.command_list.setObjectName(u"command_list")
        self.command_list.setGeometry(QRect(30, 64, 225, 131))
        self.command_list.setFont(font)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(32, 208, 401, 401))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.flow_progress_bar = QProgressBar(self.layoutWidget)
        self.flow_progress_bar.setObjectName(u"flow_progress_bar")
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8edf\u6b63\u9ed1\u9ad4"])
        font1.setPointSize(12)
        self.flow_progress_bar.setFont(font1)
        self.flow_progress_bar.setValue(24)

        self.verticalLayout.addWidget(self.flow_progress_bar)

        self.log_list = QListWidget(self.layoutWidget)
        self.log_list.setObjectName(u"log_list")

        self.verticalLayout.addWidget(self.log_list)

        self.clear_button = QPushButton(self.layoutWidget)
        self.clear_button.setObjectName(u"clear_button")
        self.clear_button.setFont(font)

        self.verticalLayout.addWidget(self.clear_button)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(270, 60, 155, 130))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.home_button = QPushButton(self.layoutWidget1)
        self.home_button.setObjectName(u"home_button")
        self.home_button.setFont(font)

        self.verticalLayout_2.addWidget(self.home_button)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.move_button = QPushButton(self.layoutWidget1)
        self.move_button.setObjectName(u"move_button")
        self.move_button.setFont(font1)

        self.horizontalLayout.addWidget(self.move_button)

        self.terminate_button = QPushButton(self.layoutWidget1)
        self.terminate_button.setObjectName(u"terminate_button")
        self.terminate_button.setFont(font1)

        self.horizontalLayout.addWidget(self.terminate_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.suspend_button = QPushButton(self.layoutWidget1)
        self.suspend_button.setObjectName(u"suspend_button")
        self.suspend_button.setFont(font1)

        self.horizontalLayout_2.addWidget(self.suspend_button)

        self.continue_button = QPushButton(self.layoutWidget1)
        self.continue_button.setObjectName(u"continue_button")
        self.continue_button.setFont(font1)

        self.horizontalLayout_2.addWidget(self.continue_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.start_button = QPushButton(self.layoutWidget1)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setFont(font)

        self.verticalLayout_2.addWidget(self.start_button)

        self.layoutWidget2 = QWidget(self.centralwidget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(272, 16, 145, 32))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setSpacing(4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.open_comports_button = QPushButton(self.layoutWidget2)
        self.open_comports_button.setObjectName(u"open_comports_button")
        self.open_comports_button.setFont(font)

        self.horizontalLayout_3.addWidget(self.open_comports_button)

        self.refresh_comports_button = QPushButton(self.layoutWidget2)
        self.refresh_comports_button.setObjectName(u"refresh_comports_button")
        self.refresh_comports_button.setFont(font)

        self.horizontalLayout_3.addWidget(self.refresh_comports_button)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 460, 18))
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

        __sortingEnabled = self.command_list.isSortingEnabled()
        self.command_list.setSortingEnabled(False)
        ___qlistwidgetitem = self.command_list.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"home", None));
        ___qlistwidgetitem1 = self.command_list.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"MoveStnX	20	x	x	x	x	x	x	x	x	x	x	x	x	x	x	x", None));
        ___qlistwidgetitem2 = self.command_list.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"home", None));
        self.command_list.setSortingEnabled(__sortingEnabled)

        self.clear_button.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.home_button.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.move_button.setText(QCoreApplication.translate("MainWindow", u"Move", None))
        self.terminate_button.setText(QCoreApplication.translate("MainWindow", u"Terminate", None))
        self.suspend_button.setText(QCoreApplication.translate("MainWindow", u"Suspend", None))
        self.continue_button.setText(QCoreApplication.translate("MainWindow", u"Continue", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.open_comports_button.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.refresh_comports_button.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
    # retranslateUi
