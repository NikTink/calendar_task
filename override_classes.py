#This file contains override classes used to extend the funtionality of standard QtWidgets

from PySide2 import QtCore, QtGui, QtWidgets, QtMultimedia


from task_element import Ui_TaskElement
from error_element import Ui_ErrorElement



#hotfix for QT-bug
class ErrorWidget(QtWidgets.QWidget, Ui_ErrorElement):
    MEM_EXISTS = 1
    TAS_EXISTS = 2
    HOU_EXCEED = 3
    INVAL_NAME = 4
    COL_EXISTS = 5
    OUT_COLORS = 6
    NO_MEMBSEL = 7
    INVAL_TASK = 8
    def __init__(self, *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.trans = QtCore.QTranslator(self)
        margin = 14
        parent = args[0]
        self.play_sound()
        op = QtWidgets.QGraphicsOpacityEffect(self)
        op.setOpacity(1) #0 to 1 will cause the fade effect to kick in
        self.setGraphicsEffect(op)
        self.setAutoFillBackground(True)
        self.animation = QtCore.QPropertyAnimation(op, b"opacity")
        self.animation.setDuration(5000)
        self.animation.setStartValue(1)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InBounce)
        self.animation.setEndValue(0)
        self.animation.start(QtCore.QPropertyAnimation.DeleteWhenStopped)
        self.animation.finished.connect(lambda: self.delete_self())
        self.show()
        self.move(0 + margin,parent.height() - self.height() - margin)
        self.window().translatable_bases.append(self)
    def translate(self, language) -> None:
        pass
    def delete_self(self) -> None:
        self.window().translatable_bases.remove(self)
        self.deleteLater()
    def set_error_message(self, message:int) -> None:
        self.error_message.setCurrentIndex(message)
        return
    def play_sound(self):
        filepath = "C:\Windows\Media\Windows Ding.wav"
        global sound
        sound = QtMultimedia.QSoundEffect()
        sound.setSource(QtCore.QUrl.fromLocalFile(filepath))
        sound.play()
class BackgroundDelegate(QtWidgets.QStyledItemDelegate):
    def paint(self, qp, opt, index):
        #print(index.data(QtCore.Qt.BackgroundRole))
        #print(index.data)
        if index.data(QtCore.Qt.BackgroundRole):
            obj = self.parent.item(index.row(), index.column())
            print(opt.rect)
            
            print(index.data(QtCore.Qt.BackgroundRole).gradient())
            new_rect = opt.rect - QtCore.QMargins(4,4,4,4)
            print(new_rect)
            gradient = index.data(QtCore.Qt.BackgroundRole).gradient()
            print(gradient)
            print(obj.brush)
            print(index.parent())
            qp.fillRect(new_rect, obj.gradient)
        super().paint(qp, opt, index)

class CalendarTableWidget(QtWidgets.QTableWidget):
    def __init__(self, *args, **kwargs):
        QtWidgets.QTableWidget.__init__(self, *args, **kwargs)
        #self.delegate = BackgroundDelegate(self)
        #self.setItemDelegate(self.delegate)
        #self.delegate.parent = self
    def paintEvent(self, e: QtGui.QPaintEvent) -> None:
        for i in range(self.rowCount()):
            for j in range(self.columnCount()):
                item = self.item(i, j)
                item.redraw_colors()
        return super().paintEvent(e)

class TaskListWidget(QtWidgets.QListWidget):
    def __init__(self, *args, **kwargs):
        QtWidgets.QListWidget.__init__(self, *args, **kwargs)
        self.task_elements = []
    def clear_list(self) -> None:
        self.task_elements = []
        self.clear()
    def add_task(self, calendar_manager, taskname:str, color:str or list[int], member:str) -> bool:
        new_item = TaskListElement(self, calendar_manager)
        new_item.set_taskname(taskname)
        new_item.set_color(color)
        new_item.set_member(member)
        self.task_elements.append(new_item)
    def get_elements(self) -> list:
        return self.task_elements
