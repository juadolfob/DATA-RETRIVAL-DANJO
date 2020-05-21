import re

from nltk import RegexpTokenizer
from unidecode import unidecode
from nltk.corpus import stopwords
import string
from nltk.tokenize import word_tokenize
from nltk.tokenize.casual import _str_to_unicode


class Text:

    word = r"""[A-Za-z0-9]*[A-Za-z][A-Za-z0-9]*(?:(?:&|\-|_){0,1}[A-Za-z0-9]+)*"""

    @staticmethod
    def normalize(text):
        text = _str_to_unicode(text)
        text = text.lower()
        return text

    @staticmethod
    def tokenize_words(text):
        tokenizer = RegexpTokenizer(Text.word)
        return tokenizer.tokenize(text)

    @staticmethod
    def remove_stopwords(text):
        if text is str:
            return Text.remove_stopwords(Text.tokenize(text))
        elif '__iter__' in dir(text):
            stop_words = set(stopwords.words('english')).union(set(stopwords.words('spanish')))
            return [word for word in text if word not in stop_words]
        else:
            raise TypeError("Using " + str(type(text)) + ", but only integers are allowed")