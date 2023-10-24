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

# Forum Post Class/Model
class ForumPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(100), unique=True)
    title = db.Column(db.String(200))
    content = db.Column(db.String(2000))

    def __init__(self, user_id, title, content):
        self.user_id = user_id
        self.title = title
        self.content = content

# Forum Post Schema
class ForumPostSchema(ma.Schema):
    class Meta:
        fields = ('id', 'user_id', 'title', 'content')

# Init schema
forum_post_schema = ForumPostSchema()
forum_posts_schema = ForumPostSchema(many=True)

# Create a Forum Post
@app.route('/forum_post', methods=['POST'])
def add_forum_post():
    user_id = request.json['user_id']
    title = request.json['title']
    content = request.json['content']

    new_forum_post = ForumPost(user_id, title, content)

    db.session.add(new_forum_post)
    db.session.commit()

    return forum_post_schema.jsonify(new_forum_post)

# Get All Forum Posts
@app.route('/forum_post', methods=['GET'])
def get_forum_posts():
    all_forum_posts = ForumPost.query.all()
    result = forum_posts_schema.dump(all_forum_posts)
    return jsonify(result)

# Get Single Forum Posts
@app.route('/forum_post/<id>', methods=['GET'])
def get_forum_post(id):
    forum_post = ForumPost.query.get(id)
    return forum_post_schema.jsonify(forum_post)

# Update a Forum Post
@app.route('/forum_post/<id>', methods=['PUT'])
def update_forum_post(id):
    forum_post = ForumPost.query.get(id)

    user_id = request.json['user_id']
    title = request.json['title']
    content = request.json['content']

    forum_post.user_id = user_id
    forum_post.title = title
    forum_post.content = content

    db.session.commit()

    return forum_post_schema.jsonify(forum_post)

# Delete Forum Post
@app.route('/forum_post/<id>', methods=['DELETE'])
def delete_forum_post(id):
    forum_post = ForumPost.query.get(id)
    db.session.delete(forum_post)
    db.session.commit()

    return forum_post_schema.jsonify(forum_post)

# Run Server
if __name__ == '__main__':
    app.run(debug=True)
```