# Casting Agency API

## Capstone Project for Udacity's Full Stack Developer Nanodegree
Heroku Link: https://capstone-development.onrender.com

While running locally: http://localhost:5000

## Getting Started

### Installing Dependencies

#### Python 3.7.11

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python).

#### OPTIONAL - Create a Virtual environment

Recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).

python3 -m venv myvenv
source myvenv/bin/activate

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

## Running the server

To run the server, execute:

```bash
export FLASK_APP=app.py
flask run --reload
```

Setting the `FLASK_APP` variable to `app.py` directs flask to use the `app.py` file to find the application. 

Using the `--reload` flag will detect file changes and restart the server automatically.

## API Reference

## Getting Started
Base URL: This application can be run locally. The hosted version is at `https://ry-fsnd-capstone.herokuapp.com`.

Authentication: This application requires authentication to perform various actions. All the endpoints require
various permissions, except the root (or health) endpoint, that are passed via the `Bearer` token.

The application has three different types of roles:
- User
  - can only view the list of artist and movies and can view complete information for any actor or movie
  - has `get:actors, get:actors-info, get:movies, get:movies-info` permissions
- Manager
  - can perform all the actions that `User` can
  - can also create an actor and movie and also update respective information
  - has `patch:actor, patch:movie, post:actor, post:movie` permissions in addition to all the permissions that `User` role has
- Admin
  - can perform all the actions that `Manager` can
  - can also delete an actor or a movie
  - has `delete:actor, delete:movie` permissions in addition to all the permissions that `Manager` role has


## Error Handling
Errors are returned as JSON objects in the following format:
```
{
    "error": 404,
    "message": "The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.",
    "success": false
}
```

The API will return the following errors based on how the request fails:
 - 400: Bad Request
 - 401: Unauthorized
 - 403: Forbidden
 - 404: Not Found
 - 405: Method Not Allowed
 - 422: Unprocessable Entity
 - 500: Internal Server Error

## Endpoints

#### GET /
 - General
   - root endpoint
   - can also work to check if the api is up and running
   - is a public endpoint, requires no authentication
 
 - Sample Request
   - `https://capstone-development.onrender.com/`

<details>
<summary>Sample Response</summary>

```
{
    "health": "Running!!"
}
```

</details>

#### GET /actors
 - General
   - gets the list of all the actors
   - requires `get:actors` permission
 
 - Sample Request
   - `https://capstone-development.onrender.com/actors`

<details>
<summary>Sample Response</summary>

```
{
    "actors": [
        {
            "id": 1,
            "name": "John Doe"
        }
    ],
    "success": true
}
```

</details>

#### GET /actors/{actor_id}
 - General
   - gets the complete info for an actor
   - requires `get:actors` permission
 
 - Sample Request
   - `https://capstone-development.onrender.com/actors/1`

<details>
<summary>Sample Response</summary>

```
{
    "actor_id": 1,
    "age": 30,
    "gender": "Male",
    "name": "John Doe"
}
```
  
</details>

#### POST /actors
 - General
   - creates a new actor
   - requires `post:actors` permission
 
 - Request Body
   - name: string, required
   - age: Integer, required
   - gender: String, required
 
 - Sample Request
   - `https://capstone-development.onrender.com/actors`
   - Request Body
     ```
        {
         "name": "John Doe",
         "age": 30,
         "gender": "Male"
        }
    
     ```

<details>
<summary>Sample Response</summary>

```

    {
    "message": "Actor added successfully",
    "success": true
    }
  
```
  
</details>

#### PATCH /actors/{actor_id}
 - General
   - updates the info for an actor
   - requires `patch:actors` permission
 
 - Request Body (at least one of the following fields required)
   - name: string, optional
   - age: Integer, optional
   - gender: string, optional
 
 - Sample Request
   - `https://capstone-development.onrender.com/actors/1`
   - Request Body
     ```
      {
        "name": "Merry",
        "age": 20,
        "gender": "Female"
      }

     ```

<details>
<summary>Sample Response</summary>

```
{
    "message": "Actor updated successfully",
    "success": true
}
```
  
</details>

#### DELETE /actors/{actor_id}
 - General
   - deletes the actor
   - requires `delete:actors` permission
   - will also delete the mapping to the movie but will not delete the movie from the database
 
 - Sample Request
   - `https://capstone-development.onrender.com/actors/2`

<details>
<summary>Sample Response</summary>

```
{
    "message": "Actor deleted successfully",
    "success": true
}
```
  
</details>

#### GET /movies
 - General
   - gets the list of all the movies
   - requires `get:movies` permission
 
 - Sample Request
   - `https://capstone-development.onrender.com/movies`

<details>
<summary>Sample Response</summary>

```
{
    "movies": [
        {
            "id": 1,
            "release_year": 2023,
            "title": "Example Movie"
        }
    ],
    "success": true
}
```

</details>


#### POST /movies
 - General
   - creates a new movie
   - requires `post:movies` permission
 
 - Request Body
   - title: string, required
   - duration: integer, required
   - release_year: integer, required
   - imdb_rating: float, required
   - cast: array of string, non-empty, required
 
 - NOTE
   - Actors passed in the `cast` array in request body must already exist in the database prior to making this request.
   - If not, the request will fail with code 422.
 
 - Sample Request
   - `https://capstone-development.onrender.com/movies`
   - Request Body
     ```
      {
        "title": "The Movie",
        "release_year": 2023,
        "duration": 120,
        "imdb_rating": 8.5,
        "cast": ["Actor 1", "Actor 2", "Actor 3"]
      }
     ```

<details>
<summary>Sample Response</summary>

```
{
    "message": "Movie added successfully",
    "success": true
}
```
  
</details>

#### PATCH /movies/<int:movie_id>
 - General
   - updates the info for a movie
   - requires `patch:movies` permission
 
 - Request Body (at least one of the following fields required)
   - title: string, optional
   - duration: integer, optional
   - release_year: integer, optional
   - imdb_rating: float, optional
   - cast: array of string, non-empty, optional
 
 - NOTE
   - Actors passed in the `cast` array in request body will completely replace the existing relationship.
   - So, if you want to append new actors to a movie, pass the existing actors also in the request.
 
 - Sample Request
   - `https://capstone-development.onrender.com/movies/2`
   - Request Body
     ```
      {
        "title": "The Hidden Story",
        "release_year": 2021
      }
     ```

<details>
<summary>Sample Response</summary>

```
{
    "movie_info": {
        "duration": 120,
        "imdb_rating": 8.5,
        "release_year": 2021,
        "title": "The Hidden Story"
    },
    "success": true
}
```
  
</details>

#### DELETE /movies/{movie_id}
 - General
   - deletes the movie
   - requires `delete:movies` permission
   - will not affect the actors present in the database
 
 - Sample Request
   - `https://capstone-development.onrender.com/movies/2`

<details>
<summary>Sample Response</summary>

```
{
    "deleted_movie_id": 2,
    "success": true
}
```
  
</details>