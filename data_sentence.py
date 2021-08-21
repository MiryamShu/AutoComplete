import os
import re
import sys

from trie import Trie

from auto_complete_data import Auto_complete_data


def clear_sentence(sentence_to_clear):
    sentence_to_clear = sentence_to_clear.replace('\n', "")
    sentence_to_clear = re.sub(r'[^\w]', ' ', sentence_to_clear)
    return re.sub(' +', ' ', sentence_to_clear).lower()


class Data_Sentence:
    __instance = None
    __data_dict_tree = {}
    __words_trie = Trie()

    def __new__(cls, *args, **kwargs):
        if not Data_Sentence.__instance:
            Data_Sentence.__instance = object.__new__(cls)
        return Data_Sentence.__instance

    def load_data(self, file_path):
        files = [os.path.join(dp, f) for dp, dn, filenames in os.walk(file_path) for f in filenames if
                 os.path.splitext(f)[1] == '.txt']

        for file in files:
            with open(file, 'r', encoding="utf8") as f:
                data_file = f.readlines()
                for sentence in data_file:
                    self.add_new_sentence_to_dict(clear_sentence(sentence), sentence.replace('\n', ''), file, data_file.index(sentence))

    def add_new_sentence_to_dict(self, clear_sentence, real_sentence, file, line_number):
        sentence_list = clear_sentence.split(" ")
        for word in sentence_list:
            if word not in self.__data_dict_tree.keys():
                self.__data_dict_tree[word] = Trie()
                self.__words_trie.insert((word, word))
            sentence_value = Auto_complete_data(real_sentence, file, line_number)
            self.__data_dict_tree[word].insert(
                (clear_sentence[clear_sentence.index(word) + len(word) + 1:], sentence_value))

    def get_trie_by_word(self, word):
        try:
            return self.__data_dict_tree[word]
        except Exception:
            raise Exception("this word is not in")

    def get_sub_word(self, sub_word):
        return self.__words_trie.get_search(sub_word, self.__words_trie.root, False)[0]
