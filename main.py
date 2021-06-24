from QiitaAPI import *


def main():
    my_id = "program3152019"
    q = QiitaAPI()
    res = q.get_users()
    print(res)


if __name__ == '__main__':
    main()
