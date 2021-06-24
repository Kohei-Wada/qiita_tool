import json
import requests

from collections import namedtuple
from decoders import *


# this class is wrapper for Qiita API


class QiitaAPI:
    def __init__(self):
        self.qiita = "https://qiita.com/api/v2/"
        self.ok = 200
        self.created = 201
        self.success = 204
        self.rate_limit = 403

    ##################################################################################################################
    # LGTM

    # get a list of "LGTM!" that attached article in descending order
    def get_item_lgtm(self, item_id):
        return requests.get(self.qiita + "items/" + item_id + "/likes").json()

    ##################################################################################################################
    # ACCESS TOKEN

    ##################################################################################################################
    # GROUP

    ##################################################################################################################
    # COMMENT

    # delete the comment
    def delete_comment(self, comment_id):
        requests.delete(self.qiita + "comments/" + comment_id)
        return

    # get a comment
    def get_comment(self, comment_id):
        res = requests.get(self.qiita + "comments/" + comment_id)

        if res.status_code == self.rate_limit:
            return None

        return json.loads(res.text, object_hook=qiita_comment_decoder)

    def get_item_comments(self, item_id):
        comments = []
        res = requests.get(self.qiita + "items/" + item_id + "/comments")

        if res.status_code == self.rate_limit:
            return None

        for data in res.json():
            comments.append(qiita_comment_decoder(data))

        return comments

    ##################################################################################################################
    # TAGGING

    ##################################################################################################################
    # TAG
    # get the list of tags that is followed by user
    def get_following_tags(self, user_id, page=1, per_page=20):
        tags = []
        res = requests.get(self.qiita + "users/" + user_id + "/following_tags?" +
                           "page=" + str(page) + "&" + "per_page=" + str(per_page))

        if res.status_code == self.rate_limit:
            return None

        for data in res.json():
            tags.append(qiita_tag_decoder(data))

        return tags

    # unfollow the tag, if successful return true
    def unfollow_tag(self, tag_id):
        res = requests.delete(self.qiita + "tags/" + tag_id + "/following")
        return res.status_code == self.success

    # follow the tag
    def follow_tag(self, tag_id):
        res = requests.put(self.qiita + "tags/" + tag_id + "following")
        return res.status_code == self.success

    ##################################################################################################################
    # TEAM

    ##################################################################################################################
    # PROJECT

    ##################################################################################################################
    # USER

    # get a list of users who have stocked articles
    # in descending order of stock date and time
    def get_stockers(self, item_id, page=1, per_page=20):
        stockers = []
        res = requests.get(self.qiita + "items/" + item_id + "/stockers?" +
                           "page=" + str(page) + "&" + "per_page=" + str(per_page))

        if res.status_code == self.rate_limit:
            return None

        for data in res.json():
            stockers.append(qiita_user_decoder(data))

        return stockers

    # get a list of all users in descending
    # order of creation date and time.
    def get_users(self, page=1, per_page=20):
        users = []
        res = requests.get(self.qiita + "users?" +
                           "page=" + str(page) + "&" + "per_page=" + str(per_page))

        if res.status_code == self.rate_limit:
            return None
        for data in res.json():
            users.append(namedtuple("QiitaUser", data.keys())(*data.values()))
        return users

    # get the qiita user object.
    def get_user(self, user_id):
        res = requests.get(self.qiita + "users/" + user_id)
        if res.status_code == self.rate_limit:
            return None

        return json.loads(res.text, object_hook=qiita_user_decoder)

    # get the list of qiita user objects that the user is following
    def get_followees(self, user_id, page=1, per_page=100):
        followees = []
        res = requests.get(self.qiita + "users/" + user_id + "/followees?" +
                           "page=" + str(page) + "&" + "per_page=" + str(per_page))
        if res.status_code == self.rate_limit:
            return None
        for data in res.json():
            followees.append(qiita_user_decoder(data))
        return followees

    # get a list of users who are following users.
    def get_followers(self, user_id, page, per_page):
        followers = []
        res = requests.get(self.qiita + "users/" + user_id + "/followers?" +
                           "page=" + str(page) + "&" + "per_page" + str(per_page))

        if res.status_code == self.rate_limit:
            return None
        for data in res.json():
            followers.append(qiita_user_decoder(data))
        return followers

    # unfollow the user, return true if successful
    def unfollow(self, user_id):
        res = requests.delete(self.qiita + "users/" + user_id + "/following")
        return res.status_code == self.success

    # return true if you are following the user.
    def is_following(self):
        return

    # follow the user. if success return true
    def follow(self, user_id):
        res = requests.put(self.qiita + "users/" + user_id + "/following")
        return res.status_code == self.success

    ##################################################################################################################
    # POST(ITEM) : represents a post from a user

    # get a list of articles in descending
    # order of creation date and time
    def get_items(self, page=1, per_page=100):
        items = []
        res = requests.get(self.qiita + "items?" +
                           "page=" + str(page) + "&" + "per_page=" + str(per_page))
        if res.status_code == self.rate_limit:
            return None

        for data in res.json():
            items.append(qiita_post_decoder(data))

        return items

    # get the article list of the specified user
    # in descending order of creation date and time
    def get_user_items(self, user_id, page=1, per_page=20):
        items = []
        res = requests.get(self.qiita + "users/" + user_id +
                           "/items?" + "page=" + str(page) + "&" + "per_page=" + str(per_page))

        if res.status_code == self.rate_limit:
            return None

        for data in res.json():
            items.append(qiita_post_decoder(data))

        return items
