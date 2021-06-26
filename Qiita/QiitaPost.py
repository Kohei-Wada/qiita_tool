class QiitaPost:
    def __init__(self, rendered_body, body, coediting, comments_count,
                 created_at, group, comment_id, likes_count, private, reactions_count,
                 tags, title, updated_at, url, user, page_views_count, team_membership):
        self.rendered_body = rendered_body             # HTML body
        self.body = body                               # Markdown format text
        self.coediting = bool(coediting)               # Whether this articles is in co-update status
        self.comments_count = int(comments_count)      # number of comments on this article
        self.created_at = created_at                   # date and time when the date was created
        self.group = group                             # represents a group of Qiita team
        self.id = comment_id                           # unique ID of the article
        self.likes_count = int(likes_count)            # number of "LGTM!" to this article
        self.private = bool(private)                   # flag indicating weather it is in the limited sharing state
        self.reactions_count = int(reactions_count)    # number of emoji reactions
        self.tags = tags                               # list of QiitaTag object
        self.title = title                             # article title
        self.updated_at = updated_at                   # the date and time when the data was last updated
        self.url = url                                 # Article URL
        self.user = user                               # QiitaUser object
        self.page_views_count = page_views_count       # number of views
        self.team_membership = team_membership         # represents team member information for Qiita Team

    ####################################################################################################################
    # getter

    def get_rendered_body(self):
        return self.rendered_body

    def get_body(self):
        return self.body

    def get_coediting(self):
        return self.coediting

    def get_comments_count(self):
        return self.comments_count

    def get_created_at(self):
        return self.created_at

    def get_group(self):
        return self.group

    def get_id(self):
        return self.id

    def get_likes_count(self):
        return self.likes_count

    def get_private(self):
        return self.private

    def get_reactions_count(self):
        return self.reactions_count

    def get_tags(self):
        return self.tags

    def get_title(self):
        return self.title

    def get_updated_at(self):
        return self.updated_at

    def get_url(self):
        return self.url

    def get_user(self):
        return self.user

    def get_page_views_count(self):
        return self.page_views_count

    def get_team_member_ship(self):
        return self.team_membership
