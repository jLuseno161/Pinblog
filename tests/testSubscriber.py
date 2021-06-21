import unittest
from app.models import Subscriber


class TestSubscriber(unittest.TestCase):
    def setUp(self):
        self.mail = Subscriber(email = "Jojo@gmail.com")

    def test_instance(self):
        self.assertTrue(isinstance(self.mail, Subscriber))

    def test_init(self):
        self.assertEqual(self.mail.email,"Jojo@gmail.com")

    def test_save_comment(self):
        self.mail.save_subscriber()
        self.assertTrue(len(Subscriber.query.all()) > 0)
