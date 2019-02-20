# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StatMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("placeholder_img.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.source_data_widget = QtWidgets.QTableWidget(self.centralwidget)
        self.source_data_widget.setGeometry(QtCore.QRect(10, 10, 781, 531))
        self.source_data_widget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.source_data_widget.setShowGrid(True)
        self.source_data_widget.setObjectName("source_data_widget")
        self.source_data_widget.setColumnCount(0)
        self.source_data_widget.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.import_data_action = QtWidgets.QAction(MainWindow)
        self.import_data_action.setObjectName("import_data_action")
        self.export_data_action = QtWidgets.QAction(MainWindow)
        self.export_data_action.setObjectName("export_data_action")
        self.menu.addAction(self.import_data_action)
        self.menu.addAction(self.export_data_action)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Stat"))
        self.menu.setTitle(_translate("MainWindow", "Данные"))
        self.import_data_action.setText(_translate("MainWindow", "Импортировать"))
        self.export_data_action.setText(_translate("MainWindow", "Экспортировать"))


