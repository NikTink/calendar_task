# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import flags_rc
import tango_rc

class Ui_MainUI(object):
    def setupUi(self, MainUI):
        if not MainUI.objectName():
            MainUI.setObjectName(u"MainUI")
        MainUI.resize(800, 600)
        MainUI.setWindowTitle(u"Calendar_app")
        self.actionEnglish = QAction(MainUI)
        self.actionEnglish.setObjectName(u"actionEnglish")
        self.actionEnglish.setCheckable(True)
        self.actionEnglish.setChecked(True)
        icon = QIcon()
        icon.addFile(u":/flags/resources/flags/gb.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionEnglish.setIcon(icon)
        self.actionFinnish = QAction(MainUI)
        self.actionFinnish.setObjectName(u"actionFinnish")
        self.actionFinnish.setCheckable(True)
        icon1 = QIcon()
        icon1.addFile(u":/flags/resources/flags/fi.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionFinnish.setIcon(icon1)
        self.centralwidget = QWidget(MainUI)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setIconSize(QSize(16, 20))
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
        self.main_tab = QWidget()
        self.main_tab.setObjectName(u"main_tab")
        self.gridLayout = QGridLayout(self.main_tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.new_calendar_button = QPushButton(self.main_tab)
        self.new_calendar_button.setObjectName(u"new_calendar_button")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.new_calendar_button.sizePolicy().hasHeightForWidth())
        self.new_calendar_button.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.new_calendar_button.setFont(font)
        icon2 = QIcon()
        icon2.addFile(u":/tango32/resources/tango/32x32/actions/document-new.png", QSize(), QIcon.Normal, QIcon.Off)
        self.new_calendar_button.setIcon(icon2)
        self.new_calendar_button.setIconSize(QSize(200, 200))

        self.gridLayout.addWidget(self.new_calendar_button, 0, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.main_tab)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMaximumSize(QSize(16777215, 0))

        self.gridLayout.addWidget(self.pushButton_3, 1, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.main_tab)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy1)
        self.pushButton_4.setMaximumSize(QSize(16777215, 0))

        self.gridLayout.addWidget(self.pushButton_4, 1, 1, 1, 1)

        self.open_calendar_button = QPushButton(self.main_tab)
        self.open_calendar_button.setObjectName(u"open_calendar_button")
        sizePolicy.setHeightForWidth(self.open_calendar_button.sizePolicy().hasHeightForWidth())
        self.open_calendar_button.setSizePolicy(sizePolicy)
        self.open_calendar_button.setFont(font)
        self.open_calendar_button.setLayoutDirection(Qt.LeftToRight)
        icon3 = QIcon()
        icon3.addFile(u":/tango32/resources/tango/32x32/actions/document-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.open_calendar_button.setIcon(icon3)
        self.open_calendar_button.setIconSize(QSize(200, 200))

        self.gridLayout.addWidget(self.open_calendar_button, 0, 1, 1, 1)

        self.tabWidget.addTab(self.main_tab, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(1, 2, 1, 2)
        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(1, 1, 1, 1)
        self.copyright_notice_label = QLabel(self.widget_2)
        self.copyright_notice_label.setObjectName(u"copyright_notice_label")
        self.copyright_notice_label.setEnabled(False)
        self.copyright_notice_label.setText(u"Calendar_app \u00a9 Saaga Hartikainen 2022")

        self.horizontalLayout.addWidget(self.copyright_notice_label)

        self.devenv_notice_label = QLabel(self.widget_2)
        self.devenv_notice_label.setObjectName(u"devenv_notice_label")
        self.devenv_notice_label.setLayoutDirection(Qt.LeftToRight)
        self.devenv_notice_label.setText(u"DEVENV")
        self.devenv_notice_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.devenv_notice_label)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.line_2 = QFrame(self.widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)


        self.verticalLayout.addWidget(self.widget)

        MainUI.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainUI)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menuLanguage = QMenu(self.menubar)
        self.menuLanguage.setObjectName(u"menuLanguage")
        MainUI.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainUI)
        self.statusbar.setObjectName(u"statusbar")
        MainUI.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuLanguage.menuAction())
        self.menuLanguage.addAction(self.actionEnglish)
        self.menuLanguage.addAction(self.actionFinnish)

        self.retranslateUi(MainUI)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainUI)
    # setupUi

    def retranslateUi(self, MainUI):
        self.actionEnglish.setText(QCoreApplication.translate("MainUI", u"English", None))
        self.actionFinnish.setText(QCoreApplication.translate("MainUI", u"Finnish", None))
        self.new_calendar_button.setText(QCoreApplication.translate("MainUI", u"NEW CALENDAR", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainUI", u"MANAGE CALENDARS", None))
        self.pushButton_4.setText("")
        self.open_calendar_button.setText(QCoreApplication.translate("MainUI", u"OPEN CALENDAR", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.main_tab), QCoreApplication.translate("MainUI", u"MENU", None))
        self.menuLanguage.setTitle(QCoreApplication.translate("MainUI", u"Language", None))
        pass
    # retranslateUi

