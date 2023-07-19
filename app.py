from flask import Flask, request, abort, jsonify
from auth.auth import AuthError, requires_auth
from flask_cors import CORS
from database.models import (
    db_drop_and_create_all,
    populate_db,
    db,
    setup_db,
    Actor,
    Movie,
)
from auth.auth import requires_auth


def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)

    # Uncomment the following line on the initial run to setup
    # the required tables in the database
    db_drop_and_create_all()
    populate_db(app)

    CORS(app, resources={r"/*": {"origins": "*"}})

    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type, Authorization"
        )
        response.headers.add(
            "Access-Control-Allow-Methods", "GET, POST, PATCH, DELETE, OPTIONS"
        )
        return response

    @app.route("/")
    def health():
        return jsonify({"health": "Running!!"}), 200

    @app.route("/actors", methods=["GET"])
    @requires_auth("get:actors")
    def get_actors(payload):
        all_actors = Actor.query.all()
        actors = [actor.short() for actor in all_actors]
        return jsonify({"success": True, "actors": actors}), 200

    @app.route("/actors/<int:actor_id>")
    @requires_auth("get:actors")
    def get_actor(payload, actor_id):
        # Logic to retrieve actor by ID
        # Replace this with your own implementation

        actor = Actor.query.get_or_404(actor_id)

        return jsonify(
            {
                "actor_id": actor.id,
                "name": actor.name,
                "age": actor.age,
                "gender": actor.gender,
            }
        )

    @app.route("/actors", methods=["POST"])
    @requires_auth("post:actors")
    def add_actor(payload):
        # Logic to add a new actor

        name = request.json.get("name")
        age = request.json.get("age")
        gender = request.json.get("gender")

        actor = Actor(name=name, age=age, gender=gender)
        db.session.add(actor)
        db.session.commit()

        return jsonify({"success": True, "message": "Actor added successfully"}), 201

    @app.route("/actors/<int:actor_id>", methods=["PATCH"])
    @requires_auth("patch:actors")
    def update_actor(payload, actor_id):
        # Logic to update the actor

        actor = Actor.query.get_or_404(actor_id)

        # Update the actor attributes
        name = request.json.get("name")
        age = request.json.get("age")
        gender = request.json.get("gender")

        if name:
            actor.name = name
        if age:
            actor.age = age
        if gender:
            actor.gender = gender

        # Save the changes to the database
        db.session.commit()

        return jsonify({"success": True, "message": "Actor updated successfully"}), 200

    @app.route("/actors/<int:actor_id>", methods=["DELETE"])
    @requires_auth("delete:actors")
    def delete_actor(payload, actor_id):
        # Logic to delete the actor

        actor = Actor.query.get_or_404(actor_id)

        db.session.delete(actor)
        db.session.commit()

        return jsonify({"success": True, "message": "Actor deleted successfully"}), 200

    @app.route("/movies")
    @requires_auth("get:movies")
    def get_movies(payload):
        movies_query = Movie.query.order_by(Movie.id).all()
        movies = [movie.short() for movie in movies_query]

        return jsonify({"success": True, "movies": movies}), 200

    @app.route("/movies", methods=["POST"])
    @requires_auth("post:movies")
    def add_movies(payload):
        try:
            # Logic to add a new movie

            title = request.json.get("title")
            release_year = request.json.get("release_year")
            duration = request.json.get("duration")
            imdb_rating = request.json.get("imdb_rating")

            movie = Movie(
                title=title,
                release_year=release_year,
                duration=duration,
                imdb_rating=imdb_rating,
            )
            db.session.add(movie)
            db.session.commit()

            return (
                jsonify({"success": True, "message": "Movie added successfully"}),
                201,
            )

        except Exception as e:
            db.session.rollback()
            return jsonify({"success": False, "error": str(e)}), 500

    @app.route("/movies/<int:movie_id>", methods=["PATCH"])
    @requires_auth("patch:movies")
    def update_movie(payload, movie_id):
        movie = Movie.query.get_or_404(movie_id)

        try:
            request_body = request.get_json()
            if not bool(request_body):
                raise TypeError

            if "title" in request_body:
                if request_body["title"] == "":
                    raise ValueError

                movie.title = request_body["title"]

            if "release_year" in request_body:
                if request_body["release_year"] <= 0:
                    raise ValueError

                movie.release_year = request_body["release_year"]

            if "duration" in request_body:
                if request_body["duration"] <= 0:
                    raise ValueError

                movie.duration = request_body["duration"]

            if "imdb_rating" in request_body:
                if request_body["imdb_rating"] < 0 or request_body["imdb_rating"] > 10:
                    raise ValueError

                movie.imdb_rating = request_body["imdb_rating"]

            if "cast" in request_body:
                if len(request_body["cast"]) == 0:
                    raise ValueError

                actors = Actor.query.filter(Actor.name.in_(request_body["cast"])).all()

                if len(request_body["cast"]) == len(actors):
                    movie.cast = actors
                else:
                    raise ValueError

            movie.update()

            return jsonify({"success": True, "movie_info": movie.long()}), 200

        except (TypeError, ValueError, KeyError):
            abort(422)

        except Exception:
            abort(500)

    @app.route("/movies/<int:movie_id>", methods=["DELETE"])
    @requires_auth("delete:movies")
    def delete_movie(payload, movie_id):
        movie = Movie.query.get_or_404(movie_id)

        try:
            movie.delete()

            return jsonify({"success": True, "deleted_movie_id": movie.id}), 200

        except Exception:
            abort(500)

    @app.errorhandler(422)
    def unprocessable(error):
        return (
            jsonify({"success": False, "error": 422, "message": "Unprocessable"}),
            422,
        )

    @app.errorhandler(404)
    def not_found_error(error):
        return (
            jsonify({"success": False, "error": 404, "message": "Resource not found"}),
            404,
        )

    @app.errorhandler(AuthError)
    def handle_auth_error(error):
        response = {
            "success": False,
            "error": error.status_code,
            "message": error.error["description"],
        }
        return jsonify(response), error.status_code

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({"success": False, "error": 401, "message": "Unauthorized"}), 401

    @app.errorhandler(500)
    def internal_server_error(error):
        return (
            jsonify(
                {"success": False, "error": 500, "message": "Internal Server Error"}
            ),
            500,
        )

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({"success": False, "error": 400, "message": "Bad Request"}), 400

    @app.errorhandler(405)
    def method_not_allowed(error):
        return (
            jsonify({"success": False, "error": 405, "message": "Method Not Allowed"}),
            405,
        )

    return app


app = create_app()
