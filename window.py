import analytic
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
from StatMainWindow import Ui_MainWindow
from ClustSettDialog import ClustSettDialog
import sys
import pandas as pd


class WindowInterface(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.analyser = analytic.Analytic(self)

        self.tabs_names = {}

        self.import_data_action.triggered.connect(self.load_source_data)
        self.clusterAction.triggered.connect(self.run_cluster)
        self.show()

    def show_error(self, message):
        msg = QMessageBox(self)
        msg.setText(message)
        msg.setIcon(QMessageBox.Critical)
        msg.show()

    def view_data(self, df: pd.DataFrame, label: str, name: str):
        if name in self.tabs_names.keys():
            self.tabs_names[name].set_dataframe(df)
            self.dataTabs.setTabText(self.dataTabs.indexOf(self.tabs_names[name]), label)
        else:
            self.tabs_names[name] = self.DataFrameView(df, name)
            self.dataTabs.addTab(self.tabs_names[name], label)

    def load_source_data(self):
        path = QFileDialog.getOpenFileName(self, "Выберите файл с данными для загрузки", QtCore.QDir.currentPath(),
                                           "Электронные таблицы (*.csv *.xls *.xlsx);;Все файлы (*)")[0]
        if path:
            self.analyser.set_filepath(path)
            try:
                self.analyser.load_source_data()
            except analytic.UnknownTypeError as e:
                self.show_error("Неподдерживаемый тип файла: " + e.filetype)
            except FileNotFoundError:
                self.show_error("Файл не найден")
            self.view_data(self.analyser.source_data, "Исходные данные", "source_data")

    def run_cluster(self):
        def present_results():
            self.view_data(self.analyser.clustered_data, "Кластеризованные данные", "clustered_data")

        cont, params = ClustSettDialog.get_clust_settings(self.analyser.source_data.columns)
        if cont:
            self.analyser.set_n_of_clusts(params['n_of_clusts'])
            self.analyser.set_cols_to_clust(params['cols_to_clust'])
            # TODO: Тут должен быть обработчик исключения из cluster()
            try:
                self.analyser.cluster()
            except analytic.IncorrectDataToClusterError:
                self.show_error("Некорректные данные для кластеризации: значения должны быть числами!")
                return
            except analytic.IncorrectNumberOfClustersError:
                self.show_error("Некорректное число кластеров")
                return
            present_results()

    class DataFrameView(QTableView):
        def __init__(self, data: pd.DataFrame, name: str):
            QTableView.__init__(self)
            self.setModel(self.DataFrameModel(data, self))
            self.setObjectName(name)

        def set_dataframe(self, new_df: pd.DataFrame):
            self.setModel(self.DataFrameModel(new_df, self))

        class DataFrameModel(QtCore.QAbstractTableModel):
            def __init__(self, df: pd.DataFrame, parent=None):
                QtCore.QAbstractTableModel.__init__(self, parent)
                self._data = df

            def rowCount(self, parent=None):
                return self._data.shape[0]

            def columnCount(self, parent=None):
                return self._data.shape[1]

            def data(self, index, role=QtCore.Qt.DisplayRole):
                if index.isValid():
                    if role == QtCore.Qt.DisplayRole:
                        return str(self._data.iloc[index.row(), index.column()])
                return None

            def headerData(self, section, orientation, role: int = ...):
                if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
                    return self._data.columns[section]
                return None


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName("Python-stat")
    window = WindowInterface()
    sys.exit(app.exec_())
