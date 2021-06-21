import unittest
from app.models import Quote


class TestQuote(unittest.TestCase):
    def setUp(self):
        self.quote = Quote("Jojoy", "To blog is to vlog")

    def test_instance(self):
        self.assertTrue(isinstance(self.quote, Quote))

    def test_init(self):
        self.assertEqual(self.quote.author, "Jojoy")
        self.assertEqual(self.quote.quote, "To blog is to vlog")
