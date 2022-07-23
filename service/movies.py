from dao.movies_dao import MoviesDAO


class MoviesService:
    def __init__(self, dao: MoviesDAO):
        self.dao = dao

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        self.dao.create(data)

    def update(self, data):
        mid = data.get('id')

        movie = self.get_one(mid)

        movie.id = data.get('id')
        movie.title = data.get('title')
        movie.description = data.get('description')
        movie.trailer = data.get('trailer')
        movie.year = data.get('year')
        movie.rating = data.get('rating')
        movie.director = data.get('director')
        movie.genre = data.get('genre')

        self.dao.update(movie)

    def update_partial(self, data):
        mid = data.get('id')

        movie = self.get_one(mid)

        if 'id' in data:
            movie.id = data.get('id')
        if 'title' in data:
            movie.title = data.get('title')
        if 'description' in data:
            movie.description = data.get('description')
        if 'trailer' in data:
            movie.trailer = data.get('trailer')
        if 'year' in data:
            movie.year = data.get('year')
        if 'rating' in data:
            movie.rating = data.get('rating')
        if 'director' in data:
            movie.director = data.get('director')
        if 'genre' in data:
            movie.genre = data.get('genre')

        self.dao.update(movie)

    def delete(self, mid):
        return self.dao.delete(mid)
