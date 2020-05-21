from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
import nltk
from pprint import pprint

test          = """
Spirit genuinely goes a long way for an ambitious indie like this, and Ovid and the Art of Love has it.
"""

class text_sentiment():

    def __init__(self, text):
        self.text = TextBlob(text)



# The polarity score is a float within the range [-1.0, 1.0]
# where negative value indicates negative text and positive
# value indicates that the given text is positive.
polarity      = sent.sentiment.polarity
# The subjectivity is a float within the range [0.0, 1.0] where
# 0.0 is very objective and 1.0 is very subjective.
subjectivity  = sent.sentiment.subjectivity

sent          = TextBlob(text, analyzer = NaiveBayesAnalyzer())
classification= sent.sentiment.classification
positive      = sent.sentiment.p_pos
negative      = sent.sentiment.p_neg
from unidecode import unidecode
print("text:          ")
pprint(unidecode(text))
print("polarity:      ",polarity)
print("subjectivity:  ",subjectivity)
print("classification:",classification)
print("positive:      ",positive)
print("negative:      ",negative)