class QiitaComment:
    def __init__(self, body, created_at, comment_id, rendered_body,
                 updated_at, user):
        self.body = body
        self.created_ad = created_at
        self.id = comment_id
        self.render_body = rendered_body
        self.updated_at = updated_at
        self.user = user

    def get_user(self):
        return self.user
