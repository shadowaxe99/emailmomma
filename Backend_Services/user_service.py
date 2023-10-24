```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)

# User Class/Model
class User(db.Model):
    user_id = db.Column(db.String(100), primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(200))

    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

# User Schema
class UserSchema(ma.Schema):
    class Meta:
        fields = ('user_id', 'name', 'email')

# Init schema
user_schema = UserSchema()
users_schema = UserSchema(many=True)

# Create a User
@app.route('/user', methods=['POST'])
def add_user():
    user_id = request.json['user_id']
    name = request.json['name']
    email = request.json['email']

    new_user = User(user_id, name, email)

    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user)

# Get All Users
@app.route('/user', methods=['GET'])
def get_users():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result)

# Get Single User
@app.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    return user_schema.jsonify(user)

# Update a User
@app.route('/user/<user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)

    name = request.json['name']
    email = request.json['email']

    user.name = name
    user.email = email

    db.session.commit()

    return user_schema.jsonify(user)

# Delete User
@app.route('/user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()

    return user_schema.jsonify(user)

# Run Server
if __name__ == '__main__':
    app.run(debug=True)
```