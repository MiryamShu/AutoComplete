from string import ascii_lowercase

from auto_complete_data import Auto_complete_data

SIZE = 5
class Trie:

    def __init__(self):
         self.root = dict()
         self.result = []

    def insert(self,word):
        root = self.root
        current_dict = root
        for letter in word[0]:
            current_dict = current_dict.setdefault(letter, {})
            if isinstance(current_dict, Auto_complete_data):
                return
        current_dict["$"] = word[1]
        self.root = root

    def get_search(self, sentence, node_to_start, bool):
        temp_node = node_to_start
        for char in sentence:
            if char in temp_node:
                temp_node = temp_node[char]
            else:
                raise Exception("this sentence not in")
        self.result = []
        self.get_sentence(temp_node)
        return self.result, temp_node



    def get_sentence(self, temp, size = SIZE, bool=True):
        temp_root = temp

        if isinstance(temp, Auto_complete_data) or isinstance(temp, str):
            if len(self.result) == size:
                return self.result
            else:
                self.result.append(temp_root)
                return
        arr = ' '+ascii_lowercase+'$' if bool else ascii_lowercase+'$'
        for char in arr:
            if char in temp_root:
                self.get_sentence(temp_root[char])
        return self.result


    def get_root(self):
        return self.root

