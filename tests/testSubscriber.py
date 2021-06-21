import unittest
from app.models import Subscriber


class TestSubscriber(unittest.TestCase):
    def setUp(self):
        self.mail = Subscriber(email = "Joo@gmail.com")

    def test_instance(self):
        self.assertTrue(isinstance(self.mail, Subscriber))

    def test_init(self):
        self.assertEqual(self.mail.email,"Joo@gmail.com")

    def test_save_comment(self):
        self.mail.save_subscriber()
        self.assertTrue(len(Subscriber.query.all()) > 0)
