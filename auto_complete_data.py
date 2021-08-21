import os


class Auto_complete_data:

    def __init__(self, completed_sentence, source, offset, score=0):
        self.__completed_sentence = completed_sentence
        self.__source = source
        self.__offset = offset
        self.__score = score

    def __str__(self):
        name = os.path.basename(self.__source)
        return f"{self.__completed_sentence} ({name} {self.__offset})\n"

    def get_score(self):
        return self.__score

    def set_score(self, new_score):
        self.__score = new_score
