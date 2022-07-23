from dao.genres_dao import GenresDAO


class GenresService:
    def __init__(self, dao: GenresDAO):
        self.dao = dao

    def get_one(self, gid):
        return self.dao.get_one(gid)

    def get_all(self):
        return self.dao.get_all()
