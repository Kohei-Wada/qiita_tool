from Qiita import QiitaAPI


def main():
    user = QiitaAPI.get_user("drken")
    followers = user.get_followers(20)

    for user in followers:
        print(f"{user.id} : {user.get_github_url()}")


if __name__ == '__main__':
    main()
