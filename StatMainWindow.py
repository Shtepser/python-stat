# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StatMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


def getManualPage():
    return QtCore.QUrl("man_files/index.html")


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
        self.dataTabs = QtWidgets.QTabWidget(self.centralwidget)
        self.dataTabs.setGeometry(QtCore.QRect(20, 0, 761, 531))
        self.dataTabs.setObjectName("dataTabs")
        self.readme_tab = QtWidgets.QWidget()
        self.readme_tab.setObjectName("readme_tab")
        self.readme_browser = QtWidgets.QTextBrowser(self.readme_tab)
        self.readme_browser.setGeometry(QtCore.QRect(10, 9, 721, 481))
        self.readme_browser.setMinimumSize(QtCore.QSize(200, 200))
        self.readme_browser.setObjectName("readme_browser")
        self.dataTabs.addTab(self.readme_tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.dataMenu = QtWidgets.QMenu(self.menubar)
        self.dataMenu.setObjectName("dataMenu")
        self.export_data_menu = QtWidgets.QMenu(self.dataMenu)
        self.export_data_menu.setObjectName("export_data_menu")
        self.analysisMenu = QtWidgets.QMenu(self.menubar)
        self.analysisMenu.setObjectName("analysisMenu")
        self.plots_menu = QtWidgets.QMenu(self.analysisMenu)
        self.plots_menu.setObjectName("plots_menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.import_data_action = QtWidgets.QAction(MainWindow)
        self.import_data_action.setObjectName("import_data_action")
        self.clusterAction = QtWidgets.QAction(MainWindow)
        self.clusterAction.setObjectName("clusterAction")
        self.scatterplot_action = QtWidgets.QAction(MainWindow)
        self.scatterplot_action.setObjectName("scatterplot_action")
        self.dendrogram_action = QtWidgets.QAction(MainWindow)
        self.dendrogram_action.setObjectName("dendrogram_action")
        self.export_marks_action = QtWidgets.QAction(MainWindow)
        self.export_marks_action.setObjectName("export_marks_action")
        self.export_distance_action = QtWidgets.QAction(MainWindow)
        self.export_distance_action.setObjectName("export_distance_action")
        self.export_data_menu.addAction(self.export_marks_action)
        self.export_data_menu.addAction(self.export_distance_action)
        self.dataMenu.addAction(self.import_data_action)
        self.dataMenu.addAction(self.export_data_menu.menuAction())
        self.plots_menu.addAction(self.scatterplot_action)
        self.plots_menu.addAction(self.dendrogram_action)
        self.analysisMenu.addAction(self.clusterAction)
        self.analysisMenu.addAction(self.plots_menu.menuAction())
        self.menubar.addAction(self.dataMenu.menuAction())
        self.menubar.addAction(self.analysisMenu.menuAction())

        self.retranslateUi(MainWindow)
        self.dataTabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Stat"))

        self.readme_browser.setSource(getManualPage())
        self.readme_browser.setSearchPaths(["man_files"])

        self.dataTabs.setTabText(self.dataTabs.indexOf(self.readme_tab), _translate("MainWindow", "Руководство"))
        self.dataMenu.setTitle(_translate("MainWindow", "Данные"))
        self.export_data_menu.setTitle(_translate("MainWindow", "Экспортировать"))
        self.analysisMenu.setTitle(_translate("MainWindow", "Анализ"))
        self.plots_menu.setTitle(_translate("MainWindow", "График"))
        self.import_data_action.setText(_translate("MainWindow", "Импортировать"))
        self.clusterAction.setText(_translate("MainWindow", "Кластеризовать"))
        self.scatterplot_action.setText(_translate("MainWindow", "Диаграмма рассеяния"))
        self.dendrogram_action.setText(_translate("MainWindow", "Дендрограмма"))
        self.export_marks_action.setText(_translate("MainWindow", "Таблицу с метками кластеров"))
        self.export_distance_action.setText(_translate("MainWindow", "Матрицу расстояний"))


