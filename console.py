# PYTHON_PATH = "C:/Users/Пользователь/AppData/Local/Programs/Python/Python37-32"


def get_file_type():
    print("excel file")


def main():
    print("Main function")
    exec(open("func.py").read())

if __name__ == '__main__':
    main()
