
class QiitaPost:
    def __init__(self, rendered_body, body, coediting, comments_count,
                 created_at, group, comment_id, likes_count, private, reactions_count,
                 tags, title, updated_at, url, user, page_views_count, team_membership):
        self.rendered_body = rendered_body
        self.body = body
        self.coediting = coediting
        self.comments_count = int(comments_count)
        self.created_at = created_at
        self.group = group
        self.id = comment_id
        self.likes_count = int(likes_count)
        self.private = private
        self.reactions_count = reactions_count
        self.tags = tags
        self.title = title
        self.updated_at = updated_at
        self.url = url
        self.user = user
        self.page_views_count = page_views_count
        self.team_membership = team_membership

    def get_id(self):
        return self.id

    def get_user(self):
        return self.user

    def get_url(self):
        return self.url

    def get_likes_count(self):
        return self.likes_count

    def get_tag(self):
        return self.tags
