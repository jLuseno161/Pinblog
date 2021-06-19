from flask import render_template
from . import main




#categories
@main.route('/')
def index():
    """
        function that returns index page
    """

    # all_blogs = Blog.query.order_by('id').all()

    title = 'Pinblog'
    return render_template('index.html')
    # return render_template('index.html', title=title, all_blogs=all_blogs)

