"""
DATABASE MODELS

INSTRUCTIONS:
1. Import SQLAlchemy
2. Create a User model
3. Define fields (id, username, email, password)
4. Add __repr__ method (optional)
"""

# TODO: import SQLAlchemy instance
from extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

# TODO: create User model
# Fields:
# - id (primary key)
# - username (string)
# - email (unique)
# - password (hashed)
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)

    # Hash plain text passwords
    def set_password(self, password):
        """Hashes the password and sets the hashed password column"""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Checks the provided password against the stored hash"""
        return check_password_hash(self.password_hash, password) # type: ignore
    
    def __repr__(self):
        return f"<User {self.username}>"

# TODO: create relationships if needed
