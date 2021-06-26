class QiitaComment:
    def __init__(self, body, created_at, comment_id, rendered_body,
                 updated_at, user):
        self.body = body                  # Markdown format string representing the content of the comment
        self.created_at = created_at      # Date and time when the data was created
        self.id = comment_id              # unique ID of the comment
        self.render_body = rendered_body  # HTML format string representing the content of the comment
        self.updated_at = updated_at      # Date and time when the data was last updated
        self.user = user                  # qiita user object

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
