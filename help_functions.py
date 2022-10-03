#help functions:
from PySide2 import QtGui, QtCore, QtWidgets


def get_icon_from_color(color: str or list[int]):
    pixmap = QtGui.QPixmap(100, 100)
    if type(color) != str:
        r, g, b = color
        pixmap.fill(QtGui.QColor(r,g,b))
    else:
        pixmap.fill(QtGui.QColor(color))
    
    return QtGui.QIcon(pixmap)