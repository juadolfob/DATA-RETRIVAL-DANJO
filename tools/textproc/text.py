import re
from unidecode import unidecode
from nltk.corpus import stopwords
import nltk
from nltk.tokenize import word_tokenize


class text():
    
    @staticmethod
    def alphabetic_normalize(text):
        # remove links | VERY SLOW
        # text = re.sub(
        # r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|\n[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''',
        # " ", text)
        
        # international alphabet to american alphabet
        text = unidecode(text)
        # lowercase
        text = text.lower()
        # regex remove non alphabetic chars
        # text = re.sub(r'[^a-z]+', ' ', text)
        # regex remove single characters
        # text = re.sub(r'((^|[ ]).)+( |$)', ' ', text)
        # regex remove multiple spaces | whith word separator ' '
        text = re.sub(r' +', ' ', text)
        return text
    
    @staticmethod
    def tokenize(text):
        return word_tokenize(text)
        
    @staticmethod
    def remove_stopwords(_text):
        word_tokens = text.tokenize(_text)
        stop_words = set(stopwords.words('english')).union(set(stopwords.words('spanish')))
        _text = [w for w in word_tokens if w not in stop_words] 
        return _text
    
