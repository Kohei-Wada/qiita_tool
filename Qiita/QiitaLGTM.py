class QiitaLGTM:
    def __init__(self, created_at, user):
        self.created_at = created_at  # date and time when the data was created
        self.user = user              # qiita user object

    ####################################################################################################################
    # getter

    def get_created_at(self):
        return self.created_at

    def get_user(self):
        return self.user
