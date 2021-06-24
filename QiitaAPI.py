import json
import requests


class QiitaAPI:
    def __init__(self):
        self.qiita = "https://qiita.com/api/v2/"

    def delete_commend(self, comment_id):
        requests.delete(self.qiita + "comments/" + comment_id)
        return

    def get_comment(self, comment_id):
        requests.get(self.qiita + "comments/" + comment_id)

    def get_items(self, user_id, page=1, per_page=100):
        return

    # get a list of all users in descending order of creation date and time.
    def get_users(self, page=1, per_page=20):
        res = requests.get(self.qiita + "users?" +
                           "page=" + str(page) + "&" + "per_page=" + str(per_page))
        return json.loads(res.text)

    # get the user.
    def get_user(self, user_id):
        res = requests.get(self.qiita + user_id)
        return json.loads(res.text)

    # get the list of users that the user is following
    def get_followees(self, user_id):
        res = requests.get(self.qiita + "users/" + user_id + "/followees")
        return json.loads(res.text)

    # get a list of users who are following users.
    def get_followers(self, user_id, page, per_page):
        res = requests.get(self.qiita + "users/" + user_id + "/followers?" +
                           "page=" + str(page) + "&" + "per_page" + str(per_page))
        return json.loads(res.text)

    # unfollow the user
    def unfollow(self, user_id):
        requests.delete(self.qiita + "users/" + user_id + "/following")
        return

    # return true if you are following the user.
    def is_following(self):
        return

