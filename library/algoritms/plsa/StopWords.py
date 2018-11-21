import codecs


class StopWords:

    def __init__(self):
        self._stopWords = []
        self.__pathToFileWithStopWords = "C:\\Users\\miga\\Desktop\\data-lws\\library\\data\\stopwords.dic"

    def get_stop_words(self):
        return self._stopWords

    def load_stop_words(self):
        file = codecs.open(self.__pathToFileWithStopWords, 'r', 'utf-8')
        stop_words = [line.strip() for line in file]
        file.close()
        self._stopWords = stop_words

