from PyQt5 import QtWidgets, QtCore

import analytic
from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import *
from StatMainWindow import Ui_MainWindow
import sys
import pandas as pd


class WindowInterface(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.analyser = analytic.Analytic(self)

        # self.tabs_names_index = {}

        self.import_data_action.triggered.connect(self.load_source_data)

        self.show()

    def show_error(self, message):
        msg = QMessageBox(self)
        msg.setText(message)
        msg.setIcon(QMessageBox.Critical)
        msg.show()

    def view_data(self, df: pd.DataFrame, label: str, name: str):
        qtablewidget = QtWidgets.QTableWidget()
        headers = df.columns.values.tolist()
        qtablewidget.setObjectName(name)
        qtablewidget.setGeometry(QtCore.QRect(5, 10, 741, 491))
        qtablewidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        qtablewidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        qtablewidget.setShowGrid(True)
        qtablewidget.setColumnCount(len(headers))
        qtablewidget.setHorizontalHeaderLabels(headers)

        for i, row in df.iterrows():
            # Добавление строки
            qtablewidget.setRowCount(qtablewidget.rowCount() + 1)
            for j in range(qtablewidget.columnCount()):
                qtablewidget.setItem(i, j, QTableWidgetItem(str(row[j])))

        self.dataTabs.addTab(qtablewidget, label)

    def load_source_data(self):
        path = QFileDialog.getOpenFileName(self, "Выберите файл с данными для загрузки", QDir.currentPath(),
                                           "Электронные таблицы (*.csv *.xls *.xlsx);;Все файлы (*.*)")[0]
        if path:
            self.analyser.set_filepath(path)
            try:
                self.analyser.load_source_data()
            except analytic.UnknownTypeError as e:
                self.show_error("Unsupported file type: " + e.filetype)
            except FileNotFoundError:
                self.show_error("File not found")
            self.view_data(self.analyser.source_data, "Исходные данные", "source_data")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName("Python-stat")
    window = WindowInterface()
    sys.exit(app.exec_())
