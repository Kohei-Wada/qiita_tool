class QiitaUser:

    def __init__(self, description, facebook_id, followers_count, followees_count,
                 github_login_name, user_id, items_count, linkedin_id, location, name, organization,
                 permanent_id, profile_image_url, team_only, twitter_screen_name, website_url):

        self.description = description  # self introduction
        self.facebook_id = facebook_id  # Facebook ID
        self.followers_count = int(followers_count)  # number of users this user is following
        self.followees_count = int(followees_count)  # number of users following this user
        self.github_login_name = github_login_name  # GitHub ID
        self.id = user_id  # User ID
        self.items_count = int(items_count)  # number of articles published by this user on qiita.com
        self.linkedin_id = linkedin_id  # Linkin ID
        self.location = location  # residence
        self.name = name  # name this user set
        self.organization = organization  # organization to which the user belong
        self.permanent_id = int(permanent_id)  # integer ID assigned to each user
        self.profile_image_url = profile_image_url  # URL of the profile image the user set
        self.team_only = bool(team_only)  # weather it is set to Qiita team dedicated mode
        self.twitter_screen_name = twitter_screen_name  # Twitter screen name
        self.website_url = website_url  # URL of the website the user set

    # if the user set github account return true
    def has_github_account(self):
        return self.github_login_name is not None
