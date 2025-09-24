import os

SECRET_KEY = os.environ.get("SECRET_KEY", "your-secret-key")
SQLALCHEMY_DATABASE_URI = "sqlite:///site.db"  # Use PostgreSQL/MySQL later
SQLALCHEMY_TRACK_MODIFICATIONS = False
JWT_SECRET_KEY = "your-jwt-secret"
