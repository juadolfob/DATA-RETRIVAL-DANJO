from tools.scrapper.scrapper import scrapper
from tools.textproc.text import Text
from pprint import pprint
from collections import Counter
from collections import OrderedDict
from tools.list.index import Index

scrape = scrapper(['denticenter'])
results = scrape.simple()

indexed_words = Index()
normalized_text = []

for index, result in enumerate(results):
    print(str(index) + "...")

    ### ### ### TEXT                ### ### ###
    body = Text.normalize(result['body'])

    ### ### ### SENTIMENT ANALYSIS  ### ### ###



    ### ### ### INDEX               ### ### ###

    text = Text.remove_stopwords(Text.tokenize_words(body))

    indexed_words.add(dict(Counter(text)))
    print(text)

print("FINISH")

indexed_words = OrderedDict(sorted(indexed_words.items(), key=lambda kv: (kv[1])))

#pprint(indexed_words)
