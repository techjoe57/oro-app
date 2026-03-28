"""
ENTRY POINT OF YOUR BACKEND APPLICATION

INSTRUCTIONS:
1. Create a Flask app instance
2. Load environment variables
3. Initialize database connection
4. Register blueprints (routes)
5. Run the app
"""

# TODO: import Flask
from flask import Flask
from extensions import db

# TODO: import config settings
from config import Config
# TODO: import route blueprints

# TODO: initialize Flask app
app = Flask(__name__)

# TODO: load configurations from config.py
app.config.from_object(Config)
# TODO: initialize database (SQLAlchemy)
db.init_app(app)

from models import User

with app.app_context():
     db.create_all()
# TODO: register routes (e.g., auth routes)
@app.route('/')
def index():
    return "Hello World!!"

print(app.config["SQLALCHEMY_DATABASE_URI"])

# TODO: run the app (debug mode for development)
if __name__ == '__main__':
    app.run(debug=True)