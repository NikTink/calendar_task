#This file contains override classes used to extend the funtionality of task_element.py

from PySide2 import QtCore, QtGui, QtWidgets
from help_functions import *
import random
class MemberMenu(QtWidgets.QToolButton):
    def __init__(self, *args, **kwargs):
        QtWidgets.QToolButton.__init__(self, *args, **kwargs)
        self.menu = QtWidgets.QMenu()
        self.calendar_manager = False
        self.taskname = False
        self.triggered.connect(self.action_clicked)
    def action_clicked(self, action: QtWidgets.QAction) -> None:
        name = action._member_name
        if self.calendar_manager:
            #print("color change!")
            #print(name)
            self.calendar_manager.reassign_task_week(self.taskname, name)
    def update_menu_contents(self, members: list[list[str,str]]) -> None:
        self.menu.clear()
        for member in members:
            name, color = member
            icon = get_icon_from_color(color)
            action = QtWidgets.QAction(self)
            action.setIcon(icon)
            action.setText(name)
            action._member_name = name
            self.menu.addAction(action)
        self.setMenu(self.menu)
    def set_calander_manager(self, calendar_manager) -> None:
        self.calendar_manager = calendar_manager
    def set_taskname(self, taskname:str) -> None:
        self.taskname = taskname