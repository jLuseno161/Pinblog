from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    """ 
    class modelling the users 
    """

    __tablename__ = 'users'

    #create the columns
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True)
    email = db.Column(db.String(255), unique=True, index=True)
    password_hash = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_path = db.Column(db.String())
    blog = db.relationship("Blog", backref="user", lazy="dynamic")
    comment = db.relationship("Comment", backref="user", lazy="dynamic")

    # securing passwords
    @property
    def password(self):
        raise AttributeError("You cant always get it right")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'User {self.username}'


class Blog(db.Model):
    """
    List of blogs in each category 
    """

    __tablename__ = 'blogs'

    id = db.Column(db.Integer, primary_key=True)
    blog_id = db.Column(db.Integer)
    blog_title = db.Column(db.String)
    blog_content = db.Column(db.String)
    posted_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    delete = db.Column(db.Integer)
    update = db.Column(db.Integer)
    comment = db.relationship('Comment', backref='blog', lazy="dynamic")

    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    def delete_blog(self):
        db.session.delete(self)
        db.session.commit()

    # def update_blog(self):
    #     db.session.add(self)
    #     db.session.commit()


    @classmethod
    def get_blogs(cls, id):
        blogs = Blog.query.filter_by(user_id = id).order_by(Blog.posted_at.desc()).all()
        return blogs

    @classmethod
    def get_all_blogs(cls):
        return Blog.query.order_by(Blog.posted_at).all()

class Comment(db.Model):
    """
    User comment model for each blog 
    """
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(255))
    comment_date = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    blog_id = db.Column(db.Integer, db.ForeignKey("blogs.id"))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    def delete_comment(self):
        db.session.remove(self)
        db.session.commit()

    @classmethod
    def get_comments(self, id):
        comment = Comment.query.order_by(
            Comment.time_posted.desc()).filter_by(blog_id=id).all()
        return comment

class Subscriber(db.Model):
    '''
    model class for subscribers
    '''
    __tablename__='subscribers'

    id=db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(255),unique=True,index=True)

    def save_subscriber(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'Subscriber {self.email}'

class Quote:
    """
    Blueprint class for quotes consumed from API
    """
    def __init__(self, author, quote):
        self.author = author
        self.quote = quote