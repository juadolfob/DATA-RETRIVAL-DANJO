import collections
from textblob import TextBlob
from nltk.corpus import stopwords
from scrapper.scrapper import scrapper
from matplotlib import pyplot as plt


class test:

    def __init__(self, keywords):
        scrape = scrapper(keywords)
        scrape.remove_from_domain("www.youtube.com")
        self.results = scrape.simple()
        self.stop_words = set(stopwords.words('english') + stopwords.words('spanish'))
        #   domain stop words
        self.stop_words = self.stop_words.union(
            ["cola", "agregar", "cerrar", "correo", "mã¡s'", "gusta", "debemos", "condiciones", "contenido", "volver",
             "enviar", "cómo", "tarde", "grupo", "navegador", "fila", "mas", "reproducción", "denunciar", "comentarios",
             "videos", "vistas", "https", "“", "ver", "website", "puede", "pueden", "ser", "cargando", "video", "”",
             "si", "¿no", "â€", "cookies", "acceder", "accede", "tener", "”"])
        self.all_words = collections.Counter()
        self.polarity = 0.0
        self.subjectivity = 0.0
        self._sentiment_()
        self._words_()

    ### ### ###                     ### ### ###### ### ###                     ### ### ###
    ### ### ###                              PLOT                              ### ### ###
    ### ### ###                     ### ### ###### ### ###                     ### ### ###

    def plot(self):
        ordered_values = [item[1] for item in self.all_words.most_common()]
        total = sum(ordered_values)
        sum_ordered_values = [ordered_values[0]]
        for i in range(1, len(ordered_values)):
            sum_ordered_values.append(ordered_values[i] + sum_ordered_values[i - 1])

        plt.plot([value / total for value in ordered_values], label='occurrences')
        plt.plot([value / total for value in sum_ordered_values], label='percentage')
        plt.title('Words')
        plt.legend(loc='best')
        plt.show()

    ### ### ###                     ### ### ###### ### ###                     ### ### ###
    ### ### ###                       SENTIMENT ANALYSIS                       ### ### ###
    ### ### ###                     ### ### ###### ### ###                     ### ### ###

    def _sentiment_(self):
        for index, result in enumerate(self.results):
            text = TextBlob(result['body'])
            self.subjectivity += (text.sentiment.subjectivity / len(self.results))
            self.polarity += (text.sentiment.polarity / len(self.results))

    ### ### ###                     ### ### ###### ### ###                     ### ### ###
    ### ### ###                              STUFF                             ### ### ###
    ### ### ###                     ### ### ###### ### ###                     ### ### ###
    def _words_(self):
        for index, result in enumerate(self.results):
            text = TextBlob(result['body'])
            ### ### ### INDEX               ### ### ###
            words = text.word_counts
            for stop_word in self.stop_words:
                words.pop(stop_word, None)
            self.all_words.update(words)


def main():
    Query = "Alimentos saludables en la cuarentena"
    query = test(Query)

    print("Query                           : ", Query)
    print()
    print("Polarity     (-1: bad, 1: good) : ", query.polarity)
    print("Subjectivity ( 0: low, 1: high) : ", query.subjectivity)
    print("Words count                     : ", query.all_words.most_common(90))
    print("\n________________________________________________\n\nPer page:\n")

    for result in query.results:
        text = TextBlob(result['body'])
        print("Title                           : ", result['title'])
        print("Polarity     (-1: bad, 1: good) : ", text.polarity)
        print("Subjectivity ( 0: low, 1: high) : ", text.subjectivity)
        print("Snippet                         : ", result['snippet'])
        counter = collections.Counter()
        counter.update(text.word_counts)
        for stop_word in query.stop_words:
            counter.pop(stop_word, None)
        print("Words count                     : ", counter.most_common(9))
        print()

    query.plot()


if __name__ == "__main__":
    main()
