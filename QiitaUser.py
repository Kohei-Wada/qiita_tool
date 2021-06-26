class QiitaUser:

    def __init__(self, description, facebook_id, followers_count, followees_count,
                 github_login_name, user_id, items_count, linkedin_id, location, name, organization,
                 permanent_id, profile_image_url, team_only, twitter_screen_name, website_url):
        self.description = description                  # self introduction
        self.facebook_id = facebook_id                  # Facebook ID
        self.followees_count = int(followees_count)     # number of users following this user
        self.followers_count = int(followers_count)     # number of users this user is following
        self.github_login_name = github_login_name      # GitHub ID
        self.id = user_id                               # User ID
        self.items_count = int(items_count)             # number of articles published by this user on qiita.com
        self.linkedin_id = linkedin_id                  # Linkin ID
        self.location = location                        # residence
        self.name = name                                # name this user set
        self.organization = organization                # organization to which the user belong
        self.permanent_id = int(permanent_id)           # integer ID assigned to each user
        self.profile_image_url = profile_image_url      # URL of the profile image the user set
        self.team_only = bool(team_only)                # weather it is set to Qiita team dedicated mode
        self.twitter_screen_name = twitter_screen_name  # Twitter screen name
        self.website_url = website_url                  # URL of the website the user set

    ####################################################################################################################
    # getter

    def get_description(self):
        return self.description

    def get_facebook_id(self):
        return self.facebook_id

    def get_followers_count(self):
        return self.followers_count

    def get_followees_count(self):
        return self.followees_count

    def get_github_login_name(self):
        return self.github_login_name

    def get_id(self):
        return self.id

    def get_items_count(self):
        return self.items_count

    def get_linkedin_id(self):
        return self.linkedin_id

    def get_location(self):
        return self.location

    def get_name(self):
        return self.name

    def get_organization(self):
        return self.organization

    def get_permanent_id(self):
        return self.permanent_id

    def get_profile_image_url(self):
        return self.profile_image_url

    def get_team_only(self):
        return self.team_only

    def get_twitter_screen_name(self):
        return self.twitter_screen_name

    def get_website_url(self):
        return self.website_url

    ####################################################################################################################
    def get_github_url(self):
        if self.github_login_name is not None:
            return f"https://github.com/{self.github_login_name}"
        else:
            return None

    def has_github_account(self):
        return self.github_login_name is not None

    def get_item_count(self):
        return self.items_count
