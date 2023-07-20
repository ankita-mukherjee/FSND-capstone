import unittest
import json
from app import create_app, db
from database.models import Actor, Movie, setup_db
import os


class CastingAgencyTestCase(unittest.TestCase):
    def setUp(self):
        # Set up the database and models
        self.app = create_app()
        self.client = self.app.test_client
        database_filename = "database_test.db"
        project_dir = os.path.dirname(os.path.abspath(__file__))
        database_path = "sqlite:///{}".format(
            os.path.join(project_dir, database_filename)
        )

        with self.app.app_context():
            setup_db(self.app)

        # Set up test data
        self.casting_assistant_token = os.environ["casting_assistant_token"]
        self.casting_director_token = os.environ["casting_director_token"]
        self.executive_producer_token = os.environ["executive_producer_token"]

        self.new_actor = {"name": "Test Actor", "age": 30, "gender": "Male"}

        self.new_movie = {
            "title": "Test Movie",
            "release_year": 2023,
            "duration": 120,
            "imdb_rating": 8.5,
        }

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    # Helper methods for authentication headers
    def casting_assistant_headers(self):
        return {"Authorization": "Bearer " + self.casting_assistant_token}

    def casting_director_headers(self):
        return {"Authorization": "Bearer " + self.casting_director_token}

    def executive_producer_headers(self):
        return {"Authorization": "Bearer " + self.executive_producer_token}

    # Test cases for error behavior of each endpoint
    def test_404_get_actors_with_invalid_id(self):
        # Try to get an actor with an invalid ID (999) that does not exist
        res = self.client().get("/actors/999", headers=self.casting_assistant_headers())
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data["success"])
        self.assertEqual(data["message"], "Resource not found")

    def test_404_get_movies(self):
        # Try to get all movies with an invalid URL
        res = self.client().get("/movies/999", headers=self.casting_assistant_headers())
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data["success"])
        self.assertEqual(data["message"], "Resource not found")

    def test_404_get_movies_with_invalid_id(self):
        # Try to get a movie with an invalid ID (999) that does not exist
        res = self.client().get("/movies/999", headers=self.casting_assistant_headers())
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data["success"])
        self.assertEqual(data["message"], "Resource not found")

    def test_create_actor(self):
        # Casting Director should have permission to add an actor
        res = self.client().post(
            "/actors", headers=self.casting_director_headers(), json=self.new_actor
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 201)  # Corrected to 201 (Created)
        self.assertTrue(data["success"])

    def test_create_movie(self):
        # Executive Producer should have permission to add a movie
        res = self.client().post(
            "/movies", headers=self.executive_producer_headers(), json=self.new_movie
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 201)
        self.assertTrue(data["success"])

    # Test cases for error behavior of each endpoint
    def test_404_get_actors(self):
        res = self.client().get("/actors/999", headers=self.casting_assistant_headers())
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data["success"])

    def test_404_get_movies(self):
        # Try to get all movies with an invalid URL
        res = self.client().get("/movies/999", headers=self.casting_assistant_headers())
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertFalse(data["success"])

    def test_404_get_movies_with_invalid_id(self):
        # Try to get a movie with an invalid ID (999) that does not exist
        res = self.client().get("/movies/999", headers=self.casting_assistant_headers())
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertFalse(data["success"])

    def test_create_actor_without_permission(self):
        # Casting Assistant should not have permission to add an actor
        res = self.client().post(
            "/actors", headers=self.casting_assistant_headers(), json=self.new_actor
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data["success"])

    def test_casting_director_modify_actor(self):
        # Casting Director should have permission to modify an actor
        res = self.client().patch(
            "/actors/1",
            headers=self.casting_director_headers(),
            json={"name": "Updated Actor Name"},
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])

    def test_executive_producer_permissions(self):
        # Executive Producer should have permission to delete a movie
        res = self.client().delete(
            "/movies/1", headers=self.executive_producer_headers()
        )
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)  # Corrected to 200 (OK)
        self.assertTrue(data["success"])


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
