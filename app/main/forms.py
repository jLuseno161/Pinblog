from wtforms import StringField, TextAreaField, SubmitField, SelectField
from flask_wtf import FlaskForm
from wtforms.validators import Required


class BlogForm(FlaskForm):
    """
    form for creating a blog
    """
    blog_title = StringField('Title', validators=[Required()])
    blog_content = TextAreaField("Type Away:", validators=[Required()])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    """
        form for creating a blog comment
    """
    comment = TextAreaField('COMMENT ON BLOG')
    submit = SubmitField('SUBMIT')


class UpdateBlogForm(FlaskForm):
    blog_title = StringField("Title", validators=[Required()])
    blog_content = TextAreaField("Type Away", validators=[Required()])
    submit = SubmitField("Update")

# class CommentForm(FlaskForm):
#     comment = TextAreaField("Post Comment", validators=[Required()])
    alias = StringField("Comment Alias")
#     submit = SubmitField("Comment")


class UpdateProfile(FlaskForm):
    username = StringField("Username")
    bio = TextAreaField("Bio")
    email = StringField("Email")
    submit = SubmitField("Update")
