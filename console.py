from pprint import pprint
import analytic


class ConsoleInterface:
    def __init__(self):
        self.analyser = analytic.Analytic(self)
        self.run()

    def load_data(self):
        while True:
            self.analyser.set_filepath(input("Enter path to file: "))
            try:
                self.analyser.load_source_data()
            except analytic.UnknownTypeError as e:
                print("Unsupported file type: " + e.filetype)
                continue
            except FileNotFoundError:
                print("File not found")
                continue
            break

    def show_selected_columns(self):
        for i in self.analyser.source_data.columns:
            selected = "Selected" if self.analyser.is_col_in_clust(i) \
                else "Not Selected"
            print("%s - %s" % (i, selected))

    def include_columns(self):
        cols = input("Which columns you want to include (separated by comma with NO spaces)?:\n")
        self.analyser.include_col_to_clust(cols.split(','))

    def exclude_columns(self):
        cols = input("Which columns you want to exclude (separated by comma with NO spaces)?:\n")
        self.analyser.exclude_col_from_clust(cols.split(','))

    def run(self):
        print("Console interface for python-stat v 0.0.1")

        # 1. Загрузка данных
        self.load_data()
        print("Checking data:")
        pprint(self.analyser.source_data)

        # 2. Непосредственно кластеризация
        while True:
            # выбираем столбцы для кластеризации
            # показываем выбранные столбцы
            while True:
                self.show_selected_columns()
                options = {
                    'i': lambda: self.include_columns(),
                    'e': lambda: self.exclude_columns(),
                }
                choice = input("Do you want to ({0})nclude or ({1})xclude columns or ({2})ot? [{0}/{1}/{2}] \n"
                               .format('i', 'e', 'n'))
                if choice == 'n':
                    break
                try:
                    options[choice]()
                except KeyError:
                    print("Unknown option. Please try again")
                continue

            # запрашиваем число кластеров
            self.analyser.set_n_of_clusts(int(input("Enter number of clusters: ")))
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
