import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")
    DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///memegenerator.db")
    HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY", "")

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False