from dao.model.directors import DirectorSchema, Director
from dao.model.genres import GenreSchema, Genre
from setup_db import db
from marshmallow import Schema, fields


class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    trailer = db.Column(db.String(255))
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey(Genre.id))
    genre = db.relationship(Genre)
    director_id = db.Column(db.Integer, db.ForeignKey(Director.id))
    director = db.relationship(Director)


class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()

    genre = fields.Pluck(GenreSchema, 'name')
    director = fields.Pluck(DirectorSchema,'name')
