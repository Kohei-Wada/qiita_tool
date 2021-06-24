from QiitaAPI import *


def main():
    q = QiitaAPI()
    users = q.get_followees("drken")



    for user in users:
        print(user.has_github_account())




if __name__ == '__main__':
    main()
