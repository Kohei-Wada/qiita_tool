import QiitaAPI


def main():
    items = QiitaAPI.get_user_items("drken")
    for item in items:
        print(item.get_likes_count())


if __name__ == '__main__':
    main()
