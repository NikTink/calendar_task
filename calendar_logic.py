#Ulkoiset Kirjastot: Tähän projektiin tarvitsemme PySide2-kirjaston Qt-siteeksi
from PySide2 import QtCore, QtGui, QtWidgets


from calendar_ui import Ui_CalendarFormUI
from override_classes import *

import math, random, json
from help_functions import *
    

class CalendarMember():
    def __init__(self, name:str = "Unknown", color: str or list[int] = None, tasks: dict = {}):
        self.name = name
        self.tasks = tasks
        self.color = color
    def load_data(self, data: dict) -> None:
        self.name = data["name"]
        self.tasks = data["tasks"]
        self.color = data["colors"]
    def save_data(self) -> dict:
        save_data = {
            "name": self.name,
            "color": self.color,
            "tasks": self.tasks
        }
        return save_data
    def set_color(self, color: str or list[int]) -> None:
        self.color = color
    def add_task(self, day_index:int, week_index:int, task:dict, taskname:str) -> None:
        if week_index in self.tasks:
            if day_index in self.tasks[week_index]:
                self.tasks[week_index][day_index][taskname] = task
            else:
                self.tasks[week_index][day_index] = {}
                self.add_task(day_index, week_index, task, taskname)
        else:
            self.tasks[week_index] = {}
            self.add_task(day_index, week_index, task, taskname)
    def remove_task(self, day_index:int, week_index:int, taskname:str) -> bool:
        if week_index in self.tasks:
            if day_index in self.tasks[week_index]:
                if taskname in self.tasks[week_index][day_index]:
                    del self.tasks[week_index][day_index][taskname]
                    return True
        return False
    def get_color(self):
        return self.color
    def get_member_hours(self, day_index:int, week_index:int) -> int:
        total_hours = 0
        if week_index in self.tasks:
            if day_index in self.tasks[week_index]:
                for taskname in self.tasks[week_index][day_index]:
                    task = self.tasks[week_index][day_index][taskname]
                    task_start = math.floor(task["start"])
                    task_end = math.ceil(task["end"])
                    total_hours += task_end-task_start
        return total_hours
class MemberManager():
    #hallitsee kalenterin jäseniä
    def __init__(self, parent):
        self.free_colors = ["green", "red", "blue", "yellow", "cyan", "gray", "orange", "pink"]
        self.calendar_members = {}
        self.calendar_colors = {}
        self.parent = parent
    def load_data(self, data: dict) -> None:
        self.free_colors = data["free_colors"]
        members = {}
        for member in data["calendar_members"]:
            t_member_handle = data["calendar_members"][member]
            t_member_name = t_member_handle["name"]
            t_member_color = t_member_handle["color"]
            t_member_tasks = t_member_handle["tasks"]
            t_member = CalendarMember(t_member_name, t_member_color, t_member_tasks)
            members[member] = t_member
        self.calendar_members = members
        self.calendar_colors = data["calendar_colors"]
    def save_data(self) -> dict:
        member_data = {}
        for member in self.calendar_members:
            member_data[member] = self.calendar_members[member].save_data()
        save_data = {
            "free_colors": self.free_colors,
            "calendar_members": member_data,
            "calendar_colors": self.calendar_colors
        }
        return save_data
    def get_free_colors(self) -> list:
        return self.free_colors
    def add_member(self, name:str, color:str = None) -> bool:
        if name == "":
            self.parent.error_message(ErrorWidget.INVAL_NAME)
            return False

        
        if name not in self.calendar_members:
            
            if color != None:
                
                if color not in self.calendar_colors:
                    new_member = CalendarMember(name, color)
                    self.calendar_members[name] = new_member
                    self.calendar_colors[color] = name
                    if color in self.free_colors:
                        self.free_colors.remove(color)
                    return True
                self.parent.error_message(ErrorWidget.COL_EXISTS)
                return False
            new_member = CalendarMember(name)
            self.calendar_members[name] = new_member
            return True
        self.parent.error_message(ErrorWidget.MEM_EXISTS)
        return False
    def remove_member(self, name:str) -> bool:
        if name in self.calendar_members:
            if self.get_color(name) in self.calendar_colors:
                del self.calendar_colors[self.get_color(name)]
            del self.calendar_members[name]
            return True
        return False
    def get_members(self) -> list:
        return self.calendar_members.keys()
    def set_color(self, name:str, color:str or list[int]) -> bool:
        if name in self.calendar_members:
            self.calendar_members[name].set_color(color)
            return True
        return False
    def get_color(self, name:str) -> str or list[int]:
        return self.calendar_members[name].get_color()
    def get_member_hours(self, member:str, day_index:int, week_index:int) -> int:
        if member != None:
            return self.calendar_members[member].get_member_hours(day_index, week_index)
        return 0
    def add_member_task(self, day_index:int, week_index:int, member:str, task:str, taskname:dict) -> None:
        if member != None:
            return self.calendar_members[member].add_task(day_index, week_index, task, taskname)
    def remove_member_task(self, day_index:int, week_index:int, member:str, taskname:str) -> bool:
        if member != None:
            return self.calendar_members[member].remove_task(day_index, week_index, taskname)
        return True
