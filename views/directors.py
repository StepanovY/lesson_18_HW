from flask_restx import Resource, Namespace

from dao.model.directors import DirectorSchema
from implemented import directors_service

directors_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@directors_ns.route('/')
class DirectorsViews(Resource):
    def get(self):
        all_directors = directors_service.get_all()
        return directors_schema.dump(all_directors), 200


@directors_ns.route('/<int:did>')
class DirectorsViews(Resource):
    def get(self, did):
        director = directors_service.get_one(did)
        return director_schema.dump(director), 200
