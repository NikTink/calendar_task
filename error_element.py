# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'error_element.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import tango_rc

class Ui_ErrorElement(object):
    def setupUi(self, ErrorElement):
        if not ErrorElement.objectName():
            ErrorElement.setObjectName(u"ErrorElement")
        ErrorElement.resize(265, 50)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ErrorElement.sizePolicy().hasHeightForWidth())
        ErrorElement.setSizePolicy(sizePolicy)
        ErrorElement.setAutoFillBackground(False)
        self.verticalLayout = QVBoxLayout(ErrorElement)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(ErrorElement)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"QWidget#widget{\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 white, stop: 1 red);\n"
"border-style: solid;\n"
"border-color: grey;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(6, 4, 2, 4)
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy1)
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Error = QLabel(self.widget_2)
        self.Error.setObjectName(u"Error")
        self.Error.setStyleSheet(u"QWidget{border-width: 0px;}")

        self.verticalLayout_3.addWidget(self.Error)

        self.error_message = QComboBox(self.widget_2)
        self.error_message.addItem("")
        self.error_message.addItem("")
        self.error_message.addItem("")
        self.error_message.addItem("")
        self.error_message.addItem("")
        self.error_message.addItem("")
        self.error_message.addItem("")
        self.error_message.addItem("")
        self.error_message.addItem("")
        self.error_message.setObjectName(u"error_message")
        self.error_message.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.error_message.sizePolicy().hasHeightForWidth())
        self.error_message.setSizePolicy(sizePolicy2)
        self.error_message.setAutoFillBackground(False)
        self.error_message.setStyleSheet(u"QComboBox::down-arrow {image: url(noimg); border-width: 0px;}\n"
"QComboBox::drop-down {border-width: 0px;}\n"
"QComboBox{\n"
"	\n"
"	background-color: rgba(255, 209, 162, 0);\n"
"	border-radius: 2px;\n"
"}")
        self.error_message.setIconSize(QSize(16, 16))
        self.error_message.setFrame(False)

        self.verticalLayout_3.addWidget(self.error_message)


        self.horizontalLayout.addWidget(self.widget_2)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setPixmap(QPixmap(u":/tango32/resources/tango/32x32/emblems/emblem-important.png"))

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(ErrorElement)

        self.error_message.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(ErrorElement)
    # setupUi

    def retranslateUi(self, ErrorElement):
        ErrorElement.setWindowTitle(QCoreApplication.translate("ErrorElement", u"Error", None))
        self.Error.setText(QCoreApplication.translate("ErrorElement", u"Error", None))
        self.error_message.setItemText(0, QCoreApplication.translate("ErrorElement", u"unspecified_error", None))
        self.error_message.setItemText(1, QCoreApplication.translate("ErrorElement", u"Member already exists", None))
        self.error_message.setItemText(2, QCoreApplication.translate("ErrorElement", u"Task already exists", None))
        self.error_message.setItemText(3, QCoreApplication.translate("ErrorElement", u"Daily member-hours exceeded", None))
        self.error_message.setItemText(4, QCoreApplication.translate("ErrorElement", u"Invalid member name", None))
        self.error_message.setItemText(5, QCoreApplication.translate("ErrorElement", u"Color already exists", None))
        self.error_message.setItemText(6, QCoreApplication.translate("ErrorElement", u"Out of free colors", None))
        self.error_message.setItemText(7, QCoreApplication.translate("ErrorElement", u"No member selected", None))
        self.error_message.setItemText(8, QCoreApplication.translate("ErrorElement", u"Invalid task name", None))

        self.label.setText("")
    # retranslateUi

