import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Application Settings
SECRET_KEY = os.getenv('SECRET_KEY', 'fallback_dev_key_change_in_production')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', '')

# Database Settings
DB_NAME = os.getenv('DB_NAME', 'users.db')

# File Upload Settings
UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', 'uploads')

# Server Settings
DEBUG = os.getenv('FLASK_DEBUG', 'False').lower() in ('true', '1', 't')
PORT = int(os.getenv('PORT', 5000))
HOST = os.getenv('HOST', '0.0.0.0')
