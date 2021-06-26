from Qiita.QiitaUser import QiitaUser
from Qiita.QiitaComment import QiitaComment
from Qiita.QiitaPost import QiitaPost
from Qiita.QiitaTag import QiitaTag
from Qiita.QiitaLGTM import QiitaLGTM


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


def qiita_comment_decoder(obj):
    return QiitaComment(obj['body'],
                        obj['created_at'],
                        obj['id'],
                        obj['rendered_body'],
                        obj['updated_at'],
                        qiita_user_decoder(obj['user']))


def qiita_tag_decoder(obj):
    return QiitaTag(obj['followers_count'],
                    obj['icon_url'],
                    obj['id'],
                    obj['items_count'])


def qiita_post_decoder(obj):
    return QiitaPost(obj['rendered_body'],
                     obj['body'],
                     obj['coediting'],
                     obj['comments_count'],
                     obj['created_at'],
                     obj['group'],
                     obj['id'],
                     obj['likes_count'],
                     obj['private'],
                     obj['reactions_count'],
                     obj['tags'],
                     obj['title'],
                     obj['updated_at'],
                     obj['url'],
                     qiita_user_decoder(obj['user']),
                     obj['page_views_count'],
                     obj['team_membership'])


def qiita_lgtm_decoder(obj):
    return QiitaLGTM(obj['created_at'],
                     qiita_user_decoder(obj['user']))