class TaskManager():
    def __init__(self, parent) -> None:
        self.tasks = {}
        self.parent = parent
    def load_data(self, data: dict) -> None:
        #self.tasks = data["tasks"]

        #\/ \/ \/ HOTFIX \/ \/ \/
        #This is necessary, because when saving the data to json, the integer format week index is translated to a string.
        #We must change it back.
        for week_index in data["tasks"]:
            t_week_handle = data["tasks"][week_index]
            self.tasks[int(week_index)] = t_week_handle
        # /\ /\ /\ HOTFIX /\ /\ /\

    def save_data(self) -> dict:
        save_data = {
            "tasks": self.tasks
        }
        return save_data
    def add_task_week(self, task:dict, taskname:str, week_index:int) -> bool:
        if week_index not in self.tasks.keys():
            self.tasks[week_index] = {}
        if taskname != "":
            if taskname not in self.tasks[week_index]:
                self.tasks[week_index][taskname] = task
                return True
            self.parent.error_message(ErrorWidget.TAS_EXISTS)
        self.parent.error_message(ErrorWidget.INVAL_TASK)
        return False
    def remove_task_week(self, taskname:str, week_index:int) -> bool:
        if week_index in self.tasks.keys():
            if taskname in self.tasks[week_index]:
                del self.tasks[week_index][taskname]
                return True
        return False
    def get_tasks(self) -> dict:
        return self.tasks
        return False
    def get_task_week(self, week_index:int, task:str) -> dict:
        if week_index in self.tasks:
            if task in self.tasks[week_index]:
                return self.tasks[week_index][task]
            return {}
        return {}
    def get_tasks_week(self, week_index: int) -> dict:
        #print(self.tasks)
        if week_index in self.tasks:
            return self.tasks[week_index]
        return {}
    def change_taskname_week(self, taskname: str, new_taskname:str, week_index:int) -> bool:
        if taskname in self.tasks[week_index]:
            if new_taskname not in self.tasks[week_index]:
                old_task = self.tasks[week_index][taskname]
                old_task["task_name"] = new_taskname
                self.tasks[week_index][new_taskname] = old_task
                del self.tasks[week_index][taskname]
                return True
            self.parent.error_message(ErrorWidget.TAS_EXISTS)
        return {}
    def change_color_week(self, taskname: str, color:str or list[int], week_index:int) -> bool:
        if taskname in self.tasks[week_index]:
            old_task = self.tasks[week_index][taskname]
            old_task["color"] = color
            self.tasks[week_index][taskname] = old_task
            return True
        return False
    def delete_task_week(self, taskname:str, week_index:int) -> bool:
        if week_index in self.tasks:
            if taskname in self.tasks[week_index]:
                del self.tasks[week_index][taskname]
                return True
        return False
    def reassign_task_week(self, taskname:str, member:str, week_index:int) -> bool:
        if taskname in self.tasks[week_index]:
            old_task = self.tasks[week_index][taskname]
            old_task["member"] = member
            self.tasks[week_index][taskname] = old_task
            return True
        return False
    def get_task_length(self, task:dict) -> int:
        task_start = math.floor(task["start"])
        task_end = math.ceil(task["end"])
        return task_end-task_start
