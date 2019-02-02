from pprint import pprint
import analytic


class ConsoleInterface:
    def __init__(self):
        print("Console interface for python-stat v 0.0.1")
        analyser = analytic.Analytic(self)
        analyser.load_source_data(input("Enter path to file: "))
        print("Checking data:")
        pprint(analyser.source_data)


if __name__ == '__main__':
    ConsoleInterface()
