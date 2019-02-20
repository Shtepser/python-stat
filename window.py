import analytic
from PyQt5.QtWidgets import *
from StatMainWindow import Ui_MainWindow
import sys
import pandas as pd

class WindowInterface(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.analyser = analytic.Analytic(self)

        self.show()

    def view_source_data(self):
        df = self.analyser.source_data
        headers = df.columns.values.tolist()

        # Отображение данных на виджете
        table = self.source_data_widget
        table.setColumnCount(len(headers))
        table.setHorizontalHeaderLabels(headers)

        for i, row in df.iterrows():
            # Добавление строки
            table.setRowCount(table.rowCount() + 1)

            for j in range(table.columnCount()):
                table.setItem(i, j, QTableWidgetItem(str(row[j])))

    # noinspection PyMethodMayBeStatic
    def view_data(self, df: pd.DataFrame, qtablewidget: QTableWidget):
        headers = df.columns.values.tolist()
        qtablewidget.setColumnCount(len(headers))
        qtablewidget.setHorizontalHeaderLabels(headers)

        for i, row in df.iterrows():
            # Добавление строки
            qtablewidget.setRowCount(qtablewidget.rowCount() + 1)
            for j in range(qtablewidget.columnCount()):
                qtablewidget.setItem(i, j, QTableWidgetItem(str(row[j])))

    def load_source_data(self):
        self.analyser.filepath, _ = QFileDialog.getOpenFileName(self, "Open file", "", "Text documents (*.csv)", "All files (*.*)")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName("Python-stat")

    window = WindowInterface()
    # tmp
    window.load_source_data()
    # window.analyser.filepath = "sample_table.csv"
    window.analyser.load_source_data()
    window.view_data(window.analyser.source_data, window.source_data_widget)
    # end tmp
    sys.exit(app.exec_())
