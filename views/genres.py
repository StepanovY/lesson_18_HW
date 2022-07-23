from flask_restx import Resource, Namespace

from dao.model.genres import GenreSchema
from implemented import genres_service

genres_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genres_ns.route('/')
class GenresViews(Resource):
    def get(self):
        all_genres = genres_service.get_all()
        return genres_schema.dump(all_genres), 200


@genres_ns.route('/<int:gid>')
class GenresViews(Resource):
    def get(self, gid):
        genre = genres_service.get_one(gid)
        return genre_schema.dump(genre), 200
