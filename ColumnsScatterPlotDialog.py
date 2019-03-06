# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ColumnsScatterPlotDialog.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *


class ScatterPlotColumnsDialog(QDialog):

    def __init__(self, columns):
        super().__init__()
        self.setup_ui()

        self.params = None

        self.axis_x_column_list.addItems(columns)
        self.axis_x_column_list.setSelectionMode(QAbstractItemView.SingleSelection)
        self.axis_y_column_list.addItems(columns)
        self.axis_y_column_list.setSelectionMode(QAbstractItemView.SingleSelection)

        self.plot_draw_buttons.accepted.connect(self.save_and_close)
        self.plot_draw_buttons.rejected.connect(self.close)

    def setup_ui(self):
        self.setObjectName("ScatterPlotColumnsDialog")
        self.resize(459, 360)
        self.plot_draw_buttons = QDialogButtonBox(self)
        self.plot_draw_buttons.setGeometry(QtCore.QRect(100, 320, 341, 32))
        self.plot_draw_buttons.setOrientation(QtCore.Qt.Horizontal)
        self.plot_draw_buttons.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.plot_draw_buttons.setObjectName("plot_draw_buttons")
        self.horizontalLayoutWidget = QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 441, 301))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.axis_x_layout = QVBoxLayout()
        self.axis_x_layout.setContentsMargins(10, 10, 10, 10)
        self.axis_x_layout.setSpacing(10)
        self.axis_x_layout.setObjectName("axis_x_layout")
        self.axis_x_column_label = QLabel(self.horizontalLayoutWidget)
        self.axis_x_column_label.setObjectName("axis_x_column_label")
        self.axis_x_layout.addWidget(self.axis_x_column_label)
        self.axis_x_column_list = QListWidget(self.horizontalLayoutWidget)
        self.axis_x_column_list.setObjectName("axis_x_column_list")
        self.axis_x_layout.addWidget(self.axis_x_column_list)
        self.horizontalLayout.addLayout(self.axis_x_layout)
        self.axis_y_layout = QVBoxLayout()
        self.axis_y_layout.setContentsMargins(10, 10, 10, 10)
        self.axis_y_layout.setSpacing(10)
        self.axis_y_layout.setObjectName("axis_y_layout")
        self.axis_x_column_label_2 = QLabel(self.horizontalLayoutWidget)
        self.axis_x_column_label_2.setObjectName("axis_x_column_label_2")
        self.axis_y_layout.addWidget(self.axis_x_column_label_2)
        self.axis_y_column_list = QListWidget(self.horizontalLayoutWidget)
        self.axis_y_column_list.setObjectName("axis_y_column_list")
        self.axis_y_layout.addWidget(self.axis_y_column_list)
        self.horizontalLayout.addLayout(self.axis_y_layout)

        self.retranslate_ui()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("ScatterPlotColumnsDialog", "Выберите колонки для"))
        self.axis_x_column_label.setText(_translate("ScatterPlotColumnsDialog", "Колонка для отображения по оси X"))
        self.axis_x_column_label_2.setText(_translate("ScatterPlotColumnsDialog", "Колонка для отображения по оси Y"))

    def save_and_close(self):
        self.params = self.get_params()
        self.close()

    def get_params(self):
        if self.axis_x_column_list.selectedItems() and self.axis_y_column_list.selectedItems():
            return {
                'x_axis_column': self.axis_x_column_list.selectedItems()[0].text(),
                'y_axis_column': self.axis_y_column_list.selectedItems()[0].text()
            }
        else:
            return None

    @staticmethod
    def get_columns(columns):
        dlg = ScatterPlotColumnsDialog(columns)
        dlg.exec_()
        return dlg.params


if __name__ == "__main__":
    app = QApplication([])
    app.setApplicationName("ClustSettDial")
    cols = ScatterPlotColumnsDialog.get_columns(['Alpha', 'Beta', 'Gamma'])
    if cols:
        print(cols["x_axis_column"])
        print(cols["y_axis_column"])