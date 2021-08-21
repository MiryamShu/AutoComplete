from data_sentence import Data_Sentence
from sentence_finder import SentenceFinder
from trie import Trie


class SearchWithChanges:
    def __init__(self):
        self.__sentence_finder = SentenceFinder()

    def get_sentence_finder(self):
        return self.__sentence_finder

    def search(self, sentence, size=5):
        raise

    def get_score(self, index, sentence):
        if index > 3:
            return len(sentence) - 1
        else:
            return len(sentence) - 5 + index
