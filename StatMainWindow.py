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
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 28))
        self.menubar.setObjectName("menubar")
        self.dataMenu = QtWidgets.QMenu(self.menubar)
        self.dataMenu.setObjectName("dataMenu")
        self.analysisMenu = QtWidgets.QMenu(self.menubar)
        self.analysisMenu.setObjectName("analysisMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.import_data_action = QtWidgets.QAction(MainWindow)
        self.import_data_action.setObjectName("import_data_action")
        self.export_data_action = QtWidgets.QAction(MainWindow)
        self.export_data_action.setObjectName("export_data_action")
        self.clusterAction = QtWidgets.QAction(MainWindow)
        self.clusterAction.setObjectName("clusterAction")
        self.dataMenu.addAction(self.import_data_action)
        self.dataMenu.addAction(self.export_data_action)
        self.analysisMenu.addAction(self.clusterAction)
        self.menubar.addAction(self.dataMenu.menuAction())
        self.menubar.addAction(self.analysisMenu.menuAction())

        self.retranslateUi(MainWindow)
        self.dataTabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Stat"))
        self.readme_browser.setHtml(_translate("MainWindow",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'Cantarell\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\">Здесь будет инструкция пользователя. Когда-нибудь.</span></p>\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\">В настоящий момент программа реализует иерархическую кластеризацию</span></p></body></html>"))
        self.dataTabs.setTabText(self.dataTabs.indexOf(self.readme_tab), _translate("MainWindow", "Стартовая страница"))
        self.dataMenu.setTitle(_translate("MainWindow", "Данные"))
        self.analysisMenu.setTitle(_translate("MainWindow", "Анализ"))
        self.import_data_action.setText(_translate("MainWindow", "Импортировать"))
        self.export_data_action.setText(_translate("MainWindow", "Экспортировать"))
        self.clusterAction.setText(_translate("MainWindow", "Кластеризовать"))
