import sys
import json
import requests
import inspect
from Qiita.decoders import *

# this class is wrapper for Qiita API


qiita = "https://qiita.com/api/v2/"

OK = 200
SUCCESS = 204
RATE_LIMIT = 403


##################################################################################################################
# control debug error logging

def error(msg):
    sys.stderr.write(f"{msg}")


def log(msg, flag=False):
    if flag:
        sys.stderr.write(f"{msg}")


##################################################################################################################
# LGTM


def get_item_lgtm(item_id):
    """
    get a list of "LGTM!" that attached article in descending order
    :param item_id: unique ID of the "LGTM!"
    :return:
    """

    lgtms = []
    res = requests.get(qiita + "items/" + item_id + "/likes")
    if res.status_code == RATE_LIMIT:
        error(f"{inspect.currentframe().f_code.co_name}: late limit.")
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


def delete_comment(comment_id):
    """
    delete the comment
    :param comment_id: unique ID of the comment
    :return: bool
    """

    requests.delete(qiita + "comments/" + comment_id)
    return


def get_comment(comment_id):
    """
    get a comment object
    :param comment_id: unique ID of the comment
    :return: QiitaComment object
    """
    res = requests.get(qiita + "comments/" + comment_id)

    if res.status_code == RATE_LIMIT:
        error(f"{inspect.currentframe().f_code.co_name}: late limit.")
        return None

    return json.loads(res.text, object_hook=qiita_comment_decoder)


def get_item_comments(item_id):
    """
    get the list of comment object attached to the item.

    :param item_id: unique ID of the article
    :return: list of QiitaComment objects
    """
    comments = []
    res = requests.get(qiita + "items/" + item_id + "/comments")

    if res.status_code == RATE_LIMIT:
        error(f"{inspect.currentframe().f_code.co_name}: late limit.")
        return None

    for data in res.json():
        comments.append(qiita_comment_decoder(data))

    return comments


##################################################################################################################
# TAGGING

##################################################################################################################
# TAG


def get_all_tags(page=1, per_page=20):
    """
    get the QiitaTag objects list in descending order
    of creation date and time.

    :param page: index of page
    :param per_page: number of QiitaTag objects  per page
    :return: list of QiitaTag objects
    """

    if page < 0 or page > 100:
        page = 20

    if per_page < 0 or per_page > 100:
        per_page = 20

    tags = []
    res = requests.get(qiita + "tags?" +
                       "page=" + str(page) + "&" + "per_page=" + str(per_page))
    if res.status_code == RATE_LIMIT:
        error(f"{inspect.currentframe().f_code.co_name}: late limit.")
        return None

    for data in res.json():
        tags.append(qiita_tag_decoder(data))

    return tags


def get_tag(tag_id):
    """
    get QiitaTag object
    :param tag_id: unique ID of the tag
    :return: QiitaTag object
    """

    res = requests.get(qiita + "tags/" + tag_id)
    if res.status_code == RATE_LIMIT:
        error(f"{inspect.currentframe().f_code.co_name}: late limit.")

        return None

    return json.loads(res.text, object_hook=qiita_tag_decoder)


def get_following_tags(user_id, page=1, per_page=20):
    """
    get the list of tag object that is followed by user

    :param user_id: unique ID of the user
    :param page: index of the page
    :param per_page: number of QiitaTag objects per page
    :return: list of QiitaTag object
    """
    if page < 0 or page > 100:
        page = 20

    if per_page < 0 or per_page > 100:
        per_page = 20

    tags = []
    res = requests.get(qiita + "users/" + user_id + "/following_tags?" +
                       "page=" + str(page) + "&" + "per_page=" + str(per_page))

    if res.status_code == RATE_LIMIT:
        error(f"{inspect.currentframe().f_code.co_name}: late limit.")
        return None

    for data in res.json():
        tags.append(qiita_tag_decoder(data))

    return tags


def unfollow_tag(tag_id):
    """
    unfollow the tag. if successful , return true.

    :param tag_id: unique ID of the tag
    :return: bool
    """
    res = requests.delete(qiita + "tags/" + tag_id + "/following")
    return res.status_code == SUCCESS


def follow_tag(tag_id):
    """
    follow the tag. if successful , return true.

    :param tag_id: unique ID of the tag
    :return: bool
    """

    res = requests.put(qiita + "tags/" + tag_id + "following")
    return res.status_code == SUCCESS


##################################################################################################################
# TEAM

##################################################################################################################
# PROJECT

##################################################################################################################
# USER


def get_stockers(item_id, page=1, per_page=20):
    """
    get the list of QiitaUser object that have stocked articles
    int descending order of stock date and time.

    :param item_id: unique ID of the article
    :param page: index of the page
    :param per_page: list of QiitaUser objects
    :return:
    """
    if page < 0 or page > 100:
        page = 20

    if per_page < 0 or per_page > 100:
        per_page = 20

    stockers = []
    res = requests.get(qiita + "items/" + item_id + "/stockers?" +
                       "page=" + str(page) + "&" + "per_page=" + str(per_page))

    if res.status_code == RATE_LIMIT:
        error(f"{inspect.currentframe().f_code.co_name}: late limit.")
        return None

    for data in res.json():
        stockers.append(qiita_user_decoder(data))

    return stockers


def get_users(page=1, per_page=20):
    """
    get the list of QiitaUser object in descending order
    of creation date and time.

    :param page: index of a page
    :param per_page: number of QiitaUser objects per page
    :return: list of QiitaUser objects
    """
    if page < 0 or page > 100:
        page = 20

    if per_page < 0 or per_page > 100:
        per_page = 20

    users = []
    res = requests.get(qiita + "users?" +
                       "page=" + str(page) + "&" + "per_page=" + str(per_page))

    if res.status_code == RATE_LIMIT:
        error(f"{inspect.currentframe().f_code.co_name}: late limit.")
        return None
    for data in res.json():
        users.append(qiita_user_decoder(data))
    return users


def get_user(user_id):
    """
    get the QiitaUser object
    :param user_id: unique ID of the user
    :return: QiitaUser object
    """
    res = requests.get(qiita + "users/" + user_id)
    if res.status_code == RATE_LIMIT:
        error(f"{inspect.currentframe().f_code.co_name}: late limit.")
        return None

    return json.loads(res.text, object_hook=qiita_user_decoder)


def get_followees(user_id, page=1, per_page=20):
    """
    get the list of QiitaUser objects that is followed by the user

    :param user_id: unique ID of the user
    :param page: index of the page
    :param per_page: number of QiitaUser objects per page
    :return: list of QiitaUser objects
    """
    if page < 0 or page > 100:
        page = 20

    if per_page < 0 or per_page > 100:
        per_page = 20

    followees = []
    res = requests.get(qiita + "users/" + user_id + "/followees?" +
                       "page=" + str(page) + "&" + "per_page=" + str(per_page))
    if res.status_code == RATE_LIMIT:
        error(f"{inspect.currentframe().f_code.co_name}: late limit.")
        return None

    for data in res.json():
        followees.append(qiita_user_decoder(data))
    return followees


def get_followers(user_id, page=1, per_page=20):
    """
    get the list of QiitaUser objects that is following the user

    :param user_id: unique ID of the user
    :param page: index of the page
    :param per_page: number of QiitaUser objects per page
    :return: list of QiitaUser objects
    """
    if page < 0 or page > 100:
        page = 20

    if per_page < 0 or per_page > 100:
        per_page = 20

    followers = []
    res = requests.get(qiita + "users/" + user_id + "/followers?" +
                       "page=" + str(page) + "&" + "per_page" + str(per_page))

    if res.status_code == RATE_LIMIT:
        error(f"{inspect.currentframe().f_code.co_name}: late limit.")
        return None

    for data in res.json():
        followers.append(qiita_user_decoder(data))
    return followers


def unfollow(user_id):
    """
    unfollow the user. if successful, return true.
    :param user_id: unique ID of the user
    :return: bool
    """
    res = requests.delete(qiita + "users/" + user_id + "/following")
    return res.status_code == SUCCESS


def is_following():
    return


def follow(user_id):
    """
    follow the user. if successful, return true.
    :param user_id: unique ID of the user
    :return: bool
    """

    res = requests.put(qiita + "users/" + user_id + "/following")
    return res.status_code == SUCCESS


##################################################################################################################
# POST(ITEM) : represents a post from a user


def get_items(page=1, per_page=20):
    """
    get the list of article object in descending order
    of creation date and time.
    :param page: index of the page
    :param per_page: number of QiitaPost objects per page
    :return: list of QiitaPost objects
    """
    if page < 0 or page > 100:
        page = 20

    if per_page < 0 or per_page > 100:
        per_page = 20

    items = []
    res = requests.get(qiita + "items?" +
                       "page=" + str(page) + "&" + "per_page=" + str(per_page))
    if res.status_code == RATE_LIMIT:
        error(f"{inspect.currentframe().f_code.co_name}: late limit.")
        return None

    for data in res.json():
        items.append(qiita_post_decoder(data))

    return items


def get_user_items(user_id, page=1, per_page=20):
    """
    get the article object list of the specified user
    in descending order of creation date and time

    :param user_id: unique ID of the user
    :param page: index of the page
    :param per_page: number of QiitaPost objects per page
    :return: list of QiitaPost objects
    """
    if page < 0 or page > 100:
        page = 20

    if per_page < 0 or per_page > 100:
        per_page = 20

    items = []
    res = requests.get(qiita + "users/" + user_id +
                       "/items?" + "page=" + str(page) + "&" + "per_page=" + str(per_page))

    if res.status_code == RATE_LIMIT:
        error(f"{inspect.currentframe().f_code.co_name}: late limit.")
        return None

    for data in res.json():
        items.append(qiita_post_decoder(data))

    return items
