from pprint import pprint
import analytic

# TODO: устранить баг выдачи ошибки неверных данных при слишком большом числе кластеров
# TODO: добавить обработку ошибки при некорректном вводе числа кластеров (при введении не-числа)


class ConsoleInterface:
    def __init__(self):
        self.analyser = analytic.Analytic(self)
        self.run()

    def run(self):
        completed = False  # завершён ли анализ - прекращается ли цикл

        def load_data():
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

        def check_data():
            def show_loaded():
                print("\n\nLoaded data:\n")
                pprint(self.analyser.source_data)

            while True:
                options = {
                    'y': lambda : show_loaded(),
                    'n': lambda : None
                }
                choice = input("Do you want to view loaded data? [y/n]")
                try:
                    options[choice]()
                except KeyError:
                    print("Unknown option")
                    continue
                break

        def set_params():
            def set_columns_to_clust():
                def show_selected_columns():
                    for i in self.analyser.source_data.columns:
                        selected = "Selected" if self.analyser.is_col_in_clust(i) \
                            else "Not Selected"
                        print("%s - %s" % (i, selected))

                def include_columns():
                    cols = input("Which columns you want to include (separated by comma with NO spaces)?:\n")
                    self.analyser.include_col_to_clust(cols.split(','))

                def exclude_columns():
                    cols = input("Which columns you want to exclude (separated by comma with NO spaces)?:\n")
                    self.analyser.exclude_col_from_clust(cols.split(','))

                while True:
                    show_selected_columns()
                    options = {
                        'i': lambda: include_columns(),
                        'e': lambda: exclude_columns(),
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

            def set_n_of_clusts():
                self.analyser.set_n_of_clusts(int(input("Enter number of clusters: ")))

            set_columns_to_clust()
            set_n_of_clusts()

        def cluster():
            self.analyser.cluster()
            print("Successfully clustered")

        def use_results():
            def show_clustered():
                print("\n\nResults of analysis:\n")
                pprint(self.analyser.clustered_data)

            def save_clustered():
                savepath = input("Enter path to save results: ")
                try:
                    self.analyser.save_clustered_data(savepath)
                except analytic.UnknownTypeError as e:
                    print("Unsupported filetype: " + e.filetype)
                print("Successfully saved")

            def add_clustered_to_source():
                try:
                    self.analyser.save_clustered_data(self.analyser.filepath)
                except analytic.UnknownTypeError as e:
                    print("Unsupported filetype: " + e.filetype)
                print("Successfully saved")

            options = {
                'h': lambda: show_clustered(),
                's': lambda: save_clustered(),
                'a': lambda: add_clustered_to_source()
            }

            while True:
                choice = input("Do you want to s({0})ow results, ({1})ave it, ({2})dd it to original data, "
                               "({3})etry analysis or ({4})xit?\n".format('h', 's', 'a', 'r', 'e'))
                if choice == 'r':
                    break
                if choice == 'e':
                    nonlocal completed
                    completed = True
                    break
                try:
                    options[choice]()
                except KeyError:
                    print("Unknown option. Please try again")
                    continue

        print("Console interface for python-stat v 0.0.1")
        load_data()
        check_data()

        """
        цикл: 
        выбрали параметры - провели анализ - просмотрели результаты - завершили работу или выбрали новые параметры
        """
        while not completed:
            set_params()
            try:
                cluster()
            except analytic.IncorrectDataToClusterError:
                print("Incorrect data to cluster: values should be numeric")
                continue
            except analytic.IncorrectNumberOfClustersError:
                print("Incorrect number of clusters")
                continue
            use_results()


if __name__ == '__main__':
    ConsoleInterface()
