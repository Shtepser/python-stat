from pprint import pprint
import analytic


class ConsoleInterface:
    def __init__(self):
        self.analyser = analytic.Analytic(self)
        self.run()

    def run(self):
        print("Console interface for python-stat v 0.0.1")
        while True:
            filepath = input("Enter path to file: ")
            try:
                self.analyser.load_source_data(filepath=filepath)
            except analytic.UnknownTypeError as e:
                print("Unsupported file type: " + e.type)
                continue
            except FileNotFoundError:
                print("File not found")
                continue
            break
        print("Checking data:")
        pprint(self.analyser.source_data)
        no_clusters = int(input("Enter number of clusters: "))
        self.analyser.cluster(no_clusters)
        pprint(self.analyser.clustered_data)


if __name__ == '__main__':
    ConsoleInterface()
