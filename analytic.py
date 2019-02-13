import pandas as pd
import re
from copy import deepcopy
from sklearn.cluster import KMeans


class UnknownTypeError(Exception):
    """ Ошибка нераспознанного типа для чтения/записи файла """

    def __init__(self, filetype):
        self.filetype = filetype


class IncorrectDataToClusterError(Exception):
    """ Ошибка некорректно выбранных данных """
    # "Incorrect data to cluster: values should be numeric"


class IncorrectNumberOfClustersError(Exception):
    """ Ошибка некорректного числа кластеров """


class Analytic:
    """
        Аналитическое ядро программы, непосредственно хранящее и обрабатывающее данные.
    """

    def __init__(self, interface):
        self.interface = interface
        self.filepath = ""
        self.source_data = pd.DataFrame()
        self.clustered_data = pd.DataFrame()
        self.cols_to_clust = []
        self.n_of_clusts = 1

    def set_filepath(self, filepath):
        self.filepath = filepath

    def load_source_data(self):
        file_ext = re.search(r'\.[\w\d]+$', self.filepath)[0]  # расширение файла
        types = {
            ".xlsx": lambda path: pd.read_excel(path),
            ".xls": lambda path: pd.read_excel(path),
            ".csv": lambda path: pd.read_csv(path)
        }
        try:
            self.source_data = types[file_ext](self.filepath)
        except KeyError:
            raise UnknownTypeError(file_ext)
        self.cols_to_clust = list(deepcopy(self.source_data.columns))

    def is_col_in_clust(self, column):
        """ Проверяет, используется ли столбец для кластеризации """
        return column in self.cols_to_clust

    def exclude_col_from_clust(self, columns):
        """ Исключает столбец из используемых для кластеризации """
        for col in columns:
            if col in self.cols_to_clust:
                self.cols_to_clust.remove(col)

    def include_col_to_clust(self, columns):
        """ Включает столбец в используемые для кластеризации """
        for col in columns:
            if col not in self.cols_to_clust:
                self.cols_to_clust.append(col)

    def set_n_of_clusts(self, num):
        self.n_of_clusts = num

    def cluster(self):
        # TODO: добавить возможность выбора метода кластеризации
        # TODO: добавить возможность выбора параметров (столбцов) для кластеризации
        self.clustered_data = deepcopy(self.source_data)
        try:
            # добавляем 1, т.к. изначально кластеры нумеруются с 0
            self.clustered_data['cluster'] = KMeans(self.n_of_clusts) \
                                                 .fit(self.source_data[self.cols_to_clust]).labels_ + 1
        except ValueError:
            raise IncorrectDataToClusterError

    def save_clustered_data(self, savepath):
        file_ext = re.search(r'\.[\w\d]+$', savepath)[0]  # расширение файла
        types = {
            ".xlsx": lambda path: self.clustered_data.to_excel(path),
            ".xls": lambda path: self.clustered_data.to_excel(path),
            ".csv": lambda path: self.clustered_data.to_csv(path)
        }
        try:
            types[file_ext](savepath)
        except KeyError:
            raise UnknownTypeError(file_ext)
