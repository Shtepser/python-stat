# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ColumnsScatterPlotDialog.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(459, 360)
        self.plot_draw_buttons = QtWidgets.QDialogButtonBox(Dialog)
        self.plot_draw_buttons.setGeometry(QtCore.QRect(100, 320, 341, 32))
        self.plot_draw_buttons.setOrientation(QtCore.Qt.Horizontal)
        self.plot_draw_buttons.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.plot_draw_buttons.setObjectName("plot_draw_buttons")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 441, 301))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.axis_x_layout = QtWidgets.QVBoxLayout()
        self.axis_x_layout.setContentsMargins(10, 10, 10, 10)
        self.axis_x_layout.setSpacing(10)
        self.axis_x_layout.setObjectName("axis_x_layout")
        self.axis_x_column_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.axis_x_column_label.setObjectName("axis_x_column_label")
        self.axis_x_layout.addWidget(self.axis_x_column_label)
        self.axis_x_column_list = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.axis_x_column_list.setObjectName("axis_x_column_list")
        self.axis_x_layout.addWidget(self.axis_x_column_list)
        self.horizontalLayout.addLayout(self.axis_x_layout)
        self.axis_y_layout = QtWidgets.QVBoxLayout()
        self.axis_y_layout.setContentsMargins(10, 10, 10, 10)
        self.axis_y_layout.setSpacing(10)
        self.axis_y_layout.setObjectName("axis_y_layout")
        self.axis_x_column_label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.axis_x_column_label_2.setObjectName("axis_x_column_label_2")
        self.axis_y_layout.addWidget(self.axis_x_column_label_2)
        self.axis_y_column_list = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.axis_y_column_list.setObjectName("axis_y_column_list")
        self.axis_y_layout.addWidget(self.axis_y_column_list)
        self.horizontalLayout.addLayout(self.axis_y_layout)

        self.retranslateUi(Dialog)
        self.plot_draw_buttons.accepted.connect(Dialog.accept)
        self.plot_draw_buttons.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.axis_x_column_label.setText(_translate("Dialog", "Колонка для отображения по оси X"))
        self.axis_x_column_label_2.setText(_translate("Dialog", "Колонка для отображения по оси Y"))


