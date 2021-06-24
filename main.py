from QiitaAPI import QiitaAPI 


def main():
    q = QiitaAPI()
    user = q.get_user("drken")
    items = q.get_user_items("drken", 1, 5)

    coments_list = []
    for item in items:
        coments_list.append(q.get_item_comments(item.get_id()))

    comments = coments_list[1]

    for comment in comments:
        print(comment.get_user().get_github_url())





if __name__ == '__main__':
    main()
