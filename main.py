from Qiita import QiitaAPI


def main():
    user = QiitaAPI.get_user("program3152019")
    print(user.get_followers_count())


if __name__ == '__main__':
    main()
