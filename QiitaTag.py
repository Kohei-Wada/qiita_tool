class QiitaTag:
    def __init__(self, followers_count, icon_url, tag_id, items_count):
        self.followers_count = int(followers_count)  # number of users following tag
        self.icon_url = icon_url                     # URL to the icon image set in this tag
        self.id = tag_id                             # unique ID of the tag
        self.items_count = int(items_count)          # number of articles tagged with this tag

    ###################################################################################################################
    # getter

    def get_followers_count(self):
        return self.followers_count

    def get_icon_url(self):
        return self.icon_url

    def get_id(self):
        return self.id

    def get_items_count(self):
        return self.items_count
