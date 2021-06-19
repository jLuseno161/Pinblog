from flask import (render_template, request, redirect,
                   url_for)
from app.main.forms import CommentForm
from app.email import mail_message
from flask import render_template, request
from . import main
from .. import db
from ..requests import get_quote
from ..models import User, Comment, Blog, Subscriber
from flask_login import current_user
from datetime import datetime


@main.route("/", methods=["GET", "BLOG"])
def index():
    blogs = Blog.get_all_blogs()
    quote = get_quote()

    if request.method == "BLOG":
        new_sub = Subscriber(email=request.form.get("subscriber"))
        db.session.add(new_sub)
        db.session.commit()
        mail_message("Thank you for subscribing to the CM blog",
                     "email/welcome", new_sub.email)
    return render_template("index.html",
                           blogs=blogs,
                           quote=quote)


@main.route("/blog/<int:id>", methods=["BLOG", "GET"])
def blog(id):
    blog = Blog.query.filter_by(id=id).first()
    comments = Comment.query.filter_by(blog_id=id).all()
    comment_form = CommentForm()
    comment_count = len(comments)

    if comment_form.validate_on_submit():
        comment = comment_form.comment.data
        comment_form.comment.data = ""
        comment_alias = comment_form.alias.data
        comment_form.alias.data = ""
        if current_user.is_authenticated:
            comment_alias = current_user.username
        new_comment = Comment(comment=comment,
                              comment_at=datetime.now(),
                              comment_by=comment_alias,
                              blog_id=id)
        new_comment.save_comment()
        return redirect(url_for("main.blog", id=blog.id))

    return render_template("blog.html",
                           blog=blog,
                           comments=comments,
                           comment_form=comment_form,
                           comment_count=comment_count)
