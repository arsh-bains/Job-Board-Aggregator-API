# Job Board Aggregator API

A portfolio REST API built with FastAPI that aggregates remote jobs from the Remotive API. Users can register, login with JWT auth, browse/filter jobs, and save favorites.

## Tech Stack
- FastAPI + Pydantic
- PostgreSQL + SQLAlchemy
- JWT Authentication (python-jose)
- Remotive API (external jobs source)

## Features
- User registration and login
- JWT-protected endpoints
- Browse and filter remote jobs by keyword/category
- Save and manage favorite jobs per user

## Setup

1. Clone the repo
2. Create a virtual environment and install dependencies:
```bash
   pip install -r requirements.txt
```
3. Copy `.env.example` to `.env` and fill in your values
4. Run the app:
```bash
   uvicorn app.main:app --reload
```

## API Docs
Visit `http://localhost:8000/docs` for Swagger UI after running locally.