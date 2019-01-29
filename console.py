# PYTHON_PATH = "C:/Users/Пользователь/AppData/Local/Programs/Python/Python37-32"


def add_loading(filename):
    f = open('script.py', 'w')
    f.write('print("script")')


def exec_script():
    exec(open("script.py").read())


def main():
    print("Main function")
    add_loading("file")
    exec_script()


if __name__ == '__main__':
    main()
