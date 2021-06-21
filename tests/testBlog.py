import unittest
from app.models import Blog, User


class BlogTest(unittest.TestCase):
    def setUp(self):
        self.user_id = User(username='jojo', password='jojes', email='joy@gmail.com')
        self.new_blog = Blog(blog_title='My Blog',posted_at='29/12/2000', blog_content='My blog', user_id=self.user_id.id, delete='1',update='1')


    def test_check_instance_variables(self):
        self.assertEquals(self.new_blog.blog_title, 'My Blog')
        self.assertEquals(self.new_blog.blog_content, 'My blog')
        self.assertEquals(self.new_blog.user_id, self.user_id.id)

    def test_save_blog(self):
        self.new_blog.save_blog()
        self.assertTrue(len(Blog.query.all()) > 0)

    def test_get_blog(self):
        self.new_blog.save_blog()
        self.assertTrue(self)
