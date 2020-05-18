from __future__ import annotations

from PySide2 import QtCore, QtGui


class MainWindow:
    def setup(self, main_window: QtGui.QWindow):
        main_window.setObjectName("main_window")
        main_window.setModality(QtCore.Qt.ApplicationModal)
        main_window.resize(QtCore.Qt.MaximumSize)
        main_window.