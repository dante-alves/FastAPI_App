# FastAPI Workshop – Blog Management REST API

This project is a simple REST API built using **FastAPI**. It allows users to create and manage blog posts, ensuring secure access through authentication mechanisms such as **OAuth2** and **JWT tokens**.

## Features

* User registration and authentication
* JWT-based access control
* CRUD operations for blog posts
* Protected blog endpoints requiring authentication

## Tech Stack

* Python 3.11+
* FastAPI
* SQLAlchemy
* OAuth2 with Password (Bearer) flow
* JWT (JSON Web Tokens)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/pedrohmadruga/FastAPI_workshop.git
   cd FastAPI_workshop
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**

   ```bash
   uvicorn main:app --reload
   ```

## API Usage

* Access the automatic documentation at:

  * Swagger UI: `http://localhost:8000/docs`
  * ReDoc: `http://localhost:8000/redoc`

* Authentication:

  * Obtain a JWT token by sending user credentials to the `/login` endpoint.
  * Use the token as a Bearer token in the Authorization header when accessing protected routes like `/blog`.

## Project Structure

```
FastAPI_workshop/
├── blog/                   Main application package.
├───── repository/          Contains CRUD logic and database operations.
├───── routers/             Organizes API routes/endpoints.
├───── database.py          Database connection setup.
├───── hashing.py           Password hashing utilities.
├───── main.py              Application entry point.
├───── models.py            SQLAlchemy ORM models.
├───── oauth2.py            OAuth2 and JWT authentication logic.
├───── schemas.py           Pydantic models for request and response validation.
├───── token.py             Token-related utilities.

├── blog.db                 SQLite database file.
└── requirements.txt        List of Python dependencies.
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Author

Pedro Madruga