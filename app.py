#!/usr/bin/python

from __future__ import annotations

import sys
from PySide2 import QtWidgets, QtCore, QtGui


class PlayerMainWindow(QtWidgets.QMainWindow):

    def __init__(self, widget: QtWidgets.QWidget):
        super().__init__()
        self.setWindowTitle('Cloud Music Player')

        self.setCentralWidget(widget)
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu('File')

        exit_action = QtWidgets.QAction('exit', self)
        exit_action.setShortcut(QtGui.QKeySequence.Quit)
        exit_action.triggered.connect(self.close)
        self.file_menu.addAction(exit_action)

        self.status_bar = self.statusBar()
        self.status_bar.showMessage('Status')


class PlayerTrackWidget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.addWidget(TrackCoverWidget())
        self.main_layout.addWidget(TrackControlWidget())
        self.setLayout(self.main_layout)


class TrackCoverWidget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)


class TrackControlWidget(QtWidgets.QWidget):

    def __init_(self, parent=None):
        super().__init__(parent)


def main():
    app = QtWidgets.QApplication([])
    widget = PlayerMainWindow(PlayerTrackWidget())
    widget.show()
    app.exec_()


if __name__ == '__main__':
    main()

