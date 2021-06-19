from flask import (render_template, request, redirect,
                   url_for)
from app.main.forms import CommentForm, UpdateBlogForm
from app.email import mail_message
from flask import render_template, request
from . import main
from .. import db
from ..requests import get_quote
from ..models import User, Comment, Blog, Subscriber
from flask_login import current_user, login_required
from datetime import datetime


@main.route("/", methods=["GET", "BLOG"])
def index():
    blogs = Blog.get_all_blogs()
    quote = get_quote()

    if request.method == "POST":
        subs = Subscriber(email=request.form.get("subscriber"))
        db.session.add(subs)
        db.session.commit()
        mail_message("Thank you for subscribing with us",
                     "email/welcome", subs.email)
    return render_template("index.html",
                           blogs=blogs,
                           quote=quote)

# create new blog post"


@main.route("/blog/<int:id>", methods=["BLOG", "GET"])
def new_blog(id):
    blog = Blog.query.filter_by(id=id).first()
    comment = Comment.query.filter_by(blog_id=id).all()
    comment_form = CommentForm()
    comment_count = len(comment)

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
        return redirect(url_for("main.blogpost", id=blog.id))

    return render_template("blogpost.html",
                           blog=blog,
                           comments=comment,
                           comment_form=comment_form,
                           comment_count=comment_count)

# function to update blog


@main.route("/post/<int:id>/update", methods=["POST", "GET"])
@login_required
def update_blog(id):
    blog = Blog.query.filter_by(id=id).first()
    form = UpdateBlogForm()

    if form.validate_on_submit():
        blog.blog_title = form.blog_title.data
        form.blog_title.data = ""
        blog.blog_content = form.blog_content.data
        form.blog_content.data = ""

        db.session.add(blog)
        db.session.commit()
        return redirect(url_for("main.update", id=blog.id))

    return render_template("update_blog.html",
                           post=blog,
                           edit_blog=form)


# function to delete blog


@main.route("/blog/<int:id>/<int:comment_id>/delete")
def delete_comment(id, comment_id):
    blog = Blog.query.filter_by(id=id).first()
    comment = Comment.query.filter_by(id=comment_id).first()
    db.session.delete(comment)
    db.session.commit()
    return redirect(url_for("main.blogpost", id=blog.id))
