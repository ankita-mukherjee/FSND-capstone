from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship, sessionmaker
from flask_sqlalchemy import SQLAlchemy
import os

# database_filename = "database.db"
# project_dir = os.path.dirname(os.path.abspath(__file__))
# database_path = "sqlite:///{}".format(os.path.join(project_dir, database_filename))
database_path = os.environ["DATABASE_URL"]
db = SQLAlchemy()


def setup_db(app):
    """binds a flask application and a SQLAlchemy service"""
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)


def db_drop_and_create_all():
    """
    drops the database tables and starts fresh
    can be used to initialize a clean database
    """
    db.drop_all()
    db.create_all()


def populate_db(app):
    with app.app_context():
        Session = sessionmaker(bind=db.engine)
        session = Session()
        # Create an entry in the actors table
        actor = Actor(name="John Doe", age=30, gender="Male")
        session.add(actor)

        # Create an entry in the movies table
        movie = Movie(
            title="Example Movie", release_year=2023, duration=120, imdb_rating=7.5
        )
        session.add(movie)

        # Commit the changes to the database
        session.commit()


actor_in_movie = db.Table(
    "actor_in_movie",
    Column("actor_id", Integer, ForeignKey("actors.id"), primary_key=True),
    Column("movie_id", Integer, ForeignKey("movies.id"), primary_key=True),
)


class Movie(db.Model):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True)
    title = Column(String(256), nullable=False)
    release_year = Column(Integer, nullable=False)
    duration = Column(Integer, nullable=False)
    imdb_rating = Column(Float, nullable=False)
    cast = relationship("Actor", secondary=actor_in_movie, backref="movies", lazy=True)

    def __init__(self, title, release_year, duration, imdb_rating):
        self.title = title
        self.release_year = release_year
        self.duration = duration
        self.imdb_rating = imdb_rating

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def short(self):
        return {"id": self.id, "title": self.title, "release_year": self.release_year}

    def long(self):
        return {
            "title": self.title,
            "duration": self.duration,
            "release_year": self.release_year,
            "imdb_rating": self.imdb_rating,
        }

    def full_info(self):
        return {
            "title": self.title,
            "duration": self.duration,
            "release_year": self.release_year,
            "imdb_rating": self.imdb_rating,
            "cast": [actor.name for actor in self.cast],
        }

    def __repr__(self):
        return "<Movie {} {} {} {} />".format(
            self.title, self.release_year, self.imdb_rating, self.duration
        )


class Actor(db.Model):
    __tablename__ = "actors"

    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String(256), nullable=False)

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def short(self):
        return {"id": self.id, "name": self.name}

    def long(self):
        return {
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
        }

    def full_info(self):
        return {
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "movies": [movie.title for movie in self.movies],
        }

    def __repr__(self):
        return "<Actor {} {} {} />".format(self.name, self.age, self.gender)