class CalendarManager():
    #hallitsee kalenteria ja dataa
    task_update = QtCore.Signal()
    def __init__(self, parent, calendar_data_object:bin = False) -> None:
        if calendar_data_object:
            pass
        #alusta member-manager
        self.parent = parent
        self.member_manager = MemberManager(parent)
        self.task_manager = TaskManager(parent)
        self.week_index = 1
        self.max_hours = 8
    def load_data(self, data: dict) -> None:
        self.member_manager.load_data(data["member_manager"])
        self.task_manager.load_data(data["task_manager"])
        #self.week_index = data["week_index"] lets not do this. Always start from week 1. Less sync-issues
        self.max_hours = data["max_hours"]
    def save_data(self) -> dict:
        save_data = {
            "member_manager": self.member_manager.save_data(),
            "task_manager": self.task_manager.save_data(),
            "week_index": self.week_index,
            "max_hours": self.max_hours
        }
        return save_data
    def get_task_length(self, task:dict) -> int:
        return self.task_manager.get_task_length(task)
    def invoke_task_update(self) -> None:
        self.parent.calendar_task_update()
    def add_member(self, name:str, color:str or list[int] = False) -> bool:
        if color:
            if self.member_manager.add_member(name, color):
                return True
        if self.member_manager.add_member(name):
            return True
        return False
    def remove_member(self, name:str) -> bool:
        return self.member_manager.remove_member(name)
    def get_members(self) -> list:
        return self.member_manager.get_members()
    def add_task_week(self, task:dict, taskname:str, week_index:int) -> bool:
        task_length = self.get_task_length(task)
        day_index = task["week_day"]
        member = task["member"]
        total_hours = self.get_member_hours(member, day_index, week_index)
        if total_hours + task_length > self.max_hours and member != None:
            self.parent.error_message(ErrorWidget.HOU_EXCEED)
            return False
        if self.task_manager.add_task_week(task, taskname, week_index):
            if member != None:
                self.member_manager.add_member_task(day_index, week_index, member, task, taskname)
            return True
        return False
    def remove_task_week(self, taskname:str, week_index:int) -> bool:
        task = self.task_manager.get_task_week(week_index, taskname)
        if self.task_manager.remove_task_week(taskname, week_index):
            if len(task):
                day_index = task["week_day"]
                member = task["member"]
                if member != None:
                    self.member_manager.remove_member_task(day_index, week_index, member, taskname)
            return True
        return False
    def get_task_week(self, week_index:int, task:str) -> dict:
        return self.task_manager.get_task_week(week_index, task)
    def get_tasks_week(self, week_index:int) -> dict:
        return self.task_manager.get_tasks_week(week_index)
    def set_color_member(self, name:str, color:str or list[int]) -> bool:
        return self.member_manager.set_color(name, color)
    def get_color_member(self, name:str) -> str or list[int]:
        return self.member_manager.get_color(name)
    def get_free_colors(self) -> list:
        return self.member_manager.get_free_colors()
    def change_taskname_week(self, taskname: str, new_taskname:str, week_index:int = None) -> bool:
        if week_index == None:
            week_index = self.week_index
        return self.task_manager.change_taskname_week(taskname, new_taskname, week_index)
    def change_color_week(self, taskname:str, color:str or list[int], week_index:int = None) -> bool:
        if week_index == None:
            week_index = self.week_index
        return self.task_manager.change_color_week(taskname, color, week_index)
    def set_week_index(self, week_index:int) -> None:
        self.week_index = week_index
    def delete_task_week(self, taskname:str, week_index:int = None) -> bool:
        if week_index == None:
            week_index = self.week_index
        if self.task_manager.delete_task_week(taskname, week_index):
            self.invoke_task_update()
            return True
        return False
    def get_member_hours(self, member:str, day_index:int, week_index:int) -> int:
        return self.member_manager.get_member_hours(member, day_index, week_index)
    def reassign_task_week(self, taskname:str, member:str, week_index:int = None) -> bool:
        if week_index == None:
            week_index = self.week_index
        task = self.get_task_week(week_index, taskname)
        task_length = self.get_task_length(task)
        day_index = task["week_day"]
        old_member = task["member"]
        total_hours = self.get_member_hours(member, day_index, week_index)
        if total_hours + task_length > self.max_hours:
            self.parent.error_message(ErrorWidget.HOU_EXCEED)
            return False
        if self.task_manager.reassign_task_week(taskname, member, week_index):
            self.member_manager.remove_member_task(day_index, week_index, old_member, taskname)
            self.member_manager.add_member_task(day_index, week_index, member, task, taskname)
            color = "purple"
            if member != None:
                color = self.get_color_member(member)
            if self.change_color_week(taskname, color, week_index):
                self.invoke_task_update()
            return True
        return False

