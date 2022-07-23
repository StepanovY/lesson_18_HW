from flask import request
from flask_restx import Resource, Namespace

from dao.model.movies import MovieSchema
from implemented import movies_service

movies_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        all_movies = movies_service.get_all()
        return movies_schema.dump(all_movies), 200

    def post(self):
        req_json = request.json
        movies_service.create(req_json)
        return '', 201


@movies_ns.route('/<int:mid>')
class MoviesView(Resource):
    def get(self, mid):
        movie = movies_service.get_one(mid)
        return movie_schema.dump(movie), 200

    def put(self, mid):
        req_json = request.json
        req_json['id'] = mid
        movies_service.update(req_json)
        return '', 204

    def patch(self, mid: int):
        req_json = request.json
        req_json['id'] = mid
        movies_service.update_partial(req_json)
        return '', 204

    def delete(self, mid):
        movies_service.delete(mid)
        return '', 204
