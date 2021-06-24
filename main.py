from QiitaAPI import *


def main():
    my_id = "program3152019"
    q = QiitaAPI()
    followees = q.get_followees(my_id)

    for i in followees:
        print(f'name : {i.name}, github : {i.github_login_name}')



if __name__ == '__main__':
    main()
