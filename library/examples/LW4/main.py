from library.algoritms.lda.LDA import LDA
from library.algoritms.lda.Corpus import Corpus
from library.algoritms.lda.StopWords import StopWords
import pandas as pd

sw = StopWords()

data = pd.read_csv("C:\\Users\\miga\\Desktop\\data-lws\\library\\data\\lenta_ru.csv")
documents = data["text"].tolist()

corpus = Corpus()
corpus.load_corpus_from_list(documents)

lda = LDA(corpus=corpus, stop_words=sw, K=20, alpha=0.5, beta=0.5, iterations=50)
print("Топы слов - ")
lda.run()
print("\n", "Распределение - ")
print("\n", lda.worddist())
