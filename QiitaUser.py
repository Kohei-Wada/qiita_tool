class QiitaUser:

    def __init__(self):
        self.description = ""  # self introduction
        self.facebook_id = ""  # Facebook ID
        self.followers_count = 0  # number of users this user is following
        self.followees_count = 0  # number of users following this user
        self.github_login_name = ""  # GitHub ID
        self.id = ""  # User ID
        self.items_count = ""  # number of articles published by this user on qiita.com
        self.linkedin_id = ""  # Linkein ID
        self.location = ""  # residence
        self.name = ""  # name this user set
        self.organization = ""  # organization to which the user belong
        self.permanent_id = -1  # integer ID assgned to each user
        self.profile_image_url = ""  # URL of the profile image the user set
        self.team_only = False  # weather it is set to Qiita team dedicated mode
        self.twitter_screen_name = ""  # Twitter screen name
        self.website_url = ""  # URL of the website the user set
