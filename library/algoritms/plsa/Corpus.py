class Corpus:

    def __init__(self):
        self.__documents = []

    def generate_corpus(self, filepath):
        from library.algoritms.plsa.Document import Document
        import pandas as pd

        data = pd.read_csv(filepath)
        documents = data["text"].tolist()
        topics = data["topic"].tolist()

        for index in range(len(documents)):
            try:
                self.__documents.append(Document(documents[index], topics[index]))  # add item after last item
            except IndexError:
                self.__documents.append(Document(documents[index], ''))

    def get_documents(self):
        return self.__documents
