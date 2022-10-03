# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calendar_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from override_classes import CalendarTableWidget
from override_classes import TaskListWidget

import tango_rc

class Ui_CalendarFormUI(object):
    def setupUi(self, CalendarFormUI):
        if not CalendarFormUI.objectName():
            CalendarFormUI.setObjectName(u"CalendarFormUI")
        CalendarFormUI.resize(790, 496)
        CalendarFormUI.setWindowTitle(u"CALENDAR")
        self.horizontalLayout = QHBoxLayout(CalendarFormUI)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.splitter = QSplitter(CalendarFormUI)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.widget_9 = QWidget(self.splitter)
        self.widget_9.setObjectName(u"widget_9")
        self.verticalLayout_5 = QVBoxLayout(self.widget_9)
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget_10 = QWidget(self.widget_9)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_5.setSpacing(2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 2)
        self.show_all_task = QCheckBox(self.widget_10)
        self.show_all_task.setObjectName(u"show_all_task")
        self.show_all_task.setChecked(True)
        self.show_all_task.setAutoExclusive(True)

        self.horizontalLayout_5.addWidget(self.show_all_task)

        self.show_selected_member_task = QCheckBox(self.widget_10)
        self.show_selected_member_task.setObjectName(u"show_selected_member_task")
        self.show_selected_member_task.setAutoExclusive(True)

        self.horizontalLayout_5.addWidget(self.show_selected_member_task)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.widget_3 = QWidget(self.widget_10)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_6.setSpacing(2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(1, 1, 1, 1)
        self.week_backward_button = QPushButton(self.widget_3)
        self.week_backward_button.setObjectName(u"week_backward_button")
        self.week_backward_button.setMaximumSize(QSize(23, 16777215))
        self.week_backward_button.setText(u"")
        icon = QIcon()
        icon.addFile(u":/tango32/resources/tango/32x32/actions/go-previous.png", QSize(), QIcon.Normal, QIcon.Off)
        self.week_backward_button.setIcon(icon)

        self.horizontalLayout_6.addWidget(self.week_backward_button)

        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_6.addWidget(self.label_2)

        self.week_index_label = QLabel(self.widget_3)
        self.week_index_label.setObjectName(u"week_index_label")
        self.week_index_label.setText(u"1")

        self.horizontalLayout_6.addWidget(self.week_index_label)

        self.week_forward_button = QPushButton(self.widget_3)
        self.week_forward_button.setObjectName(u"week_forward_button")
        self.week_forward_button.setMaximumSize(QSize(23, 16777215))
        self.week_forward_button.setText(u"")
        icon1 = QIcon()
        icon1.addFile(u":/tango32/resources/tango/32x32/actions/go-next.png", QSize(), QIcon.Normal, QIcon.Off)
        self.week_forward_button.setIcon(icon1)

        self.horizontalLayout_6.addWidget(self.week_forward_button)

        self.save_toolbutton = QToolButton(self.widget_3)
        self.save_toolbutton.setObjectName(u"save_toolbutton")
        self.save_toolbutton.setMinimumSize(QSize(36, 23))
        icon2 = QIcon()
        icon2.addFile(u":/tango32/resources/tango/32x32/actions/document-save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.save_toolbutton.setIcon(icon2)
        self.save_toolbutton.setPopupMode(QToolButton.MenuButtonPopup)
        self.save_toolbutton.setArrowType(Qt.NoArrow)

        self.horizontalLayout_6.addWidget(self.save_toolbutton)


        self.horizontalLayout_5.addWidget(self.widget_3)


        self.verticalLayout_5.addWidget(self.widget_10)

        self.tableWidget = CalendarTableWidget(self.widget_9)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QSize(499, 0))
        palette = QPalette()
        brush = QBrush(QColor(0, 211, 215, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush)
        brush1 = QBrush(QColor(0, 120, 215, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush1)
        self.tableWidget.setPalette(palette)
        self.tableWidget.setLineWidth(3)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QAbstractItemView.ContiguousSelection)
        self.tableWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setGridStyle(Qt.CustomDashLine)

        self.verticalLayout_5.addWidget(self.tableWidget)

        self.splitter.addWidget(self.widget_9)
        self.widget = QWidget(self.splitter)
        self.widget.setObjectName(u"widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.splitter_2 = QSplitter(self.widget)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Vertical)
        self.frame = QFrame(self.splitter_2)
        self.frame.setObjectName(u"frame")
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(1)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Error_widget = QWidget(self.frame)
        self.Error_widget.setObjectName(u"Error_widget")

        self.verticalLayout_2.addWidget(self.Error_widget)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.label)

        self.widget_6 = QWidget(self.frame)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy1.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy1)
        self.horizontalLayout_2 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(1, 0, 1, 0)
        self.member_combobox = QComboBox(self.widget_6)
        self.member_combobox.setObjectName(u"member_combobox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.member_combobox.sizePolicy().hasHeightForWidth())
        self.member_combobox.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.member_combobox)

        self.remove_member_button = QPushButton(self.widget_6)
        self.remove_member_button.setObjectName(u"remove_member_button")
        self.remove_member_button.setMinimumSize(QSize(23, 23))
        self.remove_member_button.setMaximumSize(QSize(23, 23))
        self.remove_member_button.setText(u"")
        icon3 = QIcon()
        icon3.addFile(u":/tango32/resources/tango/32x32/actions/list-remove.png", QSize(), QIcon.Normal, QIcon.Off)
        self.remove_member_button.setIcon(icon3)

        self.horizontalLayout_2.addWidget(self.remove_member_button)


        self.verticalLayout_2.addWidget(self.widget_6)

        self.widget_8 = QWidget(self.frame)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(1, 0, 1, 0)
        self.new_member_lineedit = QLineEdit(self.widget_8)
        self.new_member_lineedit.setObjectName(u"new_member_lineedit")

        self.horizontalLayout_4.addWidget(self.new_member_lineedit)

        self.add_member_button = QPushButton(self.widget_8)
        self.add_member_button.setObjectName(u"add_member_button")
        sizePolicy2.setHeightForWidth(self.add_member_button.sizePolicy().hasHeightForWidth())
        self.add_member_button.setSizePolicy(sizePolicy2)
        self.add_member_button.setMinimumSize(QSize(23, 0))
        self.add_member_button.setMaximumSize(QSize(23, 16777215))
        self.add_member_button.setText(u"")
        icon4 = QIcon()
        icon4.addFile(u":/tango32/resources/tango/32x32/actions/list-add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.add_member_button.setIcon(icon4)

        self.horizontalLayout_4.addWidget(self.add_member_button)


        self.verticalLayout_2.addWidget(self.widget_8)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.widget_2 = QWidget(self.frame)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy3)
        self.gridLayout_4 = QGridLayout(self.widget_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.add_task_member_button = QPushButton(self.widget_2)
        self.add_task_member_button.setObjectName(u"add_task_member_button")
        self.add_task_member_button.setEnabled(False)

        self.gridLayout_4.addWidget(self.add_task_member_button, 3, 1, 1, 1)

        self.task_name_lineedit = QLineEdit(self.widget_2)
        self.task_name_lineedit.setObjectName(u"task_name_lineedit")
        sizePolicy2.setHeightForWidth(self.task_name_lineedit.sizePolicy().hasHeightForWidth())
        self.task_name_lineedit.setSizePolicy(sizePolicy2)

        self.gridLayout_4.addWidget(self.task_name_lineedit, 0, 0, 1, 2)

        self.add_task_button = QPushButton(self.widget_2)
        self.add_task_button.setObjectName(u"add_task_button")
        self.add_task_button.setEnabled(False)

        self.gridLayout_4.addWidget(self.add_task_button, 3, 0, 1, 1)

        self.widget_7 = QWidget(self.widget_2)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy1.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy1)
        self.horizontalLayout_3 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(1, -1, 1, 1)
        self.label_5 = QLabel(self.widget_7)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_5)

        self.task_time_start = QTimeEdit(self.widget_7)
        self.task_time_start.setObjectName(u"task_time_start")
        self.task_time_start.setMaximumSize(QSize(70, 16777215))
        self.task_time_start.setMinimumTime(QTime(8, 0, 0))

        self.horizontalLayout_3.addWidget(self.task_time_start)

        self.label_4 = QLabel(self.widget_7)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.task_time_end = QTimeEdit(self.widget_7)
        self.task_time_end.setObjectName(u"task_time_end")
        sizePolicy2.setHeightForWidth(self.task_time_end.sizePolicy().hasHeightForWidth())
        self.task_time_end.setSizePolicy(sizePolicy2)
        self.task_time_end.setMaximumSize(QSize(70, 16777215))
        self.task_time_end.setMaximumTime(QTime(23, 59, 59))
        self.task_time_end.setMinimumTime(QTime(8, 0, 0))
        self.task_time_end.setTime(QTime(9, 0, 0))

        self.horizontalLayout_3.addWidget(self.task_time_end)


        self.gridLayout_4.addWidget(self.widget_7, 2, 0, 1, 2)

        self.date_combobox = QComboBox(self.widget_2)
        self.date_combobox.addItem("")
        self.date_combobox.addItem("")
        self.date_combobox.addItem("")
        self.date_combobox.addItem("")
        self.date_combobox.addItem("")
        self.date_combobox.addItem("")
        self.date_combobox.addItem("")
        self.date_combobox.setObjectName(u"date_combobox")

        self.gridLayout_4.addWidget(self.date_combobox, 1, 0, 1, 2)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.splitter_2.addWidget(self.frame)
        self.frame_2 = QFrame(self.splitter_2)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy3.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy3)
        self.frame_2.setAutoFillBackground(True)
        self.frame_2.setFrameShape(QFrame.Box)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setSpacing(1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(1, 1, 1, 1)
        self.widget_5 = QWidget(self.frame_2)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy1.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy1)
        self.gridLayout_3 = QGridLayout(self.widget_5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(1, 1, 1, 1)

        self.gridLayout.addWidget(self.widget_5, 1, 0, 1, 1)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy3.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy3)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(1, 1, 1, 1)
        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)

        self.verticalLayout_6.addWidget(self.label_3)

        self.tasks_list = TaskListWidget(self.frame_5)
        self.tasks_list.setObjectName(u"tasks_list")
        sizePolicy3.setHeightForWidth(self.tasks_list.sizePolicy().hasHeightForWidth())
        self.tasks_list.setSizePolicy(sizePolicy3)
        self.tasks_list.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tasks_list.setSelectionMode(QAbstractItemView.NoSelection)
        self.tasks_list.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.tasks_list.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.verticalLayout_6.addWidget(self.tasks_list)


        self.gridLayout.addWidget(self.frame_5, 0, 0, 1, 1)

        self.splitter_2.addWidget(self.frame_2)

        self.verticalLayout.addWidget(self.splitter_2)

        self.splitter.addWidget(self.widget)

        self.horizontalLayout.addWidget(self.splitter)


        self.retranslateUi(CalendarFormUI)

        QMetaObject.connectSlotsByName(CalendarFormUI)
    # setupUi

    def retranslateUi(self, CalendarFormUI):
        self.show_all_task.setText(QCoreApplication.translate("CalendarFormUI", u"Show all tasks", None))
        self.show_selected_member_task.setText(QCoreApplication.translate("CalendarFormUI", u"Show selected member tasks", None))
        self.label_2.setText(QCoreApplication.translate("CalendarFormUI", u"Week", None))
        self.save_toolbutton.setText("")
        self.label.setText(QCoreApplication.translate("CalendarFormUI", u"Member:", None))
        self.add_task_member_button.setText(QCoreApplication.translate("CalendarFormUI", u"ADD TASK TO MEMBER", None))
        self.add_task_button.setText(QCoreApplication.translate("CalendarFormUI", u"ADD TASK", None))
        self.label_5.setText(QCoreApplication.translate("CalendarFormUI", u"from:", None))
        self.label_4.setText(QCoreApplication.translate("CalendarFormUI", u"to:", None))
        self.date_combobox.setItemText(0, QCoreApplication.translate("CalendarFormUI", u"Monday", None))
        self.date_combobox.setItemText(1, QCoreApplication.translate("CalendarFormUI", u"Tuesday", None))
        self.date_combobox.setItemText(2, QCoreApplication.translate("CalendarFormUI", u"Wednesday", None))
        self.date_combobox.setItemText(3, QCoreApplication.translate("CalendarFormUI", u"Thursday", None))
        self.date_combobox.setItemText(4, QCoreApplication.translate("CalendarFormUI", u"Friday", None))
        self.date_combobox.setItemText(5, QCoreApplication.translate("CalendarFormUI", u"Saturday", None))
        self.date_combobox.setItemText(6, QCoreApplication.translate("CalendarFormUI", u"Sunday", None))

        self.label_3.setText(QCoreApplication.translate("CalendarFormUI", u"Taskings for this hour:", None))
        pass
    # retranslateUi

