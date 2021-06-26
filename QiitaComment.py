class QiitaComment:
    def __init__(self, body, created_at, comment_id, rendered_body,
                 updated_at, user):
        self.body = body
        self.created_at = created_at
        self.id = comment_id
        self.render_body = rendered_body
        self.updated_at = updated_at
        self.user = user

    ####################################################################################################################
    # getter

    def get_body(self):
        return self.body

    def get_created_at(self):
        return self.created_at

    def get_id(self):
        return self.id

    def get_rendered_body(self):
        return self.render_body

    def get_updated_at(self):
        return self.updated_at

    def get_user(self):
        return self.user
