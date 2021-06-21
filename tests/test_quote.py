import unittest
from app.models import Quote


class TestQuote(unittest.TestCase):
    def setUp(self):
        self.random_quote = Quote("Jojoy", "To blog is to vlog")

    def test_instance(self):
        self.assertTrue(isinstance(self.random_quote, Quote))

    def test_init(self):
        self.assertEqual(self.random_quote.author, "Jojoy")
        self.assertEqual(self.random_quote.quote, "To blog is to vlog")