class TaskListElement(QtWidgets.QListWidgetItem, Ui_TaskElement):
    def __init__(self, lst: TaskListWidget, calendar_manager):
        super(TaskListElement, self).__init__()
        self.setSizeHint(QtCore.QSize(1, 30))
        lst.addItem(self)
        self.index = lst.row(self)
        widget = QtWidgets.QWidget(lst)
        self.setupUi(widget)
        self.lst = lst
        self.calendar_manager = calendar_manager

        self.color = None
        self.member = None
        self.taskname = None
        self.ignore_changes = False

        lst.setItemWidget(self, widget)
        self.taskname_lineedit.editingFinished.connect(lambda: self.taskname_issued())
        self.assign_new_member_button.set_calander_manager(self.calendar_manager)
        self.delete_button.clicked.connect(lambda: self.delete_task())
    def delete_task(self) -> None:
        self.calendar_manager.delete_task_week(self.taskname)
    def update_menu_contents(self, members:list[str]) -> None:
        #print("self_color", [self.member, self.color])
        new_members = members.copy()
        if [self.member, self.color] in members:
            new_members.remove([self.member, self.color])
        self.assign_new_member_button.update_menu_contents(new_members)
    def set_taskname(self, taskname:str) -> None:
        self.taskname = taskname
        self.taskname_lineedit.setText(taskname)
        self.assign_new_member_button.set_taskname(self.taskname)
    def set_color(self, color:str or list[int]) -> None:
        self.color = color
        if type(color) != str:
            r, g, b = color
            self.setBackground(QtGui.QColor(r,g,b))
        else:
            self.setBackground(QtGui.QColor(color))
    def set_member(self, member:str) -> None:
        self.member = member
    def get_taskname(self) -> str:
        return self.taskname
    def taskname_issued(self) -> None:
        if not self.ignore_changes:
            new_taskname = self.taskname_lineedit.text()
            if new_taskname != self.taskname:
                if self.calendar_manager.change_taskname_week(self.taskname, new_taskname):
                    self.ignore_changes = True
                    self.taskname_lineedit.setText(new_taskname)
                    self.taskname = new_taskname
                    self.ignore_changes = False
                    return
                else:
                    self.ignore_changes = True
                    self.taskname_lineedit.setText(self.taskname)
                    self.ignore_changes = False
                    return
        return

            

class CalendarHourObject(QtWidgets.QTableWidgetItem):
    def __init__(self, *args, **kwargs):
        QtWidgets.QTableWidgetItem.__init__(self, *args, **kwargs)
        self.colors = []
        self.tasks = []
        self.parent = None
        self.brush = None
        self.gradient = None
        self.redraw_colors()
    def get_tasks(self) -> list:
        return self.tasks
    def set_colors(self, colors:list[list[int] or str] = []) -> None:
        if len(colors):
            self.colors = colors
        self.redraw_colors()
    def reset_colors(self) -> None:
        self.colors = []
    def reset_tasks(self) -> None:
        self.tasks = []
    def add_task(self, task:str) -> None:
        self.tasks.append(task)
    def add_color(self, color:list[int] or str) -> None:
        if color not in self.colors:
            self.colors.append(color)
    def redraw_colors(self) -> None:
        #parse colors:
        if self.parent != None and self.colors != []:
            # here we ⎓╎リ↸ 𝙹⚍ℸ ̣  ℸ ̣ ⍑ᒷ ᓭℸ ̣ ᔑ∷ℸ ̣ ᓭ ᔑリ↸ ᓭℸ ̣ 𝙹!¡ᓭ 𝙹⎓ ᒷᔑᓵ⍑ ᓭᒷ⊣ᒲᒷリℸ ̣  𝙹⎓ ℸ ̣ ⍑ᒷ ⊣∷ᔑ↸╎ᒷリℸ ̣
            starts = list(map(lambda x: (1/len(self.colors)) * self.colors.index(x), self.colors))
            stops = list(map(lambda x: (1/len(self.colors)) * (self.colors.index(x)+1), self.colors))

            self.rect = self.parent.visualItemRect(self)

            gradient = QtGui.QLinearGradient(0, 0, self.rect.width(), 0)
            
            for i, color in enumerate(self.colors):
                if type(color) != str:
                    r, g, b = color
                    gradient.setColorAt(starts[i], QtGui.QColor(r,g,b))
                    gradient.setColorAt(stops[i]-0.01, QtGui.QColor(r,g,b))
                    #print(starts[i], stops[i])
                else:
                    gradient.setColorAt(starts[i], QtGui.QColor(color))
                    gradient.setColorAt(stops[i]-0.01, QtGui.QColor(color))
                    #print(starts[i], stops[i])

            #painter.fillRect(self.rect(), gradient)
            brush = QtGui.QBrush(gradient)
            self.setBackground(brush)
            self.gradient = gradient
            self.brush = brush
            #print(brush)
            #print(self.rect.height())
        else:
            self.setBackground(QtGui.QBrush())
    def paintEvent(self, event):
        self.redraw_colors()
    def set_parent(self, parent:QtWidgets.QTableWidget) -> None:
        if self.parent == None:
            self.parent = parent