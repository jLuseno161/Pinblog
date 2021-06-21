import unittest
from app.models import Blog, User, Comment

class TestBlog(unittest.TestCase):
    
    def setUp(self):
        self.user_jojo = User(username = "Jojo",
                                password = "ppj",
                                email = "projectsmoringa@mail.com")
        self.new_blog = Blog(blog_title = "Title",
                            blog_content = "Hullla balloo",
                            user_id = self.user_jojo.id)
        self.new_comment = Comment(comment = "Awesome",
                                    blog_id = self.new_blog.id,
                                    user_id = self.user_jojo.id)

    def test_instance(self):
        self.assertTrue(isinstance(self.user_jojo, User))
        self.assertTrue(isinstance(self.new_blog, Blog))
        self.assertTrue(isinstance(self.new_comment, Comment))