import nltk
import operator
from collections import Counter 
class ContentAnalyzer(object):
    """This Class uses the tokenized string and python's built-in collections module to perfom analysis on text"""
    
    def __init__(self,fileContent):
        self.fileContent = fileContent

    def get_word_count(self):
        return len(self.fileContent)

    def get_word_frequency(self):
        return Counter(self.fileContent)

    def get_noun_frequency(self):
        nouns = []
        for word,pos in nltk.pos_tag(self.fileContent):
            if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'):
                nouns.append(word)
        return Counter(nouns)

    def get_adjectives_frequency(self):
        adjectives  = []
        for word,pos in nltk.pos_tag(self.fileContent):
            if (pos == 'JJ' or pos == 'JJR' or pos == 'JJS'):
                adjectives .append(word)
        return Counter(adjectives)

    def get_least_used_words(self):
        # Sorting word frequency collection into asc order and geeting the top 10
        sorted_word_count = sorted(Counter(self.fileContent).items(), key=operator.itemgetter(1),reverse=False)
        firstTen = sorted_word_count[0:10]
        return firstTen
