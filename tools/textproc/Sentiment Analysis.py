 #!/usr/bin/python3
 # -*- coding: utf-8 -*-
 
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
import nltk

text          = """Most cartoon characters have a deep mental subnormality, where behavior that is unnecessarily incorrect or idiotic is thrown at the screen as efforts of entertainment, and extreme levels of confidence and cheerfulness, do not do better, than diminishing it. The plot of these cartoons, exist only because of their protagonist beyond-belief idiocy.
Idiocy should be painful, shameful, instead more times than it is desirable, it is portrayed as the best trait someone could have."""

sent          = TextBlob(text)

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

print("polarity:      ",polarity)
print("subjectivity:  ",subjectivity)
print("classification:",classification)
print("positive:      ",positive)
print("negative:      ",negative)
