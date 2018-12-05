
import artm
import pandas as pd
import re
from nltk.corpus import stopwords
import pymorphy2
from multiprocessing import cpu_count


def preprocessing_for_artm(number_of_docs_as_collection_length=False, number_of_docs=10):
    data = pd.read_csv("C:\\Users\\miga\\Desktop\\data-lws\\library\\data\\lenta_ru.csv")
    texts = data["text"]
    all_docs = ""
    morph = pymorphy2.MorphAnalyzer()
    if number_of_docs_as_collection_length:
        number_of_docs = len(texts)
    for i in range(number_of_docs):
        text = texts[i]
        all_docs += " |text "
        text = str(text).decode('utf-8')
        text = re.sub('[0-9!@#$%^&*()\[\],.<>;:"{}/~`\-+=«»—|?\n\t\']+', '', text)
        list_of_words = re.sub("(u?)\w+", ' ', text, ).split(" ")
        filtered_list_of_word = [morph.parse(w.lower())[0].normal_form
                                 for w in list_of_words if w not in stopwords.words("russian")]
        filtered_text = " ".join(filtered_list_of_word).strip()
        all_docs += filtered_text
        all_docs += "\n"
    f = open("C:\\Users\\miga\\Desktop\\data-lws\\library\\data\\lenta.txt", "w")
    f.write(all_docs)
    f.close()


def artm_plsa(batch_vectorizer, topics, topic_names, dictionary):
    model_artm = artm.ARTM(num_topics=topics, topic_names=topic_names, num_processors=cpu_count(),
                           class_ids={"text": 1}, reuse_theta=True, cache_theta=True, num_document_passes=1)
    model_artm.initialize(dictionary=dictionary)
    model_artm.scores.add(artm.PerplexityScore("perplexity", class_ids=["text"], dictionary=dictionary))
    model_artm.fit_offline(batch_vectorizer=batch_vectorizer, num_collection_passes=50)
    print("\nPeprlexity for BigARTM PLSA: ", model_artm.score_tracker["perplexity"].value[-1])


def artm_lda(batch_vectorizer, topics, dictionary):
    model_lda = artm.LDA(num_topics=topics, num_processors=cpu_count(), cache_theta=True, num_document_passes=1)
    model_lda.initialize(dictionary=dictionary)
    model_lda.fit_offline(batch_vectorizer=batch_vectorizer, num_collection_passes=50)
    print("\nPerplexity for BigARTM LDA: ", model_lda.perplexity_last_value)


def run():
    print('BigARTM version ', artm.version(), '\n\n\n')
    topics = 10
    batch_vectorizer = artm.BatchVectorizer(data_path="C:\\Users\\miga\\Desktop\\data-lws\\library\\data\\lenta.txt",
                                            data_format="vowpal_wabbit",
                                            target_folder="batches_folder_kononovich", batch_size=10)
    topic_names = ["topic#1" + str(i) for i in range(topics - 1)] + ["bcg"]
    dictionary = artm.Dictionary("dictionary")
    dictionary.gather(batch_vectorizer.data_path)
    artm_plsa(batch_vectorizer, topics, topic_names, dictionary)
    artm_lda(batch_vectorizer, topics, dictionary)


run()
