from pprint import pprint
import analytic


class ConsoleInterface:
    def __init__(self):
        analyser = analytic.Analytic(self)
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
            break
        print("Checking data:")
        pprint(self.analyser.source_data)


if __name__ == '__main__':
    ConsoleInterface()
