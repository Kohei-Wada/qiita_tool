class QiitaLGTM:
    def __init__(self, created_at, user):
        self.ceated_at = created_at
        self.user = user

    def get_user(self):
        return self.user