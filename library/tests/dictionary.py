from unittest import TestCase
from library.algoritms.lda.StopWords import StopWords
from library.algoritms.lda.Dictionary import Dictionary


class TestVocabulary(TestCase):

    def setUp(self):
        self.sw = StopWords()
        self.sw.load_stop_words_from_file()
        self.vocabulary = Dictionary(self.sw, excluds_stopwords=False)

    def test_term_to_id(self):
        id_term_1 = self.vocabulary.term_to_id("тест")
        id_another_term = self.vocabulary.term_to_id("другойтест")
        id_term_2 = self.vocabulary.term_to_id("тест")
        id_not_word = self.vocabulary.term_to_id("666")
        id_stop_word = self.vocabulary.term_to_id(self.sw.get_stop_words()[0])
        self.assertEqual(id_term_1, id_term_2)
        self.assertNotEqual(id_term_1, id_another_term)
        self.assertNotEqual(id_term_2, id_another_term)
        self.assertIsNone(id_not_word)
        self.assertIsNone(id_stop_word)

    def test_size(self):
        id_term_1 = self.vocabulary.term_to_id("тест")
        id_another_term = self.vocabulary.term_to_id("другойтест")
        id_term_2 = self.vocabulary.term_to_id("тест")
        self.assertEqual(self.vocabulary.size(), len(list({id_term_1, id_term_2, id_another_term})))

    def test_doc_to_id(self):
        self.assertEqual(self.vocabulary.doc_to_ids("У студента было много двоек но среди двоек были и пятерки"),
                         [0, 1, 2, 3, 4, 5, 6, 4, 2, 7])