from flask import (render_template, request, redirect,
                   url_for)
from app.main.forms import BlogForm, CommentForm, UpdateBlogForm
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


@main.route("/blog/<int:id>", methods=["POST", "GET"])
def write_comment(id):
    blog = Blog.getBlogId(id)
    comment = Comment.get_comments(id)
    comment_form = CommentForm()

    if comment_form.validate_on_submit():
        comment = comment_form.comment.data
        comment_form.comment.data = ""
        new_comment = Comment(comment=comment,
                              user_id=current_user.id,
                              blog_id=blog.id)
        new_comment.save_comment()
        return redirect(url_for(".write_comment", id=blog.id))

    return render_template("comment.html",
                           comment_form=comment_form,
                           comment=comment,
                           blog=blog)

# function to delete blog


@main.route("/blog/<int:id>/delete")
def delete_comment(id):
    comment = Comment.getCommentId(id)
    db.session.delete(comment)
    db.session.commit()
    return redirect(url_for(".write_comment", id=comment.id))

# function to update blog
@main.route("/blog/<int:id>/delete")
def delete_blog(id):
    blog = Blog.getBlogId(id)
    db.session.delete(blog)
    db.session.commit()
    return redirect(url_for(".index", id=blog.id))

@main.route("/blog/new", methods=["POST", "GET"])
@login_required
def new_blog():
    newblogform = BlogForm()
    if newblogform.validate_on_submit():
        blog_title = newblogform.blog_title.data
        newblogform.blog_title.data = ""
        blog_content = newblogform.blog_content.data
        newblogform.blog_content.data = ""
        new_blog = Blog(blog_title=blog_title,
                        blog_content=blog_content,
                        posted_at=datetime.now(),
                        user_id=current_user.id)
        new_blog.save_blog()

    return render_template("new_blog.html",
                           newblogform=newblogform)

# function to update blog


@main.route("/blog/<int:id>/update", methods=["POST", "GET"])
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
                           blog=blog,
                           edit_blog=form)
