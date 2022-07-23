from dao.directors_dao import DirectorsDAO
from dao.genres_dao import GenresDAO
from dao.movies_dao import MoviesDAO
from service.directors import DirectorsService
from service.genres import GenresService
from service.movies import MoviesService
from setup_db import db

movies_dao = MoviesDAO(session=db.session)
movies_service = MoviesService(dao=movies_dao)

directors_dao = DirectorsDAO(session=db.session)
directors_service = DirectorsService(dao=directors_dao)

genres_dao = GenresDAO(session=db.session)
genres_service = GenresService(dao=genres_dao)
