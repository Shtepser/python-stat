import pandas as pd
import re


class UnknownTypeError(Exception):
    """ Ошибка нераспознанного типа для открытия файла """

    def __init__(self, type):
        self.type = type


class Analytic:
    def __init__(self, interface):
        self.interface = interface
        self.source_data = pd.DataFrame()

    def load_source_data(self, filepath):
        file_ext = re.search(r'\.[\w\d]+$', filepath)[0] # расширение файла
        types = {
                ".xlsx" : lambda path: pd.read_excel(path),
                ".xls"  : lambda path: pd.read_excel(path),
                ".csv"  : lambda path: pd.read_csv(path)
        }
        # TODO: добавить возможность загрузки .xls и .xlsx файлов, с возможностью автоматического определения
        # TODO: добавить обработку ошибки чтения/парсинга файла

        try:
            self.source_data = types[file_ext](filepath)
        except KeyError:
            raise UnknownTypeError(file_ext)
