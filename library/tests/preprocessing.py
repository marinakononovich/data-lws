from unittest import TestCase
from library.algoritms.lda.Preprocessing import Preprocessing
from library.algoritms.lda.Document import Document


class TestPreprocessing(TestCase):

    def setUp(self):
        pass

    def test_convert_word_list_to_text(self):
        word_list = ["re", "wa", "et", "ya"]
        text = Preprocessing.convert_word_list_to_text(word_list)
        self.assertEqual("re wa et ya", text)

    def test_lemmatize(self):
        text = Preprocessing.lemmatize("Тебя")
        self.assertEqual("тебя", text)

    def test_convert_text_to_list_of_words(self):
        word_list = Preprocessing.convert_text_to_list_of_words("Привет как дела")
        self.assertEqual(word_list, ["Привет", "как", "дела"])

    def test_convert_document_to_list_of_words(self):
        doc = Document("Привет как дела")
        word_list = Preprocessing.convert_document_to_list_of_words(doc)
        self.assertEqual(word_list, ["Привет", "как", "дела"])

    def test_convert_list_of_words_to_normal_forms(self):
        word_list = Preprocessing.convert_list_of_words_to_normal_forms(["люблю", "тебя"])
        self.assertEqual(word_list, ["любить", "ты"])

    def test_convert_word_to_normal_form(self):
        word = Preprocessing.convert_word_to_normal_form("гонит")
        self.assertEqual(word, "гнать")

    def test_remove_stop_words_from_list_of_words(self):
        answer = Preprocessing.remove_stop_words_from_list_of_words(["Я"], ["Я", "люблю", "тебя"])
        self.assertEqual(answer, ["люблю", "тебя"])