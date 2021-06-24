import json
import requests
from QiitaUser import *


def qiita_user_decoder(obj):
    return QiitaUser(obj['description'],
                     obj['facebook_id'],
                     obj['followees_count'],
                     obj['followers_count'],
                     obj['github_login_name'],
                     obj['id'],
                     obj['items_count'],
                     obj['linkedin_id'],
                     obj['location'],
                     obj['name'],
                     obj['organization'],
                     obj['permanent_id'],
                     obj['profile_image_url'],
                     obj['team_only'],
                     obj['twitter_screen_name'],
                     obj['website_url'])


# this class is wrapper for qiita api
class QiitaAPI:
    def __init__(self):
        self.qiita = "https://qiita.com/api/v2/"
        self.success = 204

    # LGTM

    # get a list of "LGTM!" that attached article in descending order
    def get_item_lgtm(self, item_id):
        return requests.get(self.qiita + "items/" + item_id + "/likes").json()

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

    def get_item_comments(self, item_id):
        return requests.get(self.qiita + "items/" + item_id + "/comments")

    # TAGGING

    # TAG
    # get the list of tags that is followed by user
    def get_following_tags(self, user_id, page=1, per_page=20):
        return requests.get(self.qiita + "users/" + user_id + "/following_tags?" +
                            "page=" + str(page) + "&" + "per_page=" + str(per_page)).json()

    # unfollow the tag, if successful return true
    def unfollow_tag(self, tag_id):
        res = requests.delete(self.qiita + "tags/" + tag_id + "/following")
        return res.status_code == self.success

    # follow the tag
    def follow_tage(self, tag_id):
        res = requests.put(self.qiita + "tags/" + tag_id + "following")
        return res.status_code == self.success

    # TEAM

    # PROJECT

    # USER

    # get a list of users who have stocked articles
    # in descending order of stock date and time
    def get_stockers(self, item_id, page=1, per_page=20):
        res = requests.get(self.qiita + "items/" + item_id + "/stockers?" +
                           "page=" + str(page) + "&" + "per_page=" + str(per_page))
        return json.loads(res.text)

    # get a list of all users in descending
    # order of creation date and time.
    def get_users(self, page=1, per_page=20):
        res = requests.get(self.qiita + "users?" +
                           "page=" + str(page) + "&" + "per_page=" + str(per_page))
        return res.json()

    # get the qiita user object.
    def get_user(self, user_id):
        return json.loads(requests.get(self.qiita + "users/" + user_id).text,
                          object_hook=qiita_user_decoder)

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

    # get a list of articles in descending
    # order of creation date and time
    def get_items(self, user_id, page=1, per_page=100):
        return

    # get the article list of the specified user
    # in descending order of creation date and time
    def get_user_items(self, user_id, page=1, per_page=20):
        return requests.get(self.qiita + "users/" + user_id +
                            "/items?" + "page=" + str(page) + "&" + "per_page=" + str(per_page)).json()
