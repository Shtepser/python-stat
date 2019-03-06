import analytic
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
from StatMainWindow import Ui_MainWindow
from ClustSettDialog import ClustSettDialog
from ColumnsScatterPlotDialog import ScatterPlotColumnsDialog
import sys
import pandas as pd

from scipy.cluster.hierarchy import dendrogram
from matplotlib import pyplot as plt

import numpy as np
from itertools import cycle, islice

class WindowInterface(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.analyser = analytic.Analytic(self)

        self.tabs_names = {}

        self.import_data_action.triggered.connect(self.load_source_data)
        self.export_marks_action.triggered.connect(self.save_marks)
        self.export_distance_action.triggered.connect(self.save_distances)
        self.clusterAction.triggered.connect(self.run_cluster)
        self.dendrogram_action.triggered.connect(self.present_dendrogram)
        self.scatterplot_action.triggered.connect(self.present_scatterplot)

        self.show()

    def report_error(self, error_message):
        """
        Показывает окно с сообщением об ошибке
        :param error_message: Текст сообщения об ошибке
        """
        msg = QMessageBox(self)
        msg.setText(error_message)
        msg.setIcon(QMessageBox.Critical)
        msg.show()

    def show_message(self, message):
        """
        Показывает пользователю сообщение
        :param message: текст сообщения
        """
        msg = QMessageBox(self)
        msg.setText(message)
        msg.setIcon(QMessageBox.Information)
        msg.show()

    def view_data(self, df: pd.DataFrame, label: str, name: str):
        """
        Отображает данные (pandas.DataFrame) в новой вкладке
        :param df: pandas.DataFrame, который будет отображаться
        :param label: отображаемое имя данных
        :param name: название данных (для дальнейшего обращения к ним)
        """
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
                self.report_error("Неподдерживаемый тип файла: " + e.filetype)
            except FileNotFoundError:
                self.report_error("Файл не найден")
            self.view_data(self.analyser.source_data, "Исходные данные", "source_data")

    def save_marks(self):
        """
        Сохраняет таблицу с кластеризованными данными
        TODO: Добавить работу одновременно с несколькими результатами кластеризации
        TODO: Добавить возможность сохранения графиков и диаграмм
        """
        path = QFileDialog.getSaveFileName(self, "Выберите место для сохранения файла", QtCore.QDir.currentPath(),
                                           "CSV-файл (*.csv) ;;Лист Excel (*.xls) ;; Лист Excel (*.xlsx)")[0]
        if path:
            try:
                self.analyser.save_clustered_data(path)
            except analytic.UnknownTypeError as e:
                self.report_error("Неподдерживаемый тип файла: " + e.filetype)
                return
            except Exception as e:
                self.report_error(str(e))
                return
            self.show_message("Файл успешно сохранён")

    def save_distances(self):
        path = QFileDialog.getSaveFileName(self, "Выберите место для сохранения файла", QtCore.QDir.currentPath(),
                                           "CSV-файл (*.csv) ;;Лист Excel (*.xls) ;; Лист Excel (*.xlsx)")[0]
        if path:
            try:
                self.analyser.save_data(savepath=path, data=pd.DataFrame(self.analyser.distance_matrix))
            except analytic.UnknownTypeError as e:
                self.report_error("Неподдерживаемый тип файла: " + e.filetype)
                return
            except Exception as e:
                self.report_error(str(e))
                return
            self.show_message("Файл успешно сохранён")

    def run_cluster(self):
        def present_results():
            """
            Представляет результат кластерного анализа пользователю
            TODO: Выбор вариантов представления (таблица с метками, график, дерево)
            """
            self.view_data(pd.DataFrame(self.analyser.distance_matrix),     # Привет, костыль! - по-хорошему, TODO:
                           # сделать так, чтобы view_data работал не только с pandas Dataframe, но и с ndarray
                           "Матрица расстояний, метод: " + self.analyser.method,
                           "distance_matrix")
            self.view_data(self.analyser.clustered_data,
                           "Метки кластеров: n = " + str(self.analyser.n_of_clusts),
                           "clustered_data")

        options = {"data_columns": self.analyser.source_data.columns,
                   "criterions": analytic.CRITERIONS,
                   "methods": analytic.METHODS,
                   "metrics": analytic.METRICS}

        cont, params = ClustSettDialog.get_clust_settings(options)
        if cont:
            self.analyser.set_n_of_clusts(params['n_of_clusts'])
            self.analyser.set_cols_to_clust(params['cols_to_clust'])
            self.analyser.method = params['method']
            self.analyser.metric = params['metric']
            self.analyser.criterion = params['criterion']
            try:
                self.analyser.cluster()
            except analytic.IncorrectDataToClusterError:
                self.report_error("Некорректные данные для кластеризации: значения должны быть числами!")
                return
            except analytic.IncorrectNumberOfClustersError:
                self.report_error("Некорректное число кластеров")
                return
            present_results()

    def present_dendrogram(self):
        """
        Выводит дендрограмму кластеров
        TODO: сделать показ не в отдельном окне, а во вкладке
        """

        figure = plt.figure(figsize=(12, 5))
        try:
            dn = dendrogram(self.analyser.linkage_matrix, labels=self.analyser.source_data.index)
        except TypeError:
            self.report_error("Матрица расстояний имеет недопустимый вид!")
            return
        plt.show()

    def present_scatterplot(self):
        """
        Выводит график рассеяния данных
        """
        columns = ScatterPlotColumnsDialog.get_columns(self.analyser.source_data.columns)
        if columns:
            colors = np.array(list(islice(cycle(['#377eb8', '#ff7f00', '#4daf4a',
                                                 '#f781bf', '#a65628', '#984ea3',
                                                 '#999999', '#e41a1c', '#dede00']),
                                          int(max(self.analyser.clustered_data["cluster"]) + 1))))
            try:
                plt.scatter(x=self.analyser.source_data[columns["x_axis_column"]],
                            y=self.analyser.source_data[columns["y_axis_column"]],
                            color=colors[self.analyser.clustered_data["cluster"]])
                plt.xlabel(columns["x_axis_column"])
                plt.ylabel(columns["y_axis_column"])
                plt.show()
            except Exception as e:
                self.report_error(str(e))

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
