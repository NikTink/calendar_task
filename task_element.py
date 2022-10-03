# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'task_element.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from task_element_classes import MemberMenu

import tango_rc

class Ui_TaskElement(object):
    def setupUi(self, TaskElement):
        if not TaskElement.objectName():
            TaskElement.setObjectName(u"TaskElement")
        TaskElement.resize(256, 34)
        self.verticalLayout = QVBoxLayout(TaskElement)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(1, 1, 1, 2)
        self.widget = QWidget(TaskElement)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(1, 1, 1, 2)
        self.taskname_lineedit = QLineEdit(self.widget)
        self.taskname_lineedit.setObjectName(u"taskname_lineedit")

        self.horizontalLayout.addWidget(self.taskname_lineedit)

        self.assign_new_member_button = MemberMenu(self.widget)
        self.assign_new_member_button.setObjectName(u"assign_new_member_button")
        self.assign_new_member_button.setMaximumSize(QSize(36, 23))
        icon = QIcon()
        icon.addFile(u":/tango32/resources/tango/32x32/apps/system-users.png", QSize(), QIcon.Normal, QIcon.Off)
        self.assign_new_member_button.setIcon(icon)
        self.assign_new_member_button.setPopupMode(QToolButton.MenuButtonPopup)
        self.assign_new_member_button.setArrowType(Qt.NoArrow)

        self.horizontalLayout.addWidget(self.assign_new_member_button)

        self.delete_button = QPushButton(self.widget)
        self.delete_button.setObjectName(u"delete_button")
        self.delete_button.setMaximumSize(QSize(23, 23))
        icon1 = QIcon()
        icon1.addFile(u":/tango32/resources/tango/32x32/actions/edit-delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_button.setIcon(icon1)

        self.horizontalLayout.addWidget(self.delete_button)


        self.verticalLayout.addWidget(self.widget)

        self.line = QFrame(TaskElement)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)


        self.retranslateUi(TaskElement)

        QMetaObject.connectSlotsByName(TaskElement)
    # setupUi

    def retranslateUi(self, TaskElement):
        TaskElement.setWindowTitle(QCoreApplication.translate("TaskElement", u"Form", None))
        self.assign_new_member_button.setText("")
        self.delete_button.setText("")
    # retranslateUi

