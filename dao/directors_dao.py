from dao.model.directors import Director


class DirectorsDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        return self.session.query(Director).get(mid)

    def get_all(self):
        return self.session.query(Director).all()
