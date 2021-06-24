class QiitaTag:
    def __init__(self, followers_count, icon_url, tag_id, items_count):
        self.followers_count = int(followers_count)
        self.icon_url = icon_url
        self.id = tag_id
        self.items_count = int(items_count)

    def get_followers_count(self):
        return self.followers_count

    def get_icon_url(self):
        return self.icon_url

    def get_id(self):
        return self.id

    def get_items_count(self):
        return self.items_count
