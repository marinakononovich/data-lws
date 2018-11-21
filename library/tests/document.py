from unittest import TestCase
from library.algoritms.lda.Document import Document


class TestDocument(TestCase):

    def setUp(self):
        self.doc = Document("Привет как дела")

    def test_get_text(self):
        self.assertEqual(self.doc.get_text(), "Привет как дела")

    def test_get_tag(self):
        self.assertEqual(self.doc.get_tag(), "")

    def test_get_text_as_list_of_words(self):
        self.assertEqual(self.doc.get_text_as_list_of_words(), ["Привет", "как", "дела"])

    def test_set_text(self):
        self.doc.set_text("Test!")
        self.assertEqual(self.doc.get_text(), "Test!")

    def test_set_tag(self):
        self.doc.set_tag("tag")
        self.assertEqual(self.doc.get_tag(), "tag")