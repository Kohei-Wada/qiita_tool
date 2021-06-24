from QiitaAPI import *


def main():
    q = QiitaAPI()
    users = q.get_followers("drken", page=1, per_page=100)

    for user in users:
        print(f"user id : {user.id}, github: {user.github_login_name}")


if __name__ == '__main__':
    main()
