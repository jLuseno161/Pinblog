from wtforms import StringField, TextAreaField, SubmitField, SelectField
from flask_wtf import FlaskForm
from wtforms.validators import Required


class BlogForm(FlaskForm):
    """
    form for creating a blog
    """
    blog_title = StringField('Title', validators=[Required()])
    blog_content = TextAreaField('Your Blog')
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    """
        form for creating a blog comment
    """
    opinion = TextAreaField('COMMENT ON BLOG')
    submit = SubmitField('SUBMIT')