class CalendarWindow(QtWidgets.QMainWindow, Ui_CalendarFormUI):
    def __init__(self, base, main_class, open_file: str = ""):
        print("[GUI] New calendar tab initializing...")
        self.calendar_object = super().__init__()

        self.setupUi(base)

        #korjauksia:
        setattr(self.member_combobox, "allItems", lambda: [self.member_combobox.itemText(i) for i in range(self.member_combobox.count())])


        base.tab_widget = self

        #alustetaan muuttujia:
        self.ignore_table_change = False
        self.update_connection = False
        self.save_filename = ""
        
        #alusta kalenteri-manager
        self.calendar_manager = CalendarManager(self)
        if open_file != "":
            data = {}
            with open(open_file, 'r') as openfile:
                data = json.load(openfile)
            self.calendar_manager.load_data(data)

        #alusta muuttujia
        self.current_week_index = 1

        #translator:
        self.trans = QtCore.QTranslator(self)
        self.common_words = main_class.common_words
        self.translate_common_words = main_class.translate_common_words

        #kytkimet
        self.add_member_button.clicked.connect(lambda: self.add_member_button_clicked(self.new_member_lineedit.text()))
        self.remove_member_button.clicked.connect(self.remove_member_button_clicked)
        self.add_task_button.clicked.connect(self.add_task_clicked)
        self.add_task_member_button.clicked.connect(lambda: self.add_task_clicked(True))
        self.week_forward_button.clicked.connect(self.week_forward_button_clicked)
        self.week_backward_button.clicked.connect(self.week_backward_button_clicked)
        self.task_time_start.timeChanged.connect(self.validate_task_time)
        self.task_time_end.timeChanged.connect(self.validate_task_time)
        self.tableWidget.itemSelectionChanged.connect(self.table_cell_changed)
        self.show_selected_member_task.stateChanged.connect(self.update_calendar_tasks)
        self.member_combobox.currentIndexChanged.connect(self.update_calendar_tasks)
        

        #self.show()
        self.populate_save_button()
        self.populate_table()
        self.validate_task_time()
        self.update_calendar_tasks()
        print("[GUI] Calendar tab initialized")
    def save(self) -> None:
        if self.save_filename == "":
            self.save_as()
            return
        save_data = self.calendar_manager.save_data()
        with open(self.save_filename, "w") as outfile:
            json.dump(save_data, outfile, indent=4)
        
    def save_as(self) -> None:
        fileName = QtWidgets.QFileDialog.getSaveFileName(self, self.tr("Save as..."), "", self.tr("Calendar Files (*.cldr)"))
        print(fileName)
        self.save_filename = fileName[0]
        self.save()
    def populate_save_button(self) -> None:
        save_keys = QtGui.QKeySequence.Save
        save_as_keys = QtGui.QKeySequence.SaveAs
        save_shortcut = QtWidgets.QShortcut(save_keys, self)
        save_as_shortcut = QtWidgets.QShortcut(save_as_keys, self)
        menu = QtWidgets.QMenu(self)
        menu.addAction("Save", self.save, shortcut=save_keys)
        menu.addAction("Save as...", self.save_as, shortcut=save_as_keys)
        self.save_toolbutton.setMenu(menu)
    def error_message(self, message:int) -> None:
        error = ErrorWidget(self.widget_9)
        error.set_error_message(message)
    def week_forward_button_clicked(self) -> None:
        self.current_week_index += 1
        self.calendar_manager.set_week_index(self.current_week_index)
        self.week_index_label.setText(str(self.current_week_index))
        self.update_calendar_tasks()
        print("[GUI] Calendar tab initialized")
    def week_backward_button_clicked(self) -> None:
        if self.current_week_index > 0:
            self.current_week_index -= 1
            self.calendar_manager.set_week_index(self.current_week_index)
            self.week_index_label.setText(str(self.current_week_index))
            self.update_calendar_tasks()
    def table_cell_changed(self) -> None:
        if self.ignore_table_change:
            return
        self.date_combobox.setCurrentIndex(self.tableWidget.currentColumn())
        sel_items = self.tableWidget.selectedItems()
        #print(sel_items)
        if len(sel_items):
            min_time = 25
            max_time = -1
            for item in sel_items:
                row = item.row()
                #print("item, row", row)
                if row + 8 < min_time:
                    min_time = row + 8
                if row + 9 > max_time:
                    max_time = row + 9
            #print(max_time)
            #print(min_time)
            self.task_time_start.setTime(QtCore.QTime(min_time,0))
            if max_time >= 24:
                self.task_time_end.setTime(QtCore.QTime(23,59))
                return
            self.task_time_end.setTime(QtCore.QTime(max_time,0))
            self.ignore_table_change = True
            self.tableWidget.clearSelection()
            x = self.tableWidget.currentColumn()
            y = min_time-8
            y2 = max_time -9
            self.tableWidget.setRangeSelected(QtWidgets.QTableWidgetSelectionRange(y, x, y2, x), True)
            self.ignore_table_change = False
        self.update_current_hour_tasks()
    def calendar_task_update(self) -> None:
        self.update_calendar_tasks()
        self.update_current_hour_tasks()
    def update_current_hour_tasks(self) -> None:
        column = self.tableWidget.currentColumn()
        row = self.tableWidget.currentRow()
        item = self.tableWidget.item(row, column)
        tasks = item.get_tasks()
        self.tasks_list.clear_list()
        for task in tasks:
            task_object = self.calendar_manager.get_task_week(self.current_week_index, task["task_name"])
            #print(tuple(task_object))
            taskname = task_object["task_name"]
            color = task_object["color"]
            #print(color)
            member = task_object["member"]
            self.tasks_list.add_task(self.calendar_manager, taskname, color, member)
        
        self.update_member_combobox()
    def update_calendar_tasks(self) -> None:
        tasks = self.calendar_manager.get_tasks_week(self.current_week_index)
        #print(tasks)
        occupied_cells = {}
        selected_member = self.member_combobox.itemText(self.member_combobox.currentIndex())
        show_member_tasks = self.show_selected_member_task.isChecked()
        for task in tasks:
            member = tasks[task]["member"]
            if not show_member_tasks or (show_member_tasks and (member == selected_member)):
                task_start = math.floor(tasks[task]["start"])
                task_end = math.ceil(tasks[task]["end"])
                week_day = tasks[task]["week_day"]
                for i in range (task_start, task_end):
                    #print(week_day, i-8)
                    if (i-8, week_day) in occupied_cells:
                        occupied_cells[(i-8, week_day)].append(tasks[task])
                    else:
                        occupied_cells[(i-8, week_day)] = [tasks[task]]
        for y in range(0, 16):
            for x in range(0, 7):
                #print(y,x)
                item = self.tableWidget.item(y, x)
                item.reset_colors()
                item.reset_tasks()
                if (y, x) in occupied_cells:
                    for task in occupied_cells[(y,x)]:
                        color = task["color"]
                        item.add_color(color)
                        item.add_task(task)
                item.redraw_colors()
                    
                
            

    def validate_task_time(self) -> None:
        time_start = self.task_time_start.time()
        time_end = self.task_time_end.time()
        parse_time_start = time_start.hour() + time_start.minute()/100
        parse_time_end = time_end.hour() + time_end.minute()/100

        if parse_time_start >= parse_time_end:
            self.add_task_button.setEnabled(False)
            self.add_task_member_button.setEnabled(False)
        else:
            self.add_task_button.setEnabled(True)
            self.add_task_member_button.setEnabled(True)
    def add_task_clicked(self, to_member: bool = False) -> bool:
        time_start = self.task_time_start.time()
        time_end = self.task_time_end.time()
        parse_time_start = time_start.hour() + time_start.minute()/100
        parse_time_end = time_end.hour() + time_end.minute()/100

        task_name = self.task_name_lineedit.text()
        week_day = self.date_combobox.currentIndex()
        week_number = self.current_week_index
        color = "purple"
        member = None
        if to_member:
            member = self.member_combobox.itemText(self.member_combobox.currentIndex())
            color = self.member_combobox.currentData()
            if member == "":
                self.error_message(ErrorWidget.NO_MEMBSEL)
                return False
        #print(parse_time_start, parse_time_end)
        task = {
            "task_name": task_name,
            "week_day": week_day,
            "week_number": week_number,
            "color": color,
            "start": parse_time_start,
            "end": parse_time_end,
            "member": member
        }
        if self.calendar_manager.add_task_week(task, task_name, week_number):
            self.update_calendar_tasks()
            self.tableWidget.clearSelection()
            return True
        
        

        return False

    def update_member_combobox(self) ->None:
        members = self.calendar_manager.get_members()
        combo_members = self.member_combobox.allItems()
        members_colors = []
        
        for member in members:
            members_colors.append([member, self.calendar_manager.get_color_member(member)])
            if member not in combo_members:
                color = self.calendar_manager.get_color_member(member)
                self.member_combobox.addItem(get_icon_from_color(color), member, userData = color)

        members_colors.append([None, "purple"])
        for element in self.tasks_list.get_elements():
            element.update_menu_contents(members_colors)

        for member in combo_members:
            if member not in members:
                self.member_combobox.removeItem(self.member_combobox.findText(member))

    def add_member_button_clicked(self, name:str) -> bool:
        free_colors = self.calendar_manager.get_free_colors()
        if len(free_colors):
            color = random.choice(free_colors)
            if self.calendar_manager.add_member(name, color):
                self.update_member_combobox()
                return True
            else:
                return False
        self.error_message(ErrorWidget.OUT_COLORS)
        return False
    def remove_member_button_clicked(self) -> bool:
        name = self.member_combobox.itemText(self.member_combobox.currentIndex())
        if self.calendar_manager.remove_member(name):
            self.update_member_combobox()
            return True
        return False

    def translate(self, language:str) -> None:
        if language != "":
            week_days = self.translate_common_words("week_days", "eng-fi")
            self.tableWidget.setHorizontalHeaderLabels(week_days)
        else:
            week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            self.tableWidget.setHorizontalHeaderLabels(week_days)
    def populate_table(self) -> None:
        default_times = tuple(range(0,17))
        data = {'Monday':default_times,
        'Tuesday':default_times,
        'Wednesday':default_times,
        'Thursday':default_times,
        'Friday':default_times,
        'Saturday':default_times,
        'Sunday':default_times
        }

        week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.tableWidget.setRowCount(16)
        self.tableWidget.setColumnCount(len(data))
        for n, key in enumerate(sorted(data.keys())):
            for m, item in enumerate(data[key]):
                newitem = CalendarHourObject(item)
                newitem.set_parent(self.tableWidget)
                newitem.redraw_colors()
                self.tableWidget.setItem(m, n, newitem)
        #print(week_days)
        self.tableWidget.setHorizontalHeaderLabels(week_days)
        header_object = self.tableWidget.horizontalHeader()
        for i in range(0, len(week_days)):
            header_object.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        
        times = [
            "8.00 - 9.00",
            "9.00 - 10.00",
            "10.00 - 11.00",
            "11.00 - 12.00",
            "12.00 - 13.00",
            "13.00 - 14.00",
            "14.00 - 15.00",
            "15.00 - 16.00",
            "16.00 - 17.00",
            "17.00 - 18.00",
            "18.00 - 19.00",
            "19.00 - 20.00",
            "20.00 - 21.00",
            "21.00 - 22.00",
            "22.00 - 23.00",
            "23.00 - 24.00"
        ]

        self.tableWidget.setVerticalHeaderLabels(times)
        header_object = self.tableWidget.verticalHeader()
        for i in range(0, len(times)):
            header_object.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        #self.tableWidget.resizeColumnsToContents()
        #self.tableWidget.resizeRowsToContents()

