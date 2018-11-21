import copy
import re
import pymorphy2


class Normalizer:
    morphAnalyzer = pymorphy2.MorphAnalyzer()

    @staticmethod
    def text_to_list(text):
        return re.sub("[^\w]", " ", text).split()

    @staticmethod
    def document_to_list(document):
        return re.sub("[^\w]", " ", document.get_text()).split()

    @staticmethod
    def to_normal_form(list_of_words):
        normalized_list_of_words = [Normalizer.morphAnalyzer.normal_forms(word)[0] for word in list_of_words]
        return normalized_list_of_words

    @staticmethod
    def remove_stop_words(stop_words, list_of_words):
        copy_set_of_words = copy.copy(list_of_words)
        copy_set_of_stop_words = copy.copy(stop_words)
        answer = copy.copy(copy_set_of_words)
        for word in copy_set_of_words:
            for stop_word in copy_set_of_stop_words:
                if word == stop_word:
                    answer = list(filter(lambda el: el != stop_word, answer))
        return list(answer)
