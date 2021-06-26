import json
import requests

from decoders import *

# this class is wrapper for Qiita API


qiita = "https://qiita.com/api/v2/"
OK = 200
SUCCESS = 204
RATE_LIMIT = 403

##################################################################################################################
# LGTM

"""
get a list of "LGTM!" that attached article in descending order
"""


def get_item_lgtm(item_id):
    lgtms = []
    res = requests.get(qiita + "items/" + item_id + "/likes")
    if res.status_code == RATE_LIMIT:
        return None

    for data in res.json():
        lgtms.append(qiita_lgtm_decoder(data))

    return res

    ##################################################################################################################
    # ACCESS TOKEN

    ##################################################################################################################
    # GROUP

    ##################################################################################################################
    # COMMENT


"""
delete the comment
"""


def delete_comment(comment_id):
    requests.delete(qiita + "comments/" + comment_id)
    return


"""
get a comment object
"""


def get_comment(comment_id):
    res = requests.get(qiita + "comments/" + comment_id)

    if res.status_code == RATE_LIMIT:
        return None

    return json.loads(res.text, object_hook=qiita_comment_decoder)


"""
get the list of comment object attached to item.
"""


def get_item_comments(item_id):
    comments = []
    res = requests.get(qiita + "items/" + item_id + "/comments")

    if res.status_code == RATE_LIMIT:
        return None

    for data in res.json():
        comments.append(qiita_comment_decoder(data))

    return comments


##################################################################################################################
# TAGGING

##################################################################################################################
# TAG

"""
get the tag object list in descending order 
of creation date and time.
"""


def get_all_tags(page=1, per_page=20):
    tags = []
    res = requests.get(qiita + "tags?" +
                       "page=" + str(page) + "&" + "per_page=" + str(per_page))
    if res.status_code == RATE_LIMIT:
        return None

    for data in res.json():
        tags.append(qiita_tag_decoder(data))

    return tags


"""
get the tag object.
"""


def get_tag(tag_id):
    res = requests.get(qiita + "tags/" + tag_id)
    if res.status_code == RATE_LIMIT:
        return None

    return json.loads(res.text, object_hook=qiita_tag_decoder)


"""
get the list of tag object that is followd by user
"""


def get_following_tags(user_id, page=1, per_page=20):
    tags = []
    res = requests.get(qiita + "users/" + user_id + "/following_tags?" +
                       "page=" + str(page) + "&" + "per_page=" + str(per_page))

    if res.status_code == RATE_LIMIT:
        return None

    for data in res.json():
        tags.append(qiita_tag_decoder(data))

    return tags


"""
unfollow the tag. if successful, return true.
"""


def unfollow_tag(self, tag_id):
    res = requests.delete(self.qiita + "tags/" + tag_id + "/following")
    return res.status_code == self.success


"""
follow the tag
"""


def follow_tag(tag_id):
    res = requests.put(qiita + "tags/" + tag_id + "following")
    return res.status_code == SUCCESS


##################################################################################################################
# TEAM

##################################################################################################################
# PROJECT

##################################################################################################################
# USER

"""
get the list of users who have stacked articles 
in descending order of stack date and time.
"""


def get_stockers(item_id, page=1, per_page=20):
    stockers = []
    res = requests.get(qiita + "items/" + item_id + "/stockers?" +
                       "page=" + str(page) + "&" + "per_page=" + str(per_page))

    if res.status_code == RATE_LIMIT:
        return None

    for data in res.json():
        stockers.append(qiita_user_decoder(data))

    return stockers


"""
get the list of all user object in descending order
of creation date and time.
"""


def get_users(page=1, per_page=20):
    users = []
    res = requests.get(qiita + "users?" +
                       "page=" + str(page) + "&" + "per_page=" + str(per_page))

    if res.status_code == RATE_LIMIT:
        return None
    for data in res.json():
        users.append(qiita_user_decoder(data))
    return users


"""
get the qiita user object.
"""


def get_user(user_id):
    res = requests.get(qiita + "users/" + user_id)
    if res.status_code == RATE_LIMIT:
        return None

    return json.loads(res.text, object_hook=qiita_user_decoder)


"""
get the list of qiita user objects that the user is following.
"""


def get_followees(user_id, page=1, per_page=20):
    followees = []
    res = requests.get(qiita + "users/" + user_id + "/followees?" +
                       "page=" + str(page) + "&" + "per_page=" + str(per_page))
    if res.status_code == RATE_LIMIT:
        return None
    for data in res.json():
        followees.append(qiita_user_decoder(data))
    return followees


"""
get the list of user object who are following the users.
"""


def get_followers(user_id, page=1, per_page=20):
    followers = []
    res = requests.get(qiita + "users/" + user_id + "/followers?" +
                       "page=" + str(page) + "&" + "per_page" + str(per_page))

    if res.status_code == RATE_LIMIT:
        return None
    for data in res.json():
        followers.append(qiita_user_decoder(data))
    return followers


"""
unfollowing the user, if successful, return true.
"""


def unfollow(user_id):
    res = requests.delete(qiita + "users/" + user_id + "/following")
    return res.status_code == SUCCESS


def is_following():
    return


"""
follow the user. if success, return true.
"""


def follow(user_id):
    res = requests.put(qiita + "users/" + user_id + "/following")
    return res.status_code == SUCCESS


##################################################################################################################
# POST(ITEM) : represents a post from a user

"""
get the list of article object in descending order
of creation date and time.
"""


def get_items(page=1, per_page=100):
    items = []
    res = requests.get(qiita + "items?" +
                       "page=" + str(page) + "&" + "per_page=" + str(per_page))
    if res.status_code == RATE_LIMIT:
        return None

    for data in res.json():
        items.append(qiita_post_decoder(data))

    return items


"""
get the article object list of the specified user
in descending order of creation date and time
"""


def get_user_items(user_id, page=1, per_page=20):
    items = []
    res = requests.get(qiita + "users/" + user_id +
                       "/items?" + "page=" + str(page) + "&" + "per_page=" + str(per_page))

    if res.status_code == RATE_LIMIT:
        return None

    for data in res.json():
        items.append(qiita_post_decoder(data))

    return items
