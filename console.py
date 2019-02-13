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
        looping = True
        while looping:
            # выбираем столбцы для кластеризации
            # показываем выбранные столбцы
            while True:
                self.show_selected_columns()
                options = {
                    'i': lambda: self.include_columns(),
                    'e': lambda: self.exclude_columns(),
                }
                choice = input("Do you want to ({0})nclude or ({1})xclude columns or ({2})ot? \n"
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
            print("Successfully clustered")

            while True:
                options = {
                    'h': lambda: self.show_clustered(),
                    's': lambda: self.save_clustered(),
                    'a': lambda: self.add_clustered_to_source(),
                }
                choice = input("Do you want to s({0})ow results, ({1})ave it, ({2})dd it to original data, "
                               "({3})etry analysis or ({4})xit?\n".format('h', 's', 'a', 'r', 'e'))
                if choice == 'r':
                    break
                if choice == 'e':
                    looping = False
                    break
                try:
                    options[choice]()
                except KeyError:
                    print("Unknown option. Please try again")
                    continue
            continue

        # 3. Вывод результатов кластеризации
        # TODO: а вот сюда впихнуть половину, блин, авгиева цикла из п.2

    def show_clustered(self):
        print("\n\nResults of analysis:\n")
        pprint(self.analyser.clustered_data)

    def save_clustered(self):
        savepath = input("Enter path to save results: ")
        try:
            self.analyser.save_clustered_data(savepath)
        except analytic.UnknownTypeError as e:
            print("Unsupported filetype: " + e.filetype)
        print("Successfully saved")


if __name__ == '__main__':
    ConsoleInterface()
