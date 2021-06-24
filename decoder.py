from QiitaUser import QiitaUser


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

