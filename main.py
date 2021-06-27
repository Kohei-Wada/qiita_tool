from Qiita import QiitaAPI
import sys


def main():
    args = sys.argv[1:]

    if args:
        target_id = args[0]
    else:
        target_id = "drken"

    target = QiitaAPI.get_user(target_id)

    if target is None:
        return

    if target.get_followees_count() != 0:
        users = target.get_followees(20)
    elif target.get_followers_count() != 0:
        users = target.get_followers(20)
    else:
        return

    for user in users:
        if user.has_github_account():
            print(f"{user.get_id()}, {user.get_github_url()}")


if __name__ == '__main__':
    main()
