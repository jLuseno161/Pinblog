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
    profile_pic_path = db.Column(db.String())
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
    posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    delete = db.Column(db.Integer)
    update = db.Column(db.Integer)
    comment = db.relationship('Comment', backref='blog', lazy="dynamic")

    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    def save_delete(self: update):
        db.session.add(self)
        db.session.commit()

    def save_delete(self: update):
        db.session.add(self)
        db.session.commit()


    @classmethod
    def getblogId(cls, id):
        blog = Blog.query.filter_by(id=id).first()
        return blog

    @classmethod
    def clear_blog(cls):
        Blog.all_blog.clear()


