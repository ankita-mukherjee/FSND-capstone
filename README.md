# Casting Agency API
**Introduction & Motivation:**

Welcome to the README section of the Casting Agency API! This document provides an overview of the project's specifications, goals, and the motivation behind its development.

*General Specifications:*

The Casting Agency API is designed to manage and streamline the process of creating movies and assigning actors to those movies. It adheres to the following general specifications:

Models: The API includes two classes, "Movies" and "Actors," with primary keys having at least two attributes each. Additionally, it encourages the implementation of one-to-many or many-to-many relationships between these classes.

Endpoints: The API exposes several endpoints to interact with the data. These include at least two GET requests, one POST request, one PATCH request, and one DELETE request for both "actors" and "movies."

Roles: The system defines three distinct roles: "Casting Assistant," "Casting Director," and "Executive Producer," each with different permissions. Permissions are specified for all endpoints, providing role-based access control (RBAC).

Tests: Comprehensive testing is an integral part of the Casting Agency API. It includes at least one test for the success behavior of each endpoint and one test for the error behavior of each endpoint. Furthermore, at least two tests are performed to validate the RBAC implementation for each role.

*Casting Agency Specifications:*

The Casting Agency API models the operations of a company responsible for movie production and actor management. As an Executive Producer within the company, your objective is to create a system that simplifies and streamlines the entire process.

Models: The API consists of two main models:

Movies: This model represents movies and includes attributes such as "title" and "release date."

Actors: This model represents actors and includes attributes such as "name," "age," and "gender."

Endpoints: The Casting Agency API offers the following endpoints to interact with the data:

GET /actors and GET /movies: Retrieve a list of actors and movies, respectively.

DELETE /actors/ and DELETE /movies/: Delete specific actors and movies.

POST /actors and POST /movies: Add new actors and movies to the database.

PATCH /actors/ and PATCH /movies/: Modify existing actor and movie records.

Roles:

The API defines three roles with varying permissions:

Casting Assistant: This role can view details of actors and movies.

Casting Director: In addition to the permissions of a Casting Assistant, this role can add or delete actors from the database and modify actor and movie details.

Executive Producer: This role possesses all the permissions of a Casting Director and has the additional ability to add or delete movies from the database.

Tests:

To ensure the reliability and correctness of the API, the project includes the following tests:

Success Behavior Tests: For each endpoint, there is at least one test to validate its successful execution.

Error Behavior Tests: For each endpoint, there is at least one test to handle and verify error scenarios.

RBAC Tests: The API is thoroughly tested with role-based access control to ensure that each role's permissions are correctly enforced.

The Casting Agency API aims to simplify the movie-making process by providing a comprehensive and secure platform for managing actors and movies. We hope this documentation guides you in effectively utilizing the API's features and functionalities. Happy movie-making!

## Capstone Project for Udacity's Full Stack Developer Nanodegree
*Render Link: https://capstone-development.onrender.com*

*While running locally: http://localhost:5000*

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

For Linux:

```bash
export FLASK_APP=app.py
flask run --reload
```
For Windows:

```bash
set FLASK_APP=app.py
flask run --reload
```
For macOS (Mac):

```bash
export FLASK_APP=app.py
flask run --reload
```

These commands set the FLASK_APP environment variable to *app.py*, which is the entry point of the Flask application. The --reload flag enables automatic reloading of the server whenever changes are detected in the code, which is useful for development purposes. Now you're ready to start the server and use the Casting Agency API on your preferred platform!

## API Reference

## Getting Started
Base URL: This application can be run locally. The hosted version is at `https://capstone-development.onrender.com`.

## Third-Party Authentication
*Tasks:*
Setup Auth0
Create a new Auth0 Account
Select a unique tenant domain
Create a new, single page web application
Create a new API
in API Settings:
Enable RBAC
Enable Add Permissions in the Access Token
Create new API permissions:
```
get:actors-> view all actors	
get:movies-> view all movies	
delete:actors-> delete actors	
delete:movies-> delete movies	
post:actors-> post actors	
post:movies-> post movies	
patch:actors-> update actor	
patch:movies-> update movies
```
Sign into each account and make note of the JWT.
Authentication: This application requires authentication to perform various actions. All the endpoints require
various permissions, except the root (or health) endpoint, that are passed via the `Bearer` token.

The application has three different types of roles:
- Casting_Assistant
  - can only view the list of artist and movies and can view complete information for any actor or movie
  - has `get:actors, get:movies` permissions
- Casting_Director
  - can perform all the actions that `Casting_Assistant` can
  - can also create an actor and movie and also update respective information
  - has `post:actors, delete:actors, patch:actors, patch:movies, ` permissions in addition to all the permissions that `Casting_Assistant` role has
- Executive_Producer
  - can perform all the actions that `Casting_Director` can
  - can also add, delete movies
  - has `post:movies, delete:movies` permissions in addition to all the permissions that `Casting_Director` role has


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


## Deployment to Render Cloud Platform
*Prerequisites*
Before you begin, make sure you have the following:
An active Render account. If you don't have one, sign up at https://render.com/.
Your application's source code ready for deployment. Ensure it's compatible with Render's supported programming languages and frameworks.
Any necessary configurations or environment variables required for your application.

*Step 1: Create a New Service:*

1. Log in to your Render account.
2. From the Render dashboard, click on the "Create a New Service" button.
3. Select your preferred Git repository hosting platform (GitHub, GitLab, or Bitbucket) and connect it with your Render account.
4. Choose the repository containing your application code.
5. Configure the following settings:
6. Service Name: Give your service a meaningful name.
7. Environment: Choose the environment that suits your application (e.g., Docker, Node.js, Python, etc.).
8. Start Command: Specify the command required to start your application.
9. Environment Variables: Add any necessary environment variables for your application.
10. Click on "Create Service."

*Step 2: Configure Your Service:*

1. After creating the service, you'll be redirected to the service's dashboard.
2. In the dashboard, go to the "Settings" tab.
3. Review and adjust the settings as needed, including custom domains, automatic scaling, and health checks.
4. If your application requires a database, click on the "Databases" tab to set up a database and connect it to your service.
5. Save the changes

*Step 3: Deploy Your Application:*

1. In the service dashboard, click on the "Deploys" tab.
2. Select the branch or commit you want to deploy from your connected Git repository.
3. Click on the "Deploy" button to start the deployment process.
4. Monitor the deployment progress in the deploy log.
5. Once the deployment is successful, you'll receive a URL where your application is now live.

*Step 4: Manage Your Service:*

1. From the service dashboard, you can manage your application, view logs, scale your service, and make configuration changes.
2. To view logs, go to the "Logs" tab. This is useful for debugging and monitoring your application.
3. To scale your service, go to the "Scaling" tab, where you can adjust the number of instances based on your application's needs.

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


**Running test_app.py with Tokens in setup.sh**
To run the test suite test_app.py, which contains unit tests for Casting Agency application, you need to follow these steps. Before proceeding, make sure you have the required dependencies installed and the application set up, including the Flask application (app.py) and the test suite (test_app.py).

Step 1: Set Up Environment Variables in setup.sh
The setup.sh file contains environment variables, including tokens needed for authentication in the test suite. Open the setup.sh file and make sure it has the necessary environment variables defined. It should look something like this:
```
export casting_assistant_token="YOUR_CASTING_ASSISTANT_TOKEN_HERE"
export casting_director_token="YOUR_CASTING_DIRECTOR_TOKEN_HERE"
export executive_producer_token="YOUR_EXECUTIVE_PRODUCER_TOKEN_HERE"
```
Replace "YOUR_CASTING_ASSISTANT_TOKEN_HERE", "YOUR_CASTING_DIRECTOR_TOKEN_HERE", and "YOUR_EXECUTIVE_PRODUCER_TOKEN_HERE" with the actual tokens you obtained for the respective roles. Make sure to save the changes to setup.sh.

Step 2: Activate the Environment
Before running the tests, you need to activate the environment to make the environment variables in setup.sh available.

On macOS/Linux, use the following command:
```
source setup.sh
```
On Windows, use the following command:
```
source setup.sh
```
Step 3: Run the Test Suite
Now that the environment variables are set, you can run the test suite using the python command.
```
python3 test_app.py
```
Observe the output on the terminal. The test suite should execute, and you should see test results indicating which tests passed and which ones failed.