import os

class Config:
    # Secret key - GUNA ENVIRONMENT VARIABLE UNTUK SECURITY
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'attendance-secret-key-2024-internship'
    
    # Database configuration
    basedir = os.path.abspath(os.path.dirname(__file__))
    
    # Render guna SQLite dalam /tmp/ folder (persistent)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'instance', 'database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Upload configuration
    UPLOAD_FOLDER = os.path.join(basedir, 'static', 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    
    # Session configuration
    SESSION_TYPE = 'filesystem'
    PERMANENT_SESSION_LIFETIME = 3600
