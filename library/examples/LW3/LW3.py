from library.algoritms.plsa.PLSA import PLSA
from library.algoritms.plsa.Corpus import Corpus

corpus = Corpus()
corpus.generate_corpus("C:\\Users\\miga\\Desktop\\data-lws\\library\\data\\lenta_ru.csv")

plsa = PLSA(corpus)
plsa.init_stop_words()
plsa.fit_em_algo()
