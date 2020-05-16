 #!/usr/bin/python3
 # -*- coding: utf-8 -*-
 
class indexer():
    text
    def __init__(self,text):
    self.text=text
    
    regex_normalize(text):
    
    # remove links

    text = re.sub(
    r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|\n[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''',
    " ",
    text)
    
    # international alphabet to american alphabet
    text = unidecode(text)
    
        # lowercase
    text = text.lower()
    
    # regex remove non alphabetic chars
    text = re.sub(r'[^a-z]+', ' ', text)
    
    # regex remove single letters
    text = re.sub(r'((^|[^a-z])[a-z])+([^a-z]|$)', ' ', text)
    
    # regex remove multiple spaces | word separator ' '
    text = re.sub(r' +', ' ', text)
