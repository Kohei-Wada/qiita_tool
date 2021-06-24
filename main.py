from QiitaAPI import QiitaAPI 


def main():
    q = QiitaAPI()
    user = q.get_user("drken")


if __name__ == '__main__':
    main()
