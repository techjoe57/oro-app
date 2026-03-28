"""
AUTHENTICATION ROUTES

INSTRUCTIONS:
1. Create a blueprint for auth routes
2. Implement:
   - Register endpoint
   - Login endpoint
3. Hash passwords before saving
4. Validate user input
"""

# TODO: import Blueprint, request, jsonify
from flask import Blueprint, request, jsonify
from extensions import db
from models import User
# TODO: create blueprint
auth_bp = Blueprint('auth', __name__)

# TODO: create /register route
# Steps:
# - get JSON data
# - validate input
# - hash password
# - save user to DB
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    # Validate data for empty input
    if not data:
        return jsonify({"error":"Not data provided"}), 400
    
    # Validate data for missing input
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not username or not email or not password:
        return jsonify({"error":"All user input required"}), 400
    
    # Check if the user exists[Use email as that is unique!]
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({"message":"User already exists"}), 400
    
    # Add new user
    new_user = User(
        username=username,
        email=email
    )
    new_user.set_password(password)

    # Add user to database
    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "message": "user added!!", 
         "user":{
             "id": new_user.id,
             "username": new_user.username,
             "email": new_user.email}
             }), 201

# TODO: create /login route
# Steps:
# - check email/password
# - return success/failure response
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    # Check for empty input
    if not data:
        return jsonify({"error":"No input provided"}), 400
    # Check for data for missing input

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error":"No password or email entered!"}), 400
    
    # Check if user exists
    existing_user = User.query.filter_by(email=email).first()

    # Return error message if user does not exist
    if not existing_user:
        return jsonify({"error":"user does not exist!!"}), 404
    
    # Return error if password is wrong
    if not existing_user.check_password(password):
        return jsonify({"message": "wrong password"}), 401
    
    return jsonify({"message": "Login successful","user":{"email":email}}), 200