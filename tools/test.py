from scrapper.scrapper import scrapper
from textproc.text  import text
from pprint import pprint
from collections import Counter
from collections import OrderedDict

scrape = scrapper(['denticenter'])
results = scrape.simple()

lemma = ""
indexed_words = {}

for index, result in enumerate(results):
    print(str(index) + " ")
    normalized_body = text.alphabetic_normalize(result['body'])
    print(str(index) + " NORMALIZED")
    normalized_body = text.remove_stopwords(normalized_body)
    print(str(index) + " STOP WORDS REMOVED")
    results[index]['body'] = normalized_body
    print(str(results[index]) + " Counting and Indexing")
    result_index = dict(Counter(results[index]['body']))
    print(result_index)
    indexed_words = {k: indexed_words.get(k, 0) + result_index.get(k, 0) for k in set(indexed_words) | set(result_index)}

print("FINISH")

indexed_words = OrderedDict(sorted(indexed_words.items(), key=lambda kv:(kv[1]))) 

pprint(indexed_words)
