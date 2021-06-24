import json
import requests


# this class is wrapper for qiita api
class QiitaAPI:
    def __init__(self):
        self.qiita = "https://qiita.com/api/v2/"
        self.success = 204

    # LGTM
    # ACCESS TOKEN
    # GROUP

    # COMMENT

    # delete the comment
    def delete_comment(self, comment_id):
        requests.delete(self.qiita + "comments/" + comment_id)
        return

    # get a comment
    def get_comment(self, comment_id):
        res = requests.get(self.qiita + "comments/" + comment_id)
        return json.loads(res.text)

    # TAGGING

    # TAG

    # TEAM

    # PROJECT

    # USER

    # get a list of users who have stocked articles int descending order of stock date and time
    def get_stockers(self, item_id, page=1, per_page=20):
        res = requests.get(self.qiita + "items/" + item_id + "/stockers?" +
                           "page=" + str(page) + "&" + "per_page=" + str(per_page))
        return json.loads(res.text)

    # get a list of all users in descending order of creation date and time.
    def get_users(self, page=1, per_page=20):
        res = requests.get(self.qiita + "users?" +
                           "page=" + str(page) + "&" + "per_page=" + str(per_page))
        return res.json()

    # get the user.
    def get_user(self, user_id):
        return requests.get(self.qiita + user_id).json()

    # get the list of users that the user is following
    def get_followees(self, user_id):
        return requests.get(self.qiita + "users/" + user_id + "/followees").json()

    # get a list of users who are following users.
    def get_followers(self, user_id, page, per_page):
        return requests.get(self.qiita + "users/" + user_id + "/followers?" +
                            "page=" + str(page) + "&" + "per_page" + str(per_page)).json()

    # unfollow the user, return true if successful
    def unfollow(self, user_id):
        res = requests.delete(self.qiita + "users/" + user_id + "/following")
        return res.status_code == self.success

    # return true if you are following the user.
    def is_following(self):
        return

    def follow(self, user_id):
        requests.put(self.qiita + "users/" + user_id + "/following")

    # POST : represents a post from a user

    # get a list of articles in descending order of creation date and time
    def get_items(self, user_id, page=1, per_page=100):
        return

    # get the article list of the specified user in descending order of creation date and time
    def get_user_items(self, user_id, page=1, per_page=20):
        return requests.get(self.qiita + "users/" + user_id +
                            "/items?" + "page=" + str(page) + "&" + "per_page=" + str(per_page)).json()
