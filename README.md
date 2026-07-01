# GitHub Issue Intelligence

A FastAPI + PostgreSQL backend that ingests GitHub issues and uses NLP/ML 
to detect duplicates and classify labels automatically.

## Tech Stack
- **Backend:** Python, FastAPI, SQLAlchemy
- **Database:** PostgreSQL
- **ML:** scikit-learn, sentence-transformers
- **Data:** pandas, Celery
- **Testing:** pytest, FastAPI TestClient
- **Deploy:** Docker, Render

## Getting Started

1. Clone the repo
2. Create a virtual environment: `python3 -m venv venv && source venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Copy `.env.example` to `.env` and fill in your values
5. Run: `uvicorn app.main:app --reload`
6. Visit: `http://localhost:8000/docs`