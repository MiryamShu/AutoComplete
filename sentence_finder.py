from data_sentence import Data_Sentence, clear_sentence
from trie import Trie


class SentenceFinder:
    def __init__(self):
        self.data = Data_Sentence()
        self.__trie = Trie()


    def search(self, sentence, bool=True, node=None):
        sentence = clear_sentence(sentence)

        if node is None:
            s = sentence.split(" ")[0]
            try:
                trie = self.data.get_trie_by_word(s)
            except Exception as error:
                raise error
            sentence = " ".join(sentence.split(" ")[1:])
            node = trie.get_root()
        try:
            result = self.__trie.get_search(sentence, node, bool)  # start the search from the last common node
        except Exception as error:
            raise error

        return result

    def get_search(self, words, sentence="", size=5):
        res = []
        for word in words:
            if len(res) < size:
                try:
                    a = self.search(f"{word} {sentence}", False)[0]
                    for i in a:
                        res.append(i)
                except Exception:
                    continue
        if len(res) > size:
            res = res[0:size]
        return res