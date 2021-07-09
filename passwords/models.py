import uuid

class Password:

    def __init__(self, app, user, password, notes, uid=None):
        self.app = app
        self.user = user
        self.password = password
        self.notes = notes
        self.uid = uid or uuid.uuid4()

    def to_dict(self):
        return vars(self)

    @staticmethod
    def schema():
        return ['app', 'user', 'password', 'notes', 'uid']