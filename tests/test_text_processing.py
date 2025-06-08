import unittest
from my_awesome_lib.text_processing import word_count, reverse_words

class TestTextProcessing(unittest.TestCase):
    def test_word_count(self):
        self.assertEqual(word_count("hello world"), 2)

    def test_word_count_empty(self):
        self.assertEqual(word_count(""), 0)

    def test_word_count_invalid(self):
        with self.assertRaises(ValueError): word_count(None)

    def test_reverse_words(self):
        self.assertEqual(reverse_words("a b c"), "c b a")

    def test_reverse_words_single(self):
        self.assertEqual(reverse_words("hello"), "hello")

    def test_reverse_words_invalid(self):
        with self.assertRaises(ValueError): reverse_words(None)
