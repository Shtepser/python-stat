from pprint import pprint
import analytic


class ConsoleInterface:
    def __init__(self):
        self.analyser = analytic.Analytic(self)
        self.run()

    def run(self):
        print("Console interface for python-stat v 0.0.1")

        # 1. Загрузка данных
        while True:
            filepath = input("Enter path to file: ")
            try:
                self.analyser.load_source_data(filepath=filepath)
            except analytic.UnknownTypeError as e:
                print("Unsupported file type: " + e.filetype)
                continue
            except FileNotFoundError:
                print("File not found")
                continue
            break
        print("Checking data:")
        pprint(self.analyser.source_data)

        # 2. Непосредственно кластеризация
        while True:
            # выбираем столбцы для кластеризации
            # показываем выбранные столбцы
            for i in range(len(self.analyser.source_data.columns)):
                selected = "Selected" if self.analyser.source_data.columns[i] in self.analyser.cols_to_clust else "Not Selected"
                print("%i. %s - %s" % (i + 1, self.analyser.source_data.columns[i], selected))
            # запрашиваем число кластеров
            self.analyser.n_of_clusts = int(input("Enter number of clusters: "))
            # пробуем кластеризовать, если не получилось - запускаем процесс заново
            try:
                self.analyser.cluster()
            except analytic.IncorrectDataToClusterError:
                print("Incorrect data to cluster: values should be numeric")
                continue
            except analytic.IncorrectNumberOfClustersError:
                print("Incorrect number of clusters")
                continue
            print("Success")
            break

        # 3. Вывод результатов кластеризации
        pprint(self.analyser.clustered_data)


if __name__ == '__main__':
    ConsoleInterface()
