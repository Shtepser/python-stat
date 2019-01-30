import pandas as pd


class Analytic:
    def __init__(self, interface):
        self.interface = interface
        self.source_data = pd.DataFrame()

    def load_source_data(self, filepath):
        # TODO: добавить возможность загрузки .xls и .xlsx файлов, с возможностью автоматического определения
        # TODO: добавить обработку ошибки чтения/парсинга файла
        self.source_data = pd.read_csv(filepath)